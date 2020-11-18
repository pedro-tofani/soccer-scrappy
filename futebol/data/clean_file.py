import pandas as pd


def load_data():
    data = pd.read_csv('all_games_csv.csv', sep=',')
    return data


def replace_values_nan_empty(df, column, replace_value, replace_find):
    df[column] = df[column].fillna(0)
    df[column].replace(replace_find, replace_value, inplace = True)
    return df


def replace_percentual(value):
  return float(str(value).strip().split('%')[0])


table = load_data()
table['home_team_possession'] = table['home_team_possession'].map(replace_percentual)
table['away_team_possession'] = table['away_team_possession'].map(replace_percentual)

media_home = table['home_team_possession'].mean()
media_away = table['away_team_possession'].mean()

table = replace_values_nan_empty(table, 'home_team_possession', media_home, 0)
table = replace_values_nan_empty(table, 'away_team_possession', media_away, 0)

columns_to_replace_to_zero = [
 'home_team_goals',
 'away_team_goals',
 'home_team_shots_on_target',
 'away_team_shots_on_target',
 'home_team_shots_woodwork',
 'away_team_shots_woodwork',
 'home_team_shots_blocked',
 'away_team_shots_blocked',
 'home_team_shots_off_target',
 'away_team_shots_off_target',
 'home_team_attacks',
 'away_team_attacks',
 'home_team_dangerous_attacks',
 'away_team_dangerous_attacks',
 'home_team_offsides',
 'away_team_offsides',
 'home_team_penalties',
 'away_team_penalties',
 'home_team_yellow_red_cards',
 'away_team_yellow_red_cards',
 'home_team_yellow_cards',
 'away_team_yellow_cards',
 'home_team_red_cards',
 'away_team_red_cards',
 'home_team_fouls',
 'away_team_fouls',
 'home_team_free_kicks',
 'away_team_free_kicks',
 'home_team_goal_kicks',
 'away_team_goal_kicks',
 'home_team_throw_ins',
 'away_team_throw_ins',
 'home_team_corners',
 'away_team_corners']

for column in columns_to_replace_to_zero:
   table = replace_values_nan_empty(table, column, 0, ' ')

table.to_csv( "all_games_cddsv.csv", index=False, encoding='utf-8-sig')
