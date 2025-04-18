import pandas as pd
import sys
import os
import datetime
# import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger
from match_summary.match_summary_functions import MatchSummaryFunctions

class MatchSummary(MatchSummaryFunctions):
    
    def __init__(self,data=None):
        super().__init__(data)

    def match_summary_fun(self,data, df_match_summary):
        process_start=datetime.datetime.now()
        # logger.info("Creating match summary data frame")
        """Creates a DataFrame summarizing the match."""
        season= self.get_season(data)
        match_number = self.get_match_number(data) or 0
        # logger.info(f"Season: {season}, Match: {match_number}")
        team1 = data['info']['teams'][0]
        team2 = data['info']['teams'][1]
        toss = data['info']['toss']['winner'] or None
        toss_decision=data['info']['toss']['decision'] or None
        city = data.get('info', {}).get('city')
        match_date = data['info']['dates'][0]
        winning_team = data.get('info', {}).get('outcome', {}).get('winner','')
        losing_team = team1 if team2 == winning_team else team2 if team1 == winning_team else "No Result"
        match_referee = ', '.join(data.get('info', {}).get('officials', {}).get('match_referees', []))
        reserve_umpires = ", ".join(data.get('info', {}).get('officials', {}).get('reserve_umpires', [])) or None
        tv_umpire = ", ".join(data.get('info', {}).get('officials', {}).get('tv_umpires', [])) or None
        on_field_umpire = ", ".join(data.get('info', {}).get('officials', {}).get('umpires', []))
        match_result = self.get_match_result(data)
        player_of_match = ", ".join(data.get('info', {}).get('player_of_match', [])) or None

        # Creating temporary DataFrame for match summary data
        temp = pd.DataFrame([[season, match_number, match_date,team1,
                              team2, toss,toss_decision,winning_team,
                              losing_team,match_result,player_of_match, city,
                              on_field_umpire, tv_umpire,match_referee, reserve_umpires
                              ]],
                            columns=['season', 'match_number', 'match_date','Team1', 
                                     'Team2', 'Toss', 'Toss_decision','winning_team',
                                     'loosing_team','match_result','player_of_match', 'city',
                                     'on_field_umpire','tv_umpire', 'match_refree', 'reserve_umpires'])
        if len(temp)!=0:
            match_summary_records=len(temp)
            records_added=match_summary_records
            df_match_summary = pd.concat([df_match_summary, temp], ignore_index=True)
            success_ind = 'Y'
        else:
            success_ind='N'
        process_end=datetime.datetime.now()
        
        return df_match_summary,match_date,match_summary_records,records_added,process_start,success_ind,records_added,process_end
