import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "c-")
bot.load_extension("jishaku")

@bot.event
async def on_ready():
	print("Ready as", bot.user)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)