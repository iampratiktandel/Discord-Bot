import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Bot is ready.')

client.run('NzMwNDIxOTAwMDI2NzA4MDA5.XwXVzQ.C9Ja0MsLNZiZp8dE2pe6z1HN-Ww')