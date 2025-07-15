import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import webserver

# .env-Datei laden
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents konfigurieren
intents = discord.Intents.default()
intents.message_content = True

# Bot initialisieren
bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Wenn der Bot bereit ist
@bot.event
async def on_ready():
    print(f"✅ Bot ist online als {bot.user}")

# Beispiel-Befehl
@bot.command()
async def hallo(ctx):
    await ctx.send("Hallo! 👋")

webserver.keep_alive()
bot.run(TOKEN)
