import discord
from discord.ext import commands, tasks
import os
from image_handler import get_next_image, move_to_posted
from git_tools import git_commit_and_push_if_needed

TOKEN = "Photo-Bot"
CHANNEL_ID = 1394686219769745568  # Deine Channel-ID

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")
    daily_post.start()

@tasks.loop(hours=24)
async def daily_post():
    channel = bot.get_channel(CHANNEL_ID)
    image_path = get_next_image()
    if image_path:
        await channel.send(file=discord.File(image_path))
        move_to_posted(image_path)
        git_commit_and_push_if_needed(f"Bild automatisch gepostet: {os.path.basename(image_path)}")

@bot.command()
async def post_now(ctx):
    image_path = get_next_image()
    if image_path:
        await ctx.send(file=discord.File(image_path))
        move_to_posted(image_path)
        git_commit_and_push_if_needed(f"Manuell gepostet: {os.path.basename(image_path)}")
    else:
        await ctx.send("Kein Bild verfügbar.")

@bot.command()
async def moveimage(ctx, filename: str):
    source_path = os.path.join("images/to_post", filename)
    if os.path.exists(source_path):
        move_to_posted(source_path)
        git_commit_and_push_if_needed(f"Manuell verschoben: {filename}")
        await ctx.send(f"{filename} wurde verschoben.")
    else:
        await ctx.send("Datei nicht gefunden.")

bot.run(TOKEN)
