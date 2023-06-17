import random
import nhl
import nba
import casino
import discord


def handle_response(message):
    msg = message.lower().split()
    if msg[0] == "hello":
        return 'hello bot'

    if msg[0] == "roll":
        rollOutcome = ""
        if len(msg) == 3:
            numDice = int(msg[1])
            numSide = int(msg[2])

            for roll in range(numDice):
                roll = random.randint(1, numSide)
                rollOutcome = rollOutcome + str(roll) + "/" + str(numSide) + " "
            rollOutcome = rollOutcome.strip()
        else:
            rollOutcome = str(random.randint(1,6)) + "/6"

        return rollOutcome

    if msg[0] == "nhl":
        if len(msg) == 3:
            if msg[1] == "standings":
                if msg[2] == "div":
                    embedMsg = discord.Embed(title="NHL", description="Here are the current NHL Standings by division", colour=0xc99fdf)
                    nhlDivStandings = nhl.view_standings_by_division()
                    atlanticTeams = ""
                    metroTeams = ""
                    centralTeams = ""
                    pacificTeams = ""
                    for teams in nhlDivStandings:
                        if teams.get("divName") == "Atlantic":
                            atlanticTeams = atlanticTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - "+ str(teams.get("teamInfo").get("points")) + "\n"
                        if teams.get("divName") == "Metropolitan":
                            metroTeams = metroTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - "+ str(teams.get("teamInfo").get("points")) + "\n"
                        if teams.get("divName") == "Central":
                            centralTeams = centralTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - "+ str(teams.get("teamInfo").get("points")) + "\n"
                        if teams.get("divName") == "Pacific":
                            pacificTeams = pacificTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - " + str(teams.get("teamInfo").get("points")) + "\n"
                    embedMsg.add_field(name="Atlantic Division", value=atlanticTeams, inline=True)
                    embedMsg.add_field(name="Metropolitan Division", value=metroTeams, inline=True)
                    embedMsg.add_field(name="Central Division", value=centralTeams, inline=True)
                    embedMsg.add_field(name="Pacific Division", value=pacificTeams, inline=True)
                    embedMsg.set_author(name="TuulerBot")
                if msg[2] == "conf":
                    embedMsg = discord.Embed(title="NHL", description="Here are the current NHL Standings by conference",
                                             colour=0xc99fdf)
                    nhlConfStandings = nhl.view_standings_by_conference()
                    easternTeams = ""
                    westernTeams = ""
                    for teams in nhlConfStandings:
                        if teams.get("confName") == "Eastern":
                            easternTeams = easternTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - " \
                                            + str(teams.get("teamInfo").get("points")) + "\n"
                        if teams.get("confName") == "Western":
                            westernTeams = westernTeams + teams.get("teamInfo").get("name") + " - " \
                                            + teams.get("teamInfo").get("record") + " - " \
                                            + str(teams.get("teamInfo").get("points")) + "\n"
                    embedMsg.add_field(name="Eastern Conference", value=easternTeams, inline=True)
                    embedMsg.add_field(name="Western Conference", value=westernTeams, inline=True)
                    embedMsg.set_author(name="TuulerBot")
                if msg[2] == "ovr":
                    embedMsg = discord.Embed(title="NHL", description="Here are the current overall NHL Standings",
                                             colour=0xc99fdf)
                    nhlStandings = nhl.view_standings_by_league()
                    nhlTeams = ""
                    for teams in nhlStandings:
                        nhlTeams = nhlTeams + teams.get("name") + " - " \
                                           + str(teams.get("points")) + "\n"
                    embedMsg.add_field(name="League Standings", value=nhlTeams, inline=True)
                    embedMsg.set_author(name="TuulerBot")
        elif len(msg) == 2:
            if msg[1] == "scores":
                embedMsg = discord.Embed(title="NHL", description="Here are the latest games scores", colour=0xc99fdf)
                nhlScores = nhl.view_current_scores()
                scoreString = ""
                for score in nhlScores:
                    scoreString = scoreString + score
                embedMsg.add_field(name="Today's Scores", value=scoreString, inline=True)
                embedMsg.set_author(name="TuulerBot")
            else:
                embedMsg = discord.Embed(title="NHL", description="To find information about what "
                                                                  "is going on around the league, type !nhl scores"
                                                                  ",!nhl standings div, !nhl standings conf or !nhl standings ovr. "
                                                                  "You can also click one of the buttons"
                                                                  "below.", colour=0xc99fdf)
                embedMsg.set_author(name="TuulerBot")
        else:
            embedMsg = discord.Embed(title="NHL", description="To find information about what "
                                                                  "is going on around the league, type !nhl scores"
                                                                  ",!nhl standings div, !nhl standings conf or !nhl standings ovr. "
                                                                  "You can also click one of the buttons"
                                                                  "below.", colour=0xc99fdf)
            embedMsg.set_author(name="TuulerBot")
        return embedMsg

    if msg[0] == "nba":
        if len(msg) == 3:
            if msg[1] == "standings":
                if msg[2] == "div":
                    embedMsg = discord.Embed(title="NBA", description="Here are the current NBA Standings By Division", colour=0xc99fdf)
                    nbaDivStandings = nba.getCurrentStandingsByDiv()
                    atlanticTeams = ""
                    centralTeams = ""
                    southeastTeams = ""
                    pacificTeams = ""
                    southwestTeams = ""
                    northwestTeams = ""
                    for teams in nbaDivStandings:
                        if teams.get("teamDiv") == "Atlantic":
                            atlanticTeams = atlanticTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                                + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                        if teams.get("teamDiv") == "Northwest":
                            northwestTeams = northwestTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                            + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                        if teams.get("teamDiv") == "Central":
                            centralTeams = centralTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                            + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                        if teams.get("teamDiv") == "Southwest":
                            southwestTeams = southwestTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                            + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                        if teams.get("teamDiv") == "Pacific":
                            pacificTeams = pacificTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                            + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                        if teams.get("teamDiv") == "Southeast":
                            southeastTeams = southeastTeams + teams.get("teamDivRank") + ". " + teams.get("teamName") \
                                            + " - " + teams.get("teamRecord") + " - " + teams.get("teamWinPCT") + "\n"
                    embedMsg.add_field(name="Atlantic Division", value=atlanticTeams, inline=True)
                    embedMsg.add_field(name="Central Division", value=centralTeams, inline=True)
                    embedMsg.add_field(name="Southeast Division", value=southeastTeams, inline=True)
                    embedMsg.add_field(name="Northwest Division", value=northwestTeams, inline=True)
                    embedMsg.add_field(name="Pacific Division", value=pacificTeams, inline=True)
                    embedMsg.add_field(name="Southwest Division", value=southwestTeams, inline=True)
                    embedMsg.set_author(name="TuulerBot")
                elif msg[2] == "conf":
                    embedMsg = discord.Embed(title="NBA", description="Here are the current NBA Standings by conference",
                                             colour=0xc99fdf)
                    nbaConfStandings = nba.getCurrentStandingsByConf()
                    easternTeams = []
                    easternTeamString = ""
                    westernTeams = []
                    westernTeamString = ""
                    for teams in nbaConfStandings:
                        if teams.get("teamConf") == "East":
                            easternTeams.append(teams)
                        if teams.get("teamConf") == "West":
                            westernTeams.append(teams)
                    for x in easternTeams:
                        easternTeamString = easternTeamString + x.get("teamConfRank") + ". " + x.get("teamName") \
                                            + " - " + x.get("teamRecord") + " - " + x.get("teamWinPCT") + "\n"
                    for x in westernTeams:
                        westernTeamString = westernTeamString + x.get("teamConfRank") + ". " + x.get("teamName") \
                                            + " - " + x.get("teamRecord") + " - " + x.get("teamWinPCT") + "\n"
                    embedMsg.add_field(name="Eastern Conference", value=easternTeamString, inline=True)
                    embedMsg.add_field(name="Western Conference", value=westernTeamString, inline=True)
                    embedMsg.set_author(name="TuulerBot")
                else:
                    embedMsg = discord.Embed(title="NBA", description="To find information about what "
                                                                      "is going on around the league, type !nba scores"
                                                                      "or !nba standings. You can also click one of the buttons"
                                                                      "below.", colour=0xc99fdf)
                    embedMsg.set_author(name="TuulerBot")
        elif len(msg) == 2:
            if msg[1] == "scores":
                embedMsg = discord.Embed(title="NBA", description="Here are the latest games scores", colour=0xc99fdf)
                scoreString = ""
                nbaScores = nba.getCurrentGames()
                for score in nbaScores:
                    scoreString = scoreString + score
                embedMsg.add_field(name="Today's Scores", value=scoreString, inline=True)
                embedMsg.set_author(name="TuulerBot")
            else:
                embedMsg = discord.Embed(title="NBA", description="To find information about what "
                                                              "is going on around the league, type !nba scores"
                                                              "or !nba standings div or !nba standings conf. You can also click one of the buttons"
                                                              "below.", colour=0xc99fdf)
                embedMsg.set_author(name="TuulerBot")
        else:
            embedMsg = discord.Embed(title="NBA", description="To find information about what "
                                                              "is going on around the league, type !nba scores"
                                                              "or !nba standings div or !nba standings conf. You can also click one of the buttons"
                                                              "below.", colour=0xc99fdf)
            embedMsg.set_author(name="TuulerBot")
        return embedMsg

    if msg[0] == "casino":
        pass