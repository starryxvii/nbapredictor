from nba_api.stats.endpoints import winprobabilitypbp
import pandas as pd
import time
from datetime import datetime, timedelta


def getGame(id):
    game = winprobabilitypbp.WinProbabilityPBP(id).game_info.get_dict()["data"][0]
    # GAME_ID, GAME_DATE, HOME_TEAM_ID, HOME_TEAM_ABR, HOME_TEAM_PTS, VISITOR_TEAM_ID, VISITOR_TEAM_ABR, VISITOR_TEAM_PTS
    return game


start = 22100001 #
path = "/data/season21-22.csv"

d = {
    "GAME_ID": [],
    "GAME_DATE": [],
    "HOME_TEAM_ID": [],
    "HOME_TEAM_ABR": [],
    "HOME_TEAM_PTS": [],
    "VISITOR_TEAM_ID": [],
    "VISITOR_TEAM_ABR": [],
    "VISITOR_TEAM_PTS": [],
}


def populateCSV(file, log=False):
    print(
        f"Started population at {datetime.now().strftime('%H:%M:%S')} in {file}!"
    )
    for i in range(1230):
        startTime = datetime.now()
        game = getGame(f"00{start+i}")
        d["GAME_ID"].append(game[0])
        d["GAME_DATE"].append(game[1])
        d["HOME_TEAM_ID"].append(game[2])
        d["HOME_TEAM_ABR"].append(game[3])
        d["HOME_TEAM_PTS"].append(game[4])
        d["VISITOR_TEAM_ID"].append(game[5])
        d["VISITOR_TEAM_ABR"].append(game[6])
        d["VISITOR_TEAM_PTS"].append(game[7])
        if log:
            print(
                f"Logged {game[3]} @ {game[6]} game #{game[0]} at {datetime.now().strftime('%H:%M:%S')}"
            )
        endTime = datetime.now()
        dur = (endTime - startTime).total_seconds()
        time.sleep(0 if 2 - dur < 0 else 2 - dur)
    df = pd.DataFrame(data=d)
    df.to_csv(file, index=False)
    print(
        f"Completed population successfully at {datetime.now().strftime('%H:%M:%S')} in {file}!"
    )
#populateCSV(path, True)