import pandas as pd
import glob as g

data = []
file_list = g.glob('*.csv')
for file in file_list:
    df = pd.read_csv(file)
    data.append(df)

all_data = pd.concat(data, axis=0, ignore_index=True)

drop_double_data = all_data.drop_duplicates()
# drop_double_data = data.drop_duplicates()
# drop_empty_data = data['owner_location'].dropna(axis=0)

all_data.to_csv("third_data2019.csv", index=False)


