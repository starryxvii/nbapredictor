from nba_api.stats.endpoints import commonteamroster
import pandas as pd, sys, os
from datetime import datetime, timedelta
import time, players

team_id=1610612766 #Team IDs 1610612737-1610612766
path = open("/data/players22-23.csv") #

teams = []
team = commonteamroster.CommonTeamRoster(team_id=team_id).get_normalized_dict()['CommonTeamRoster']

roster = {  "PLAYER_ID": [], "PLAYER_NAME": [], "PTS": [], "AST": [], "REB": [], "PIE": [], "TEAM": []    }

for plr in range(len(team)-1):
    data = players.getPlayerData(team[plr]['PLAYER_ID'])
    if data is not None: 
        roster["PLAYER_ID"].append(data["PLAYER_ID"])
        roster["PLAYER_NAME"].append(data["PLAYER_NAME"])
        roster["PTS"].append(data["PTS"])
        roster["AST"].append(data["AST"])
        roster["REB"].append(data["REB"])
        if data.get("PIE"): roster["PIE"].append(data["PIE"])
        else: roster["PIE"].append(0)
        roster["TEAM"].append(team_id)
teams.append(roster)
print(roster)
df1 = pd.read_csv(path)
df2 = pd.DataFrame(data=roster)
df3 = pd.concat([df1,df2])
df3.to_csv(path, index=False)
#print(teams[0])

# make all players into a csv classified by team with stats
# implement as strategy (compare average pie))
