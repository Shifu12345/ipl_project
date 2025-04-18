import pandas as pd
import os
import configs
import sys
import datetime

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
from utilities.GCP import  connect_bq

df_match_summary=pd.DataFrame(columns=configs.match_summary_columns)
df_playing_11=pd.DataFrame(columns=configs.playing_11_columns)
df_score=pd.DataFrame(columns=configs.score_card_columns)
df_process_audit_table=pd.DataFrame(columns=configs.process_audit_columns)
df_file_audit_table=pd.DataFrame(columns=configs.file_audit_columns)


process_start=datetime.datetime.now()
process_start_fa=process_start
processed_flag='N'
#connect to Big-Query
gcp_connection=connect_bq.PythonGCPConnect(configs.service_account_bq_json)

# files_processed_list=gcp_connection.get_files_processed()
files_processed_list=[]

# Initialising process audit
run_number=gcp_connection.process_audit_run_number_query()
file_name = 'N/A'
process_name = 'Initialised'
table_name='N/A'
records_added=0
success_ind = 'Y'
process_end = datetime.datetime.now()

df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]
if success_ind=='N':
    gcp_connection.connect_to_bq(df_process_audit_table,
                                configs.dataset,
                                configs.process_audit_table,
                                configs.process_audit_schema)


# Download and extract class

downloader=Downloader()
downloader.downloader_and_extract()
run_number=gcp_connection.process_audit_run_number_query()

file_name = 'N/A'
process_name = 'Download and Extract'
table_name='N/A'
records_added=0
success_ind = 'Y'
process_end = datetime.datetime.now()
df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]

if success_ind=='N':
    gcp_connection.connect_to_bq(df_process_audit_table,
                                configs.dataset,
                                configs.process_audit_table,
                                configs.process_audit_schema)

score_card_directory=os.path.join(configs.base_directory_data,configs.scorecard_local_directory)
logger.info(f"Scorecards directory : {score_card_directory}")
for file in os.listdir(score_card_directory):
    logger.info(f"File parsed is {file}")
    if file.endswith(".json"):
        file_path = os.path.join(score_card_directory, file)
        process_name = 'Read JSON'
        file_name = file
        if file_name not in files_processed_list:
            read_json=ReadJson()
            # logger.info("****************Creating Read JSON class**************")
            data,process_start,success_ind,process_end,table_name=read_json.read_match_file(file_path)
            
            df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]
            if success_ind=='N':
                gcp_connection.connect_to_bq(df_process_audit_table,
                                            configs.dataset,
                                            configs.process_audit_table,
                                            configs.process_audit_schema)
                
            process_name = 'Match Summary'
            table_name=configs.match_summary_table
            match_summary = MatchSummary()
            # logger.info("****************Creating Match Summary class**************")
            df_match_summary,match_date,match_summary_records,records_added,process_start,success_ind,records_added,process_end = match_summary.match_summary_fun(data,df_match_summary)
            
            df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]
            if success_ind=='N':
                gcp_connection.connect_to_bq(df_process_audit_table,
                                            configs.dataset,
                                            configs.process_audit_table,
                                            configs.process_audit_schema)
            
            process_name = 'Playing 11'
            table_name=configs.playing_11_table
            playing_11 = Playing11()
            # logger.info("****************Creating Playing 11 class**************")
            df_playing_11, playing_11_records, success_ind, records_added, process_start, process_end = playing_11.players_in_match(data,df_playing_11)
            
            df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]
            if success_ind=='N':
                gcp_connection.connect_to_bq(df_process_audit_table,
                                            configs.dataset,
                                            configs.process_audit_table,
                                            configs.process_audit_schema)
            process_name = 'Score Card'
            table_name=configs.ball_by_ball_table
            score_card=ScoreCard()
            df_score, scorecard_records, success_ind, records_added, process_start, process_start, process_end=score_card.get_score_card(data,df_score)
            
            df_process_audit_table.loc[len(df_process_audit_table)]=[run_number, process_start,file_name, process_name, table_name, records_added, success_ind, process_end]
            if success_ind=='N':
                gcp_connection.connect_to_bq(df_process_audit_table,
                                            configs.dataset,
                                            configs.process_audit_table,
                                            configs.process_audit_schema)
            
            processed_flag='Y'
            df_file_audit_table.loc[len(df_file_audit_table)]=[file_name,processed_flag,process_start_fa,process_end]
            
        else:
            logger.info(f"{file_name} is already processed")

gcp_connection.connect_to_bq(df_process_audit_table,
                            configs.dataset,
                            configs.process_audit_table,
                            configs.process_audit_schema)

gcp_connection.connect_to_bq(df_file_audit_table,
                                configs.dataset,
                                configs.file_audit_table,
                                configs.file_audit_schema)

gcp_connection.connect_to_bq(df_match_summary,
                                configs.dataset,
                                configs.match_summary_table,
                                configs.match_summary_schema)

gcp_connection.connect_to_bq(df_playing_11,
                                configs.dataset,
                                configs.playing_11_table,
                                configs.playing_11_schema)

gcp_connection.connect_to_bq(df_score,
                                configs.dataset,
                                configs.ball_by_ball_table,
                                configs.scorecard_schema)


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