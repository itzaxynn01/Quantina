import discord
from discord.ext import commands
from discord.utils import get

class Welcome(commands.Cog, name='Welcomer'):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        role = discord.utils.get(member.guild.roles , name = 'Welcome role')
        channel = self.bot.get_channel(1041765613464461382)
        embed = discord.Embed(description=f'HI {member.mention} , Welcome to the guild!' , color=+0x0bf9f9)
        await member.add_roles(role)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(1041765613464461382)
        embed = discord.Embed(description=f"{member.mention , member.name} just left the guild")
        await channel.send(embed=embed)

    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'latency is {round(self.bot.latency * 1000)}ms')



async def setup(bot):
    await bot.add_cog(Welcome(bot))



print("welcome is loaded")