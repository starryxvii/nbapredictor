from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo


def getPlayerObject(query, searchBy='name'):
    res={}
    match searchBy:
        case 'name':
            res = players.find_players_by_full_name(query)[0]
        case 'id':
            res = players.find_player_by_id(query)
    return(res)

def getPlayerData(q):
    if type(q) == str:
        return getHeadlineStats(getPlayerObject(q)['id'])
    else:
        stats = getHeadlineStats(q)
        if stats != {}:
            return stats

def getHeadlineStats(id):
    dic=commonplayerinfo.CommonPlayerInfo(player_id=id, league_id_nullable='00').get_normalized_dict()
    if dic['PlayerHeadlineStats']: return(dic['PlayerHeadlineStats'][0])