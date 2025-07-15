import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Wichtig für das Lesen von Nachrichten

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user}')

@bot.command()
async def hallo(ctx):
    await ctx.send("Hallo")

bot.run('DEIN_BOT_TOKEN_HIER')
