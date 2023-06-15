import random
import nhl
import nba
import casino
import discord


def handle_response(message) -> str:
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
        if len(msg) >= 2:
            if msg[1] == "standings":
                if msg[2] == "div":
                    embedMsg = discord.Embed(title="NHL", description="Here are the current NHL Standings", colour=0xc99fdf)
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
                    embedMsg = discord.Embed(title="NHL", description="Here are the current NHL Standings",
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
                    embedMsg = discord.Embed(title="NHL", description="Here are the current NHL Standings",
                                             colour=0xc99fdf)
                    nhlStandings = nhl.view_standings_by_league()
                    nhlTeams = ""
                    for teams in nhlStandings:
                        nhlTeams = nhlTeams + teams.get("name") + " - " \
                                           + str(teams.get("points")) + "\n"
                    embedMsg.add_field(name="League Standings", value=nhlTeams, inline=True)
                    embedMsg.set_author(name="TuulerBot")
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
                                                              "is going on around the league, type !nhl stats, !nhl scores"
                                                              "and !nhl standings. You can also click one of the buttons"
                                                              "below.", colour=0xc99fdf)
            embedMsg.set_author(name="TuulerBot")
        return embedMsg

    if msg[0] == "nba":
        pass

    if msg[0] == "casino":
        pass