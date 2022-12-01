import discord
from discord.ext import commands


class admincommands(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


@commands.command()
@commands.has_permissions(administrator=True)



async def setup(bot:commands.Bot):
    await bot.add_cog(admincommands(bot))