import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import logging
from game import DiceGame, Welcomer
import data

client = commands.Bot(command_prefix='!')
game = None
welcomes = Welcomer

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def newgame(ctx):
   global game, welcomes
   if game == None:
      game = DiceGame(str(ctx.author))
      welcomes = Welcomer()
      await ctx.send("```Started a new game of dice!\nUse !join to join game and !roll to roll```")
   else:
      await ctx.send("```Game already in progress!\nUse !roll to roll dice```")

@client.command()
async def roll(ctx):
   global game
   if game != None:
      if game.playerInGame(str(ctx.author)):
         result = game.rollDice(str(ctx.author))
         fmt = "```{} rolled {} ``` \n"
         print(result)
         await ctx.send(fmt.format(str(ctx.author), str(result[1])))
      else:
         await ctx.send(str(ctx.author)+" you need to join before rolling!")
   else:
      await ctx.send("Could not find active game")

@client.command()
async def join(ctx):
   global game, welcomes
   player = str(ctx.author)
   otp = str(welcomes.getRandomWelcomer())
   print(otp)
   if game != None and game.playerInGame(player) == False and game.join(player):
         await ctx.send("```"+otp.format(player)+"```")
   else:
      errormsg  = "```{} you are already in game or game has not been started yet!```"
      await ctx.send(errormsg.format(player))
     
@client.command()
async def players(ctx):
   global game
   await ctx.send(game.players)

@client.command()
async def score(ctx):
   global game
   await ctx.send(game.getCurrentScore())

@client.command()
async def close(ctx):
   global game
   await ctx.send("```Closing game of dice!```\n"+game.getCurrentScore())
   game = None

@client.command()
async def pokemon(ctx, arg):
   await ctx.send(data.getPokemon(arg))

def main():
    logging.basicConfig(level=logging.INFO)
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    client.run(TOKEN)
  

if __name__ == "__main__":
    main()
