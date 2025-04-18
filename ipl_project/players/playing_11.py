import pandas as pd
import sys
import os
import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger

from match_summary.match_summary_functions import MatchSummaryFunctions
from dev import configs


class Playing11(MatchSummaryFunctions):
    def __init__(self, data=None):
        super().__init__(data)

    def players_in_match(self, data, df_playing_11):
        process_start = datetime.datetime.now()
        temp_df = pd.DataFrame(columns=configs.playing_11_columns)

        players = self.get_players(data)
        match_number = self.get_match_number(data) or 0
        season = self.get_season(data)

        team_keys = list(data['info']['players'].keys())

        for player_name in players:
            # Fallback in case player is not found in registry
            player_number = data['info']['registry']['people'].get(player_name, None)

            # Determine team
            if player_name in data['info']['players'].get(team_keys[0], []):
                team = team_keys[0]
            else:
                team = team_keys[1]

            temp_df.loc[len(temp_df)] = [
                player_name,
                player_number,
                team,
                match_number,
                season
            ]

        # Append to final DF and audit trail
        if not temp_df.empty:
            playing_11_records = len(temp_df)
            records_added = playing_11_records
            df_playing_11 = pd.concat([df_playing_11, temp_df], ignore_index=True)
            success_ind = 'Y'
        else:
            playing_11_records = 0
            records_added = 0
            success_ind = 'N'

        process_end = datetime.datetime.now()

        return df_playing_11, playing_11_records, success_ind, records_added, process_start, process_end
