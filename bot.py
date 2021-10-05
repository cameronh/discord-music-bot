import discord
from discord import voice_client
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
from music import Music

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents().default()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), description='Discord.py music bot', intents=intents)

if __name__ == "__main__":
  bot.add_cog(Music(bot))
  bot.run(DISCORD_TOKEN)