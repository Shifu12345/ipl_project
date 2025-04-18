import sys
import os
import pandas as pd
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from match_summary.match_summary_functions import MatchSummaryFunctions
from dev import configs


class ScoreCard(MatchSummaryFunctions):
    def __init__(self, data=None):
        super().__init__(data)

    def get_score_card(self, data, df_score):
        process_start = datetime.datetime.now()
        df_temp = pd.DataFrame(columns=configs.score_card_columns)

        season = int(self.get_season(data))
        match_number = self.get_match_number(data)

        # Convert innings to DataFrame and iterate
        for inning in data['innings']:
            team = inning['team']
            overs = inning['overs']  # List of overs

            for over in overs:
                over_number = over.get('over') + 1
                deliveries = over.get('deliveries', [])

                ball_number = 0
                for delivery in deliveries:
                    ball_number += 1

                    batter_strike = delivery.get('batter')
                    bowler = delivery.get('bowler')
                    batter_non_strike = delivery.get('non_striker')

                    extras_info = delivery.get('extras', {})
                    wides = extras_info.get('wides', 0)
                    no_ball = extras_info.get('noballs', 0)
                    legbyes = extras_info.get('legbyes', 0)

                    is_wide = 'Y' if wides > 0 else 'N'
                    is_no_ball = 'Y' if no_ball > 0 else 'N'
                    is_legbye = 'Y' if legbyes > 0 else 'N'

                    if is_wide == 'Y' or is_no_ball == 'Y':
                        ball_number -= 1  # Don't count extras as legal balls

                    runs = delivery.get('runs', {})
                    batter_runs = runs.get('batter', 0)
                    extras = runs.get('extras', 0)

                    is_four = 'Y' if batter_runs == 4 else 'N'
                    is_six = 'Y' if batter_runs == 6 else 'N'

                    is_wicket, who_out, how_out, fielder = self.get_wicket(delivery)

                    df_temp.loc[len(df_temp)] = [
    season, match_number, team, bowler, batter_strike, batter_non_strike,
    over_number, ball_number, batter_runs, is_six, is_four,
    is_wide, is_no_ball, is_legbye, wides, no_ball, extras,
    is_wicket, how_out, who_out, fielder
]


        # Append to main df_score
        if not df_temp.empty:
            scorecard_records = len(df_temp)
            records_added = scorecard_records
            df_score = pd.concat([df_score, df_temp], ignore_index=True)
            success_ind = 'Y'
        else:
            success_ind = 'N'
            records_added = 0
            scorecard_records = 0

        process_end = datetime.datetime.now()

        return df_score, scorecard_records, success_ind, records_added, process_start, process_start, process_end

    def get_wicket(self, delivery):
        wickets = delivery.get('wickets', [])
        if wickets:
            w = wickets[0]  # Usually only one per delivery
            how_out = w.get('kind', 'N/A')
            who_out = w.get('player_out', 'N/A')
            fielders = w.get('fielders', [])
            fielder = fielders[0].get('name', 'N/A') if fielders else 'N/A'
            return 'Y', who_out, how_out, fielder
        return 'N', 'N/A', 'N/A', 'N/A'

        