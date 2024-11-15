import os
import pandas as pd
from datetime import datetime
from datetime import date


# Calc Age from Season Start input is birthday mmm Year
def calcAge(year, datetime_str):
    try:
        birthday = datetime.strptime(datetime_str, '%d %b %Y')
        # seasonStartDate
        now = date(year, 3, 31)
        ageinYear = now.year - birthday.year - ((now.month, now.day) < (birthday.month, birthday.day))
    except:
        ageinYear = 0
    return ageinYear


def load_data(team, year):
    # url = f"https://www.footywire.com/afl/footy/tp-{team}?year={year}"
    url = f"https://www.draftguru.com.au/lists/{year}/{team}"
    html = pd.read_html(url, header=0)
    df = html[0]
    return df


# return 2nd part as first name followed by last name separated with space
def buildFullName(s):
    s1 = s.split(", ")
    return s1[1] + " " + s1[0]


year = int(input("Enter the year of Player List :"))

teams = ["carlton-blues", "essendon-bombers", "western-bulldogs-bulldogs",
         "geelong-cats", "adelaide-crows", "melbourne-demons",
         "fremantle-dockers", "west-coast-eagles", "greater-western-sydney-giants", 
         "hawthorn-hawks", "north-melbourne-kangaroos", "brisbane-lions", 
         "collingwood-magpies", "port-adelaide-power", "st-kilda-saints", 
         "gold-coast-suns", "sydney-swans", "richmond-tigers"]

dirName = "C:/Users/sunil/Projects/footy/data" 
outFile = os.path.join(dirName, f"AflPlayersDraftGuru{year}.xlsx")

for idx, team in enumerate(teams):
    clubName = team.rsplit('-', 1)[0]

    df = load_data(clubName, year)
    print(clubName)
    # Add Team name to the data frame
    # split the Teamname using - from last and get only 1 element
    # gold-coast-suns will be converted to Suns
    df['Team'] = team.rsplit('-', 1)[1].capitalize() if '-' in team else team.capitalize()        

    # Rename the first column (index 0) to "No"
    df = df.rename(columns={df.columns[0]: "No"})

    # Drop the columns with headings '#' and 'Unnamed: 1'
    df = df.drop(columns=['#', 'Unnamed: 1'], errors='ignore')


    # Clean Age, Height, and Weight columns
    df['Age'] = df['Age'].str.replace('yr', '', regex=False)
    df['Height'] = df['Height'].str.replace('cm', '', regex=False)
    df['Weight'] = df['Weight'].str.replace('kg', '', regex=False)

    # Split Drafted column into DraftRank, DraftYear, and DraftType
    draft_data = df['Drafted'].str.extract(r'#(\d+)\s+(\w+)\s+(\d+)')
    df['DraftRank'] = draft_data[0]
    df['DraftType'] = draft_data[1]
    df['DraftYear'] = draft_data[2]
    df = df.drop(columns=['Drafted'])  # Remove original Drafted column

    # Replace non-breaking space (code 160) with a regular space (code 32) in the 'Player' column
    df['Player'] = df['Player'].str.replace('\u00A0', ' ', regex=True)

    # Concatenate team data into playerList
    playerList = pd.concat([playerList, df], ignore_index=True) if idx > 0 else df

print(playerList.head(15))
# playerList['Name'] = playerList['Name'].apply(lambda s : s.rstrip(" R"))

# playerList['Name'] = playerList['Name'].apply(lambda s : buildFullName(s) )
# playerList['Age'] = playerList['Date of Birth'].apply(lambda s : calcAge(year, s))
playerList.to_excel(outFile, index=False)
print("Data saved to", outFile)