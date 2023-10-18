from nba_api.stats.endpoints import leaguestandings
from nba_api.live.nba.endpoints import scoreboard

def getCurrentGames():
    games = scoreboard.ScoreBoard()
    gamesData = games.get_dict()
    gameList = []
    for game in gamesData['scoreboard']['games']:
        gameStatus = game['gameStatusText']
        homeTeam = game['homeTeam']['teamCity'] + " " + game['homeTeam']['teamName']
        homeScore = game['homeTeam']['score']
        awayTeam = game['awayTeam']['teamCity'] + " " + game['awayTeam']['teamName']
        awayScore = game['awayTeam']['score']
        gameInfo = awayTeam + " @ " + homeTeam + " / " + str(awayScore) + ":" + str(homeScore) + " / " + gameStatus
        gameList.append(gameInfo)
    return gameList


def getCurrentStandingsByDiv():
    standings = leaguestandings.LeagueStandings()
    standingsData = standings.get_dict()
    teamList = []
    for x in standingsData['resultSets']:
        for y in x['rowSet']:
            teamName = y[3]+ " " + y[4]
            teamDiv = y[9]
            teamDivRank = y[11]
            teamRecord = y[16]
            teamWinPct = y[14]
            teamInfo = {
                "teamName": teamName,
                "teamDiv": teamDiv,
                "teamDivRank": str(teamDivRank),
                "teamRecord": teamRecord,
                "teamWinPCT": str(teamWinPct),
            }
            teamList.append(teamInfo)
    return teamList

def getCurrentStandingsByConf():
    standings = leaguestandings.LeagueStandings()
    standingsData = standings.get_dict()
    teamList = []
    for x in standingsData['resultSets']:
        for y in x['rowSet']:
            teamName = y[3]+ " " + y[4]
            teamConf = y[5]
            teamConfRank = y[7]
            teamRecord = y[16]
            teamWinPct = y[14]
            teamInfo = {
                "teamName": teamName,
                "teamConf": teamConf,
                "teamConfRank": str(teamConfRank),
                "teamRecord": teamRecord,
                "teamWinPCT": str(teamWinPct),
            }
            teamList.append(teamInfo)
    return teamList
