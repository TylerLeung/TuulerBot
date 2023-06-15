import requests

API_URL = "https://statsapi.web.nhl.com/api/v1"


def view_standings_by_division():
    reply = requests.get(API_URL+"/standings/byDivision", params={"Content-type": "application/json"})
    data = reply.json()

    teamList = []
    for records in data["records"]:
        divName = records["division"]["name"]
        for teamRecord in records["teamRecords"]:
            teamName = teamRecord["team"]["name"]
            teamWins = teamRecord["leagueRecord"]["wins"]
            teamLoss = teamRecord["leagueRecord"]["losses"]
            teamOTL = teamRecord["leagueRecord"]["ot"]
            teamPoints = teamRecord["points"]
            teamRec = str(teamWins) + "-" + str(teamLoss) + "-" + str(teamOTL)
            teamInfo = {"name": teamName,
                        "record": teamRec,
                        "points": teamPoints}
            teamInfoDiv = {"divName": divName, "teamInfo": teamInfo}
            teamList.append(teamInfoDiv)

    return teamList


def view_standings_by_conference():
    reply = requests.get(API_URL+"/standings/byConference", params={"Content-type": "application/json"})
    data = reply.json()

    teamList = []
    for records in data["records"]:
        confName = records["conference"]["name"]
        for teamRecord in records["teamRecords"]:
            teamName = teamRecord["team"]["name"]
            teamWins = teamRecord["leagueRecord"]["wins"]
            teamLoss = teamRecord["leagueRecord"]["losses"]
            teamOTL = teamRecord["leagueRecord"]["ot"]
            teamPoints = teamRecord["points"]
            teamRec = str(teamWins) + "-" + str(teamLoss) + "-" + str(teamOTL)
            teamInfo = {"name": teamName,
                        "record": teamRec,
                        "points": teamPoints}
            teamInfoConf = {"confName": confName, "teamInfo": teamInfo}
            teamList.append(teamInfoConf)

    return teamList


def view_standings_by_league():
    reply = requests.get(API_URL + "/standings/byLeague", params={"Content-type": "application/json"})
    data = reply.json()

    teamList = []
    for records in data["records"]:
        for teamRecord in records["teamRecords"]:
            teamName = teamRecord["team"]["name"]
            teamWins = teamRecord["leagueRecord"]["wins"]
            teamLoss = teamRecord["leagueRecord"]["losses"]
            teamOTL = teamRecord["leagueRecord"]["ot"]
            teamPoints = teamRecord["points"]
            teamRec = str(teamWins) + "-" + str(teamLoss) + "-" + str(teamOTL)
            teamInfo = {"name": teamName,
                        "record": teamRec,
                        "points": teamPoints}
            teamList.append(teamInfo)

    return teamList


def view_current_scores():
    reply = requests.get(API_URL + "/schedule", params={"Content-type": "application/json"})
    data = reply.json()
    gameList = []
    for date in data["dates"]:
        for game in date["games"]:
            homeTeam = game["teams"]["home"]["team"]["name"]
            awayTeam = game["teams"]["away"]["team"]["name"]

            homeScore = game["teams"]["home"]["score"]
            awayScore = game["teams"]["away"]["score"]

            gameStatus = game["status"]["detailedState"]

            gameScore = awayTeam + " @ " + homeTeam + " / " + str(awayScore) + "-" + str(homeScore) + " / " + gameStatus
            gameList.append(gameScore)
    return gameList

