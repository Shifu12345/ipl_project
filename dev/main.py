import pandas as pd
import os
import configs
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger  # Import your logging setup

#Importing Classes
from match_summary.read_json import ReadJson
from write.local_writer import LocalWriter
from match_summary.match_summary_df_creation import MatchSummary
from players.playing_11 import Playing11
from scorecard.score_card import ScoreCard
from utilities.delete_files import DeleteFiles
from utilities.download_scorecard import Downloader

# Download and extract class
downloader=Downloader()
downloader.downloader_and_extract()

df_match_summary=pd.DataFrame(columns=['season','match_number','match_date','Team1','Team2','Toss',
                            'winning_team','loosing_team','match_result','player_of_match','city','on_field_umpire',
                            'tv_umpire','match_refree','reserve_umpires'])

df_playing_11=pd.DataFrame(columns=['player_name','player_number','team','match_number','season'])

df_score=pd.DataFrame(columns=['season','match_number','team',
        'bowler', 'batter_strike', 'batter_non_strike', 'over_number', 'ball_number', 
        'batter_runs', 'is_six', 'is_four', 'is_wide', 'is_no_ball', 'is_legbye', 
        'wides', 'no_ball', 'extras', 'is_wicket', 'how_out', 'fielder'
    ])


score_card_directory=os.path.join(configs.base_directory_data,configs.scorecard_local_directory)
logger.info(f"Scorecards directory : {score_card_directory}")
for file in os.listdir(score_card_directory):
    logger.info(f"File parsed is {file}")
    if file.endswith(".json"):
        file_path = os.path.join(score_card_directory, file)
        
        read_json=ReadJson(file_path)
        # logger.info("****************Creating Read JSON class**************")
        data=read_json.read_match_file()
            
        match_summary = MatchSummary(data)
        # logger.info("****************Creating Match Summary class**************")
        df_match_summary = match_summary.match_summary_fun(df_match_summary)
        
        playing_11 = Playing11(data)
        # logger.info("****************Creating Playing 11 class**************")
        df_playing_11 = playing_11.players_in_match(df_playing_11)
        
        score_card=ScoreCard(data)
        df_score=score_card.get_score_card(df_score)
        

df_match_summary = df_match_summary.astype({
    "season": "int",
    "match_number": "int",
    "match_date": "str",
    "Team1": "str",
    "Team2": "str",
    "Toss": "str",
    "winning_team": "str",
    "loosing_team": "str",
    "match_result": "str",
    "player_of_match": "str",
    "city": "str",
    "on_field_umpire": "str",
    "tv_umpire": "str",
    "match_refree": "str",
    "reserve_umpires": "str",
    "Toss won by": "str"
})

df_playing_11 = df_playing_11.astype({
    "player_name": "str",
    "player_number": "str",
    "team": "str",
    "match_number": "int",
    "season": "int"
})


# Calling Writer class
writer=LocalWriter()

# Match Summary
logger.info("****************Creating Local Writer class**************")
writer.parquet_writer_local(df_match_summary,configs.match_summary_parquet_directory_local)#by season
logger.info("****************Creating Local Writer class**************")
logger.info(f"match summary parquet file created in {configs.match_summary_parquet_directory_local}")  
writer.csv_writer_local(df_match_summary,configs.match_summary_csv_path_local)
logger.info("****************Creating Local Writer class**************")
logger.info(f"match summary csv file created in {configs.match_summary_csv_path_local}")  

# Playing_11
writer.csv_writer_local(df_playing_11,configs.playing_11_csv_local)
logger.info(f"Playing 11 csv file created in {configs.playing_11_csv_local}")  
writer.parquet_writer_local(df_playing_11,configs.playing_11_parquet_local)#by season
logger.info(f"Playing 11 parquet file created in {configs.playing_11_parquet_local}")

# Ball by Ball
writer.parquet_writer_local(df_score,configs.scorecard_match_wise_parquet)
logger.info(f"Ball by Ball parquet file created in {configs.scorecard_match_wise_parquet}")

delete_files=DeleteFiles()
delete_files.remove_zip_files(configs.base_directory_data)
logger.info("Deleted old .zip files from local")

print("Done")