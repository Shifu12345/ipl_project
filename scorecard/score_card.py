import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from match_summary.match_summary_functions import MatchSummaryFunctions

class ScoreCard(MatchSummaryFunctions):
    def __init__(self,data):
        super().__init__(data)
        
    def get_score_card(self,df_score):
    # Create an empty DataFrame with the correct column names
        season=self.get_season()
        match_number=self.get_match_number()
        # Convert innings to DataFrame and explode overs
        df_innings = pd.DataFrame(self.data['innings']).explode('team')
        # Loop through each over
        for j,over  in df_innings.iterrows():
            team=over['team']
            overs = over.overs # List of deliveries
            
            # Iterate through each row (delivery)
            for over in overs:
                over_number=over.get('over')+1
                deliveries=over.get('deliveries')
                n=0
                for i in deliveries:
                    n=n+1
                    batter_strike=i.get('batter')
                    bowler = i.get('bowler')
                    batter_non_strike = i.get('non_striker')
                    wides=i.get('extras',{}).get('wides',0)
                    is_wide='Y' if wides>0 else 'N'
                    legbyes=i.get('extras',{}).get('legbyes',0)
                    is_legbye='Y' if legbyes>0 else 'N'
                    no_ball=i.get('extras',{}).get('noballs',0)
                    is_no_ball='Y' if no_ball>0 else 'Y'
                    runs = i.get('runs')
                    batter_runs = runs.get('batter', 0)
                    is_four='Y' if batter_runs==4 else 'N'
                    is_six='Y' if batter_runs==6 else 'N'
                    extras = runs.get('extras', 0)

                # Create a new row as a DataFrame (with correct column names)
                    df_temp = pd.DataFrame([[season,match_number,
                        team,bowler, batter_strike, batter_non_strike, over_number, n, 
                        batter_runs, is_four, is_six, is_wide, is_no_ball, is_legbye, 
                        wides, no_ball, extras, 'N', 'N', 'N'
                    ]], columns=df_score.columns)
        #             df_scorecard = pd.DataFrame(columns=['season','match_number','team',
        #     'bowler', 'batter_strike', 'batter_non_strike', 'over_number', 'ball_number', 
        #     'batter_runs', 'is_six', 'is_four', 'is_wide', 'is_no_ball', 'is_legbye', 
        #     'wides', 'no_ball', 'extras', 'is_wicket', 'how_out', 'fielder'
        # ])

                    # Append to df_score
                    df_score = pd.concat([df_score, df_temp], ignore_index=True)

        # Display the result
        return df_score
        