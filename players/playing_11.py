import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger

from match_summary.match_summary_functions import MatchSummaryFunctions


class Playing11(MatchSummaryFunctions):
    def __init__(self, data):
        super().__init__(data)

    def players_in_match(self, df_playing_11):
        players=self.get_players()
        match_number = self.get_match_number()  
        season=self.get_season()
        # logger.info(f"Season: {season}, Match: {match_number}")
        # logger.info(f"Getting players list")
        team_keys = list(self.data['info']['players'].keys())  # Store once

        for player_name in players:
            player_number = self.data['info']['registry']['people'][player_name]

            # Determine the player's team
            if player_name in self.data['info']['players'][team_keys[0]]:
                team = team_keys[0]
            else:
                team = team_keys[1]

            # logger.info(f"Create a temporary DataFrame for each player")
            temp_df = pd.DataFrame([[player_name, player_number, team, match_number, season]],
                                   columns=['player_name', 'player_number', 'team', 'match_number', 'season'])

            # logger.info("Append to df_playing_11")
            df_playing_11 = pd.concat([df_playing_11, temp_df], ignore_index=True)

        return df_playing_11
