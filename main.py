import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta

intents = discord.Intents.default()
intents.presences = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

start_time = datetime.utcnow()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    update_status.start()

@tasks.loop(seconds=5)  # Update status every 5 seconds (2.5 seconds for each status)
async def update_status():

    uptime = datetime.utcnow() - start_time

    
    days, remainder = divmod(uptime.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_uptime = f"{int(days)}d {int(hours)}h {int(minutes)}m" if days >= 1 else f"{int(hours)}h {int(minutes)}m"

   
    if update_status.current_loop % 2 == 0:
        await bot.change_presence(activity=discord.Game(name="Visual Studio Code"))
    else:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Uptime: {formatted_uptime}"))


bot.run("TOKEN")
