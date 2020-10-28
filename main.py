import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import logging
import jokes

logging.basicConfig(level=logging.INFO)
client = commands.Bot(command_prefix='!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def joke(ctx):
    await ctx.send(jokes.getJoke())


client.run(TOKEN)
