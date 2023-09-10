import pandas as pd
from nba_api.stats.static import teams
df = pd.read_csv(open("data/players22-23.csv"))

#team = df[df['TEAM'] == 1610612743]
#print(team["PIE"].mean())

season = pd.read_csv(open("data/season21-22.csv"))

def predict(mop): 
    win_total = 0
    game_samples = 1230
    games_called = 0
    for x in range (game_samples-1):
        current_game = season.loc[x]

        home_team_id = current_game.HOME_TEAM_ID
        visitor_team_id = current_game.VISITOR_TEAM_ID
        
        team1 = df[df['TEAM'] == home_team_id]
        home_pie = team1["PIE"].mean()

        team2 = df[df['TEAM'] == visitor_team_id]
        visitor_pie = team2["PIE"].mean()

        winning_team = 1232134
        if visitor_pie > home_pie + mop: 
            predicted_winner = visitor_team_id
            winning_team = current_game.HOME_TEAM_ID if current_game.HOME_TEAM_PTS > current_game.VISITOR_TEAM_PTS else current_game.VISITOR_TEAM_ID
            if predicted_winner == winning_team: 
                win_total +=1
            games_called += 1
        elif home_pie > visitor_pie + mop: 
            predicted_winner = home_team_id
            winning_team = current_game.HOME_TEAM_ID if current_game.HOME_TEAM_PTS > current_game.VISITOR_TEAM_PTS else current_game.VISITOR_TEAM_ID
            if predicted_winner == winning_team: 
                win_total +=1
            games_called += 1
        
        game = season.loc[x+1]
    return games_called, win_total/games_called

def team_predict(team1, team2):
    home_team_id = teams.find_team_by_abbreviation(team1)['id']
    visitor_team_id = teams.find_team_by_abbreviation(team2)['id']
    team1 = df[df['TEAM'] == home_team_id]
    home_pie = team1["PIE"].mean()

    team2 = df[df['TEAM'] == visitor_team_id]
    visitor_pie = team2["PIE"].mean()

    if home_pie > visitor_pie: 
        predicted_winner = home_team_id
    else:
        predicted_winner = visitor_team_id
    winner_string = teams.find_team_name_by_id(predicted_winner)['full_name']
    home_string = teams.find_team_name_by_id(home_team_id)['nickname']
    visitor_string = teams.find_team_name_by_id(visitor_team_id)['nickname']
    return(f"Predicted winner: {winner_string}, by a margin of {abs(home_pie - visitor_pie)}\n{home_string} PIE: {home_pie} / {visitor_string} PIE: {visitor_pie}")