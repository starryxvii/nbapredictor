import pandas as pd

p1 = open("../data/season22-23.csv")
p2 = open("../data/season21-22.csv")

df = pd.read_csv(p2)
df.index+=1

df2 = pd.read_csv(p1)
df2.index+=1


win_total = 0
game_samples = 1230
for x in range (game_samples):
    game = df.loc[x+1]

    home_team_odds = 0
    visitor_team_odds = 0

    #gets games fron season prior 
    for y in range(1230): 
        game2 = df2.loc[y+1] 
        if (game2.HOME_TEAM_ID == game.HOME_TEAM_ID or game2.HOME_TEAM_ID == game.VISITOR_TEAM_ID) and (game2.VISITOR_TEAM_ID == game.HOME_TEAM_ID or game2.VISITOR_TEAM_ID == game.VISITOR_TEAM_ID):
            winning_team2 = game2.HOME_TEAM_ABR if game2.HOME_TEAM_PTS > game2.VISITOR_TEAM_PTS else game2.VISITOR_TEAM_ABR
            if winning_team2 == game.HOME_TEAM_ABR: 
                home_team_odds += 1
            else: 
                visitor_team_odds += 1

    predicted_winner = game.HOME_TEAM_ABR if home_team_odds > visitor_team_odds else game.VISITOR_TEAM_ABR
    
    winning_team = game.HOME_TEAM_ABR if game.HOME_TEAM_PTS > game.VISITOR_TEAM_PTS else game.VISITOR_TEAM_ABR
    if predicted_winner == winning_team:
        win_total +=1

print("winrate = ", win_total/game_samples)

# 52.6% rate