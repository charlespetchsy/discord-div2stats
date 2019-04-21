import discord
from discord.ext import commands

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

# bot = commands.Bot(command_prefix='$')

# @bot.command()
# async def test(ctx, arg):
#     await ctx.channel.send(arg)

# # Add commands and run with token here
# bot.run('')
client.run('')