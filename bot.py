import discord
import response
import json

async def send_msg(msg, userMsg, embed):
    try:
        reply = response.handle_response(userMsg)
        if not embed:
            await msg.channel.send(reply)
        else:
            await msg.channel.send(embed=reply)

    except Exception as e:
        print("Error: "+ e.with_traceback())


def run_bot():
    jsonFile = open('BOT_INFO.json', "r")
    jsonData = json.loads(jsonFile.read())
    TOKEN = jsonData["TOKEN"]

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Good Morning {client.user}, the bot is now running.')

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            # no infinite loop on own message
            return

        userMsg = str(msg.content)

        if userMsg[0] == '!':
            userMsg = userMsg[1:]   # remove ! from message
            if "purge" in userMsg:
                await msg.channel.purge(limit=int(userMsg.split()[1]))
            elif "nhl" in userMsg or "nba" in userMsg or "casino" in userMsg:
                await send_msg(msg, userMsg, embed=True)
            else:
                await send_msg(msg, userMsg, embed=False)





    client.run(TOKEN)