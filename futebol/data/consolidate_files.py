import glob
import pandas as pd


extension = 'csv'
all_files = [i for i in glob.glob('*.{}'.format(extension))]

print(all_files)

all_games_csv = pd.concat([pd.read_csv(f) for f in all_files ])

all_games_csv.to_csv( "all_games_csv.csv", index=False, encoding='utf-8-sig')