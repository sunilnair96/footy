import os
import pandas as pd
from pprint import pprint
import re

def load_data( year):
    url =f"https://www.footywire.com/afl/footy/ft_match_list?year={year}"
    html = pd.read_html(url, header = 0)
    #index 9 has the required value
    '''
    for index, value in enumerate(html):
        print(f"Index: {index}, Value: {value}")   
    '''
    df = html[9]
    # Use the second row as column headings
    new_columns = df.iloc[0]
    df = df[1:].reset_index(drop=True)
    df.columns = new_columns

    return df

def process_data(df, year):

    # Add a new 'Year' column and populate it with the 'year' variable
    df.insert(0, 'Year', year)
    # Add a new 'Round' column and initialize it to 0
    df.insert(1, 'Round', 0)

    current_round = 1
    delete_rows = False  # Flag to indicate whether to delete rows
    #delete all rows from Qualifying finals    
    for index, row in df.iterrows():
        if delete_rows:
            df.drop(index, inplace=True)
            continue        
        if pd.isnull(row['Date']):
            df.drop(index, inplace=True)
        elif re.match(r'^Round \d+$', row['Date']):
            current_round = int(row['Date'].split()[-1])
            df.drop(index, inplace=True)
        elif re.match(r'^Date', row['Date']):
            df.drop(index, inplace=True)
        elif row['Date'] == 'Qualifying Final':
            df.drop(index, inplace=True)
            delete_rows = True            
        else:
            df.at[index, 'Round'] = current_round

    # Split the "Home v Away Teams" column into "Home" and "Away" columns
    df[['Home', 'Away']] = df['Home v Away Teams'].str.split(' v ', expand=True)
    df.drop(columns=['Home v Away Teams'], inplace=True)
    
    df.reset_index(drop=True, inplace=True)
    return df
#game = 'supercoach'
game ='dream_team'
year = 2024

dirName = "Data"
outFile = os.path.join(dirName, f"fixture_{year}.xlsx")


df = load_data( year)
df = process_data(df, year)

pprint(df)
#print(df.columns)
df.to_excel(outFile, index=False)