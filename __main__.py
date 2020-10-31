import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import logging
import jokes

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.command()
async def joke(ctx):
    await ctx.send(jokes.getJoke())

def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)
  

if __name__ == "__main__":
    main()
