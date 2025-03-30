## Folder Structure
ipl_project/
│── dev/                     # Main codebase
│   ├── main.py              # Entry point for the pipeline
│   ├── configs.py           # Configuration file (paths, URLs, etc.)
│
├── match_summary/           # Handles match summary processing
│   ├── read_json.py         # Reads JSON files
│   ├── match_summary_df_creation.py # Creates match summary dataframe
│
├── scorecard/               # Processes ball-by-ball data
│   ├── score_card.py        # Extracts scorecard information
│
├── players/                 # Handles player information
│   ├── playing_11.py        # Extracts Playing 11 data
│
├── write/                   # Manages file writing
│   ├── local_writer.py      # Writes CSV & Parquet files
│
├── utilities/               # Utility scripts
│   ├── delete_files.py      # Deletes old .zip files
│   ├── download_scorecard.py# Downloads and extracts JSON files
│   ├── logging_cust.py      # Logging configuration
│
├── data/                    # Data storage (ignored in .gitignore)
│   ├── ipl_json_files/      # Extracted JSON files
│   ├── match_summary/       # Processed match summaries
│   ├── playing_11/          # Processed playing 11 data
│   ├── scorecard_ball_by_ball/ # Processed scorecards
│
├── .gitignore               # Ignore unnecessary files
├── README.md                # Project documentation (this file)
