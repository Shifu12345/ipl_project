import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utilities.logging_cust import logger

class MatchSummaryFunctions:
    
    # 1. Match Number: Identifies the match within the tournament/series.
    # 2. Players (Both 11s): Lists both teams' playing XI.
    # 3. Match Results: Stores the match outcome (Winner, Margin, etc.).
    # 4. Season Number: Specifies the season/year of the match.
      
    def __init__(self,data=None):
        self.data=data
    #1    
    def get_match_number(self,data):
        # logger.info("Getting match number")
        """Extracts the match number from the given match data."""
        # data.get('info', {}).get('event', {}).get('match_number', 0)
        match_number=data['info']['event'].get('match_number',0)
        return int(match_number)
    #2
    def get_players(self,data):
        # logger.info("Getting players list")
        """Extracts playing XI details and updates df_playing_11 DataFrame."""
        match_refree = data['info']['officials']['match_referees']
        reserve_umpires = data.get('info', {}).get('officials', {}).get('reserve_umpires', [])
        tv_umpire = data.get('info', {}).get('officials', {}).get('tv_umpires', [])
        on_field_umpire = data['info']['officials']['umpires']

        # Extract all names from the registry
        name = list(data['info']['registry']['people'].keys())

        # Remove all match officials from the 'name' list
        players = list(set(name) - set(match_refree) - set(reserve_umpires) - set(tv_umpire) - set(on_field_umpire))
        
        return players
    #3
    def get_match_result(self,data):
        # logger.info("Getting match result")
        """Extracts the match result from the given match data."""
        
        outcome = data.get('info', {}).get('outcome', {})
        
        if 'winner' in outcome:
            by_key = list(outcome.get('by', {}).keys())[0] if 'by' in outcome else ''
            if by_key:
                return f"{outcome['winner']} win by {outcome['by'][by_key]} {by_key}"
            else:
                return f"{outcome['winner']} win"
        
        elif outcome.get('result') == 'tie':
            return "Match tied"
        
        elif 'eliminator' in outcome:
            return f"Eliminator match: {outcome['eliminator']}"
        
        return "No result"
    #4
    def get_season(self,data):
        # logger.info("Getting season number")
        if data['info']['season']=='2007/08':
            season = 2008  
        elif data['info']['season']=='2020/21':
            season = 2020
        elif data['info']['season']=='2009/10':
            season = 2010
        else:
            season=data.get('info',{}).get('season',{})
        
        return int(season)
