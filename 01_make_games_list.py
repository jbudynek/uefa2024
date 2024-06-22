import pandas as pd
import numpy as np

files = ['input_data/uefa-data-before-euro24.csv','input_data/uefa-data-euro24.csv']

df = pd.DataFrame(columns=["date", "team_1", "team_2", "win_1", "win_2"])

idx = 0
invalid = 0
for file in files:

    df2 = pd.read_csv(file)

    print(df2)
    num_entries = df2.shape
    print(f"file {file} has {num_entries} entries")

    for row in df2.itertuples():
        #d,t1,t2,s1,s2,win1,win2

        print(row.Index, row.d, row.t1,row.t2,row.s1,row.s2,row.win1,row.win2)
        valid = True
        date = row.d
        team_1 = row.t1
        team_2 = row.t2
        win_1 = row.win1
        win_2 = row.win2
        if (
            (team_1 == None)
            or (team_2 == None)
            or (win_1 == False and win_2 == False)
        ):
            print(f"{date} {team_1} {team_2} {win_1} {win_2}")
            # print(match)
            valid = False
            invalid += 1
        if valid:
            df.loc[idx] = [date, team_1, team_2, win_1, win_2]
            idx += 1

    print(f"file {file} done")


df.sort_values("date", inplace=True)
df.reset_index(drop=True, inplace=True)
print(df)

print(f"{invalid} invalid matches")

unique_values_col1 = df['team_1'].unique()
unique_values_col2 = df['team_2'].unique()

merged_array = np.concatenate((unique_values_col1, unique_values_col2))
print(f"Merged array: {merged_array}")
merged_set = sorted(list(set(merged_array)))
print(f"Merged set: {merged_set}")

df.to_csv("games/all_games.csv")

quit()
