import os
import discord
from discord.ext import commands

# Nur lokal .env laden
if os.environ.get("RENDER") != "true":
    from dotenv import load_dotenv
    load_dotenv()

# Token aus Umgebungsvariable
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

# Optional: Webserver starten (für Render)
try:
    from keep_alive import keep_alive
    keep_alive()
except:
    pass  # Falls lokal getestet wird ohne keep_alive.py

# Bot starten
bot.run(TOKEN)
