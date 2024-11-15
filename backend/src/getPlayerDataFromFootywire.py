import os
import pandas as pd

from datetime import datetime
from datetime import date

#Calc Age from Season Start inputis birthday mmm Year
def calcAge(year, datetime_str):
    try :
        birthday= datetime.strptime(datetime_str, '%d %b %Y')
        #seasonStartDate
        now = date(year,3,31)
        ageinYear = now.year - birthday.year - ((now.month, now.day) < (birthday.month, birthday.day))
    except:
        ageinYear = 0
    return(ageinYear)

def load_data(team, year):
    url = f"https://www.footywire.com/afl/footy/tp-{team}?year={year}"
    html = pd.read_html(url, header = 0)
    print (html[8])
    print ("html 10")
    print (html[10])
    df = html[10]
    return df

#return 2nd part as first name followed by last name separated with space
def buildFullName (s):
    s1 = s.split(", ")
    return (s1[1] + " " + s1[0])

year = int(input("Enter the year of Player List :"))

teams = ["carlton-blues", "essendon-bombers", "western-bulldogs",
         "geelong-cats", "adelaide-crows", "melbourne-demons",
         "fremantle-dockers", "west-coast-eagles"
         ,"greater-western-sydney-giants", "hawthorn-hawks",
         "kangaroos", "brisbane-lions", "collingwood-magpies",
         "port-adelaide-power", "st-kilda-saints"
         ,"gold-coast-suns", "sydney-swans", "richmond-tigers"]

base_path = os.path.join(os.path.dirname(__file__), '../../data')
outFile = os.path.join(base_path, f"AflPlayersFootywire{year}.xlsx")
for idx, team in enumerate(teams):
    df = load_data(team, year)
    print (df.head(5))
    #Add Team name to the data frame
    #split the Teamname using- from last and get only 1 element
    #gold-coast-suns will be converted to Suns
    df['Team'] = team.rsplit('-', 1)[1].capitalize() if '-' in team else team.capitalize() 

    # Concatenate team data into playerList
    playerList = pd.concat([playerList, df], ignore_index=True) if idx > 0 else df
print (playerList.head(15))
playerList['Name'] = playerList['Name'].apply(lambda s : s.rstrip(" R"))


playerList['Name'] = playerList['Name'].apply(lambda s : buildFullName(s) )
playerList['Age'] = playerList['Date of Birth'].apply(lambda s : calcAge(year, s))
playerList.to_excel(outFile, index=False)
