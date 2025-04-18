

drop table `synthetic-style-439016-b9.ipl.match_summary`;
CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.match_summary` (
  season INTEGER,
  match_number INTEGER,
  match_date STRING,
  Team1 STRING,
  Team2 STRING,
  Toss STRING,
  Toss_decision STRING,
  winning_team STRING,
  loosing_team STRING,
  match_result STRING,
  player_of_match STRING,
  city STRING,
  on_field_umpire STRING,
  tv_umpire STRING,
  match_refree STRING,
  reserve_umpires STRING
);

drop table `synthetic-style-439016-b9.ipl.playing_11`;
CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.playing_11` (
  player_name STRING,
  player_number STRING,
  team STRING,
  match_number INTEGER,
  season INTEGER
);

drop table `synthetic-style-439016-b9.ipl.ball_by_ball_score_card`;
CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.ball_by_ball_score_card` (
  season INTEGER,
  match_number INTEGER,
  team STRING,
  bowler STRING,
  batter_strike STRING,
  batter_non_strike STRING,
  over_number INTEGER,
  ball_number INTEGER,
  batter_runs INTEGER,
  is_six STRING,
  is_four STRING,
  is_wide STRING,
  is_no_ball STRING,
  is_legbye STRING,
  wides INTEGER,
  no_ball INTEGER,
  extras INTEGER,
  is_wicket STRING,
  how_out STRING,
  who_out STRING,
  fielder STRING
);

-- drop table `synthetic-style-439016-b9.ipl.audit_table`
-- CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.audit_table` (
--   process_start TIMESTAMP,
--   files_processed INTEGER,
--   match_summary_records INTEGER,
--   playing_11_records INTEGER,
--   scorecard_records INTEGER,
--   match_summary_table_appended STRING,
--   playing_11_table_appended STRING,
--   scorecard_table_appended STRING,
--   status STRING,
--   process_end TIMESTAMP
-- );

drop table `synthetic-style-439016-b9.ipl.file_audit_table`
CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.file_audit_table` (
  file_name STRING,
  processed_flag STRING,
  process_start TIMESTAMP,
  process_end TIMESTAMP
);

drop table `synthetic-style-439016-b9.ipl.process_audit_table`;
CREATE OR REPLACE TABLE `synthetic-style-439016-b9.ipl.process_audit` (
  run_number STRING,
  process_start DATETIME,
  file_name STRING,
  process_name STRING,
  table_name STRING,
  records_added INT64,
  success_ind STRING,
  process_end DATETIME
);