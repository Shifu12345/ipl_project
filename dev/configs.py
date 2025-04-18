from google.cloud import bigquery

# For downloading files from cricsheet.org
sheets_url="https://cricsheet.org/downloads/ipl_json.zip"
zip_file_name = "ipl_json"
base_directory_data=r"C:\Users\harsh\Downloads\ipl_project\data"


#AWS directory


#GCP directory
gcp_project_name="synthetic-style-439016-b9"
service_account_bq_json=r"C:\Users\harsh\Downloads\ipl_project\keys\bq_key.json"
dataset='ipl'
dataset_prod='ipl_prod'
service_account_bq_json=r"E:\Sivadatt K\ipl_json\bq_files_and_py\synthetic-style-439016-b9-3f5b87717517.json"
dataset='ipl'
ball_by_ball_table='ball_by_ball_score_card'
playing_11_table='playing_11'
match_summary_table='match_summary'
player_registry_table='player_registry'
audit_table='audit_table'
file_audit_table='file_audit_table'
file_audit_table='files_audit_table'
process_audit_table='process_audit_table'   

process_audit_columns = [
    "run_number",
    "process_start",
    "file_name",
    "process_name",
    "table_name",
    "records_added",
    "success_ind",
    "process_end"
]


process_audit_schema = [
    bigquery.SchemaField("run_number", "STRING"),
    bigquery.SchemaField("process_start", "DATETIME"),
    bigquery.SchemaField("file_name", "STRING"),
    bigquery.SchemaField("process_name", "STRING"),
    bigquery.SchemaField("table_name", "STRING"),
    bigquery.SchemaField("records_added", "INT64"),
    bigquery.SchemaField("success_ind", "STRING"),
    bigquery.SchemaField("process_end", "DATETIME"),
]
match_summary_columns=['season','match_number','match_date','Team1','Team2',
                    'Toss','winning_team','loosing_team','match_result',
                    'player_of_match','city','on_field_umpire','tv_umpire',
                    'match_refree','reserve_umpires']

match_summary_schema=[
    bigquery.SchemaField("season", "INTEGER"),  # Ensure BigQuery treats it as INTEGER
    bigquery.SchemaField("match_number", "INTEGER"),
    bigquery.SchemaField("match_date", "STRING"),
    bigquery.SchemaField("Team1", "STRING"),
    bigquery.SchemaField("Team2", "STRING"),
    bigquery.SchemaField("Toss", "STRING"),
    bigquery.SchemaField("Toss_decision", "STRING"),
    bigquery.SchemaField("winning_team", "STRING"),
    bigquery.SchemaField("loosing_team", "STRING"),
    bigquery.SchemaField("match_result", "STRING"),
    bigquery.SchemaField("player_of_match", "STRING"),
    bigquery.SchemaField("city", "STRING"),
    bigquery.SchemaField("on_field_umpire", "STRING"),
    bigquery.SchemaField("tv_umpire", "STRING"),
    bigquery.SchemaField("match_refree", "STRING"),
    bigquery.SchemaField("reserve_umpires", "STRING"),
]
playing_11_columns=['player_name','player_number','team','match_number','season']

playing_11_schema=[
    bigquery.SchemaField('player_name',"STRING"),
    bigquery.SchemaField('player_number',"STRING"),
    bigquery.SchemaField('team',"STRING"),
    bigquery.SchemaField('match_number',"INTEGER"),
    bigquery.SchemaField('season',"INTEGER")
]


score_card_columns=['season','match_number','team',
        'bowler', 'batter_strike', 'batter_non_strike', 'over_number', 'ball_number', 
        'batter_runs', 'is_six', 'is_four', 'is_wide', 'is_no_ball', 'is_legbye', 
        'wides', 'no_ball', 'extras', 'is_wicket', 'how_out','who_out', 'fielder'
    ]


scorecard_schema=[
    bigquery.SchemaField("season", "INTEGER"),
    bigquery.SchemaField("match_number", "INTEGER"),
    bigquery.SchemaField("team", "STRING"),
    bigquery.SchemaField("bowler", "STRING"),
    bigquery.SchemaField("batter_strike", "STRING"),
    bigquery.SchemaField("batter_non_strike", "STRING"),
    bigquery.SchemaField("over_number", "INTEGER"),
    bigquery.SchemaField("ball_number", "INTEGER"),
    bigquery.SchemaField("batter_runs", "INTEGER"),
    bigquery.SchemaField("is_six", "STRING"),
    bigquery.SchemaField("is_four", "STRING"),
    bigquery.SchemaField("is_wide", "STRING"),
    bigquery.SchemaField("is_no_ball", "STRING"),
    bigquery.SchemaField("is_legbye", "STRING"),
    bigquery.SchemaField("wides", "INTEGER"),
    bigquery.SchemaField("no_ball", "INTEGER"),
    bigquery.SchemaField("extras", "INTEGER"),
    bigquery.SchemaField("is_wicket", "STRING"),
    bigquery.SchemaField("how_out", "STRING"),
    bigquery.SchemaField("who_out", "STRING"),
    bigquery.SchemaField("fielder", "STRING"),
    bigquery.SchemaField("legbyes", "INTEGER"),
    bigquery.SchemaField("extras", "INTEGER"),
    bigquery.SchemaField("is_wicket", "STRING"),
    bigquery.SchemaField("how_out", "STRING"),
    bigquery.SchemaField("fielder", "STRING")    
]



audit_table_schema=[
    bigquery.SchemaField("process_start","TIMESTAMP"),
    bigquery.SchemaField("files_processed","INTEGER"),
    bigquery.SchemaField("match_summary_records","INTEGER"),
    bigquery.SchemaField("playing_11_records","INTEGER"),
    bigquery.SchemaField("scorecard_records","INTEGER"),
    bigquery.SchemaField("match_summary_table_appended","STRING"),
    bigquery.SchemaField("playing_11_table_appended","STRING"),
    bigquery.SchemaField("scorecard_table_appended","STRING"),
    bigquery.SchemaField("status","STRING"),
    bigquery.SchemaField("process_end","TIMESTAMP")
]

file_audit_schema=[
    bigquery.SchemaField("file_name","STRING"),
    bigquery.SchemaField("processed_flag","STRING"),
    bigquery.SchemaField("process_start","TIMESTAMP"),
    bigquery.SchemaField("process_end","TIMESTAMP")
]

file_audit_columns=["file_name","processed_flag","process_start","process_end"]

#Azure directory

# Local path
scorecard_local_directory_sample=r"sample_files"
scorecard_local_directory=r"ipl_json_files"

match_summary_parquet_directory_local=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\match_summary\parquet"
match_summary_csv_path_local=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\match_summary\csv\match_summary_data.csv"

playing_11_csv_local=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\playing_11\csv\playing_11.csv"
playing_11_parquet_local=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\playing_11\parquet"
    
scorecard_match_wise_parquet=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\scorecard\parquet"
scorecard_match_wise_csv=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\scorecard\csv\scorecard.csv"
scorecard_match_wise_csv=r"C:\Users\harsh\Downloads\ipl_project\data\processed_files\scorecard\csv\scorecard.csv"
