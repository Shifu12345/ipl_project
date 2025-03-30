import pandas as pd
import sys
import os
# import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger
from match_summary.match_summary_functions import MatchSummaryFunctions

class MatchSummary(MatchSummaryFunctions):
    
    def __init__(self, data):
        super().__init__(data)

    def match_summary_fun(self, df_match_summary):
        # logger.info("Creating match summary data frame")
        """Creates a DataFrame summarizing the match."""
        season= self.get_season()
        match_number = self.get_match_number() or 0
        # logger.info(f"Season: {season}, Match: {match_number}")
        team1 = self.data['info']['teams'][0]
        team2 = self.data['info']['teams'][1]
        toss = self.data['info']['toss']['winner'] + ' won the toss and decided to ' + self.data['info']['toss']['decision'] + ' first'
        city = self.data.get('info', {}).get('city')
        match_date = self.data['info']['dates'][0]
        winning_team=self.data.get('info',{}).get('event',{}).get('winner',{}) or None
        losing_team = team1 if team2 == winning_team else team2 if team1 == winning_team else "No Result"
        match_referee = ', '.join(self.data.get('info', {}).get('officials', {}).get('match_referees', []))
        reserve_umpires = ", ".join(self.data.get('info', {}).get('officials', {}).get('reserve_umpires', [])) or None
        tv_umpire = ", ".join(self.data.get('info', {}).get('officials', {}).get('tv_umpires', [])) or None
        on_field_umpire = ", ".join(self.data.get('info', {}).get('officials', {}).get('umpires', []))
        match_result = self.get_match_result()
        player_of_match = ", ".join(self.data.get('info', {}).get('player_of_match', [])) or None

        # Creating temporary DataFrame for match summary data
        temp = pd.DataFrame([[season, match_number, match_date, team1, team2, toss, match_result,
                              winning_team,losing_team,player_of_match,
                              city, on_field_umpire, tv_umpire, match_referee, reserve_umpires]],
                            columns=['season', 'match_number', 'match_date', 'Team1', 'Team2', 'Toss won by',
                                     'winning_team','loosing_team','match_result', 'player_of_match', 'city', 'on_field_umpire',
                                     'tv_umpire', 'match_refree', 'reserve_umpires'])

        df_match_summary = pd.concat([df_match_summary, temp], ignore_index=True)
        
        return df_match_summary
