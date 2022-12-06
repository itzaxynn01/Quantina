import discord
from discord.ext import commands


class Announcement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        pass
    

async def setup(bot):
    await bot.add_cog(Announcement(bot))
