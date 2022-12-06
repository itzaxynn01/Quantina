import discord
from discord.ext import commands
import json
import asyncio
from asyncio import sleep as s
from datetime import datetime
import keep_alive
# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]

bot = commands.Bot(prefix, intents = discord.Intents.all())
#bot.remove_command("help") after help setup uncomment krdenge
# Load cogs
extensions = [
    "commands.general_commands",
    "auto.messages",
    "commands.moderation",
    "commands.fun_commands",
    "commands.help",
    "admins.dm",
    "auto.welcome",
    "commands.spam",
    "commands.specialcommands",
    "commands.basiccommands",
]

print(extensions)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
    print(discord.__version__)

    if __name__ == '__main__':
        for extension in extensions:
            try:
                await asyncio.sleep(0.1)
                await bot.load_extension(extension)
                await asyncio.sleep(0.11)
            except Exception as e:
                await asyncio.sleep(0.111)
                print(f"Failed to load extension {extension}")
                await asyncio.sleep(0.111)


@bot.command()
@commands.has_permissions(administrator=True)
async def runtime(ctx):
    now = datetime.utcnow()
    elapsed = now - starttime
    seconds = elapsed.seconds
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    await ctx.send("Running For {}d {}h {}m {}s".format(elapsed.days, hours, minutes, seconds))
starttime = datetime.utcnow()
#reminder command
@bot.command()
async def reminder(ctx,time:int,*,msg):
    while True:
        await s(time)
        await ctx.send(f'{msg} {ctx.author.mention}')
    


#keep_alive.keep_alive()
#running the bot through config.json
bot.run(token)