__author__ = "Charles Petchsy"

__license__ = "MIT"
__maintainer__ = "Charles Petchsy"
__status__ = "Alpha"

import requests
import json
import ast
import discord

from discord.ext import commands
from html.parser import HTMLParser

class Lifetime(HTMLParser):
    """ Parse requirements:
    Each entry will include the rank percentile of the player.
    PvP Kills
    NPC Kills
    Skill Kills
    Headshots
    Items Looted
    E-Credit Balance
    Commendations
    Curr Comm. Score
    Sharpshooter Kills
    Survivalist Kills
    Demolitionist Kills
    """
    def handle_data(self, data):
        if 'window.__INITIAL_STATE__' in data:
            player_data = json.loads(
                ast.literal_eval(
                    repr(data.split(';')[0].split('=')[1])
                    )
                )
            # Get player data
            print(player_data['stats'])

client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    activity = discord.Game(name="")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == "!test":
        await message.channel.send("I'm alive.")

bot = commands.Bot(command_prefix='!')

@bot.command()
async def div2(ctx, arg):
    await ctx.channel.send(arg)

if __name__ == '__main__':
    # Add commands and run with token here
    # bot.run('')
    # client.run('')

    r = requests.get('https://division.tracker.gg/division-2/profile/uplay/Softbunn/overview')
    # print(r.content)

    # instantiate the parser and fed it some HTML
    parser = Lifetime()
    parser.feed(str(r.content))
