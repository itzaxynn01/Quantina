import discord
from discord.ext import commands
import asyncio

class Onmessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

                #we can also use if-elif-else ladders here
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "ok" or message.content == "hih":
            await message.reply("hi", delete_after=300)
            
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content == "gg":
            await message.reply("This is a message", delete_after=10)


async def setup(bot):
    await bot.add_cog(Onmessage(bot))

print("on message is loaded")