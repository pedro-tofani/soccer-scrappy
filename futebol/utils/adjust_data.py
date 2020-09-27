import csv
import re


def fix_teams_names(team_name):
    return team_name.replace("-", " ").title()


def write_csv(data):
    dialect = csv.excel
    dialect.delimiter = ";"
    headers = data.keys()

    with open("data.csv", "a", newline="") as file:
        dict_writer = csv.DictWriter(file, fieldnames=headers, dialect=dialect)
        dict_writer.writerow(data)


def get_season_round(season_string):
    return re.sub(r"\D", "", season_string)
