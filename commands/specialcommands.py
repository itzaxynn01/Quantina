import discord
from discord.ext import commands
from discord.utils import get


class Specialcommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(1046890449912205452)
    async def modme(self,member):
        role = discord.utils.get(member.guild.roles , name = 'hh')
        channel = self.bot.get_channel(1046890501321805834)
        embed = discord.Embed(description=f'HI {member.mention} , Welcome to the guild!' , color=+0x0bf9f9)
        await member.add_roles(role)
        await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Specialcommands(bot))


print("special commands is loaded")
