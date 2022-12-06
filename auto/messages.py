import discord
from discord.ext import commands
import asyncio
import random
class Onmessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

                #we can also use if-elif-else ladders here
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content == "hi":
            await message.reply("Heaya,Greetings...\nNice To Meet You I Hope You'll Have A Good Time Here", delete_after=100)

            
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content == "i love you":
            await message.reply("```Your face, your body, your style, your beauty, your nature, your soul.....I think these are most powerful magnets on this earth that have attracted cold iron like me!``` \n **I LOVE YOU 3000 <3 ❤️**", delete_after=100)


async def setup(bot):
    await bot.add_cog(Onmessage(bot))

print("on message is loaded")