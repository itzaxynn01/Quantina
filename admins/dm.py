import discord
from discord.ext import commands
from discord.utils import get

class dm(commands.Cog, name='dm'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self,ctx,user: discord.Member,*,args):
        if args != None:
            try:
                await user.send(args)
                await ctx.send(f'Dm sent to {user.name}')
            except:
                await ctx.send('user has his dm clossed')
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dmall(self,ctx,*args):
        if args != None:
            members = ctx.guild.members

            for member in members:
                try:
                    await member.send(args)
                    await ctx.send(f'dm sent to {member.name}')
                except:
                    await ctx.send(f'{member.name} has his dms closed!')


async def setup(bot):
    await bot.add_cog(dm(bot))



print("dm is loaded")