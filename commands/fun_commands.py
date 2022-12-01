import discord
from discord.ext import commands
from discord.utils import get

class fun(commands.Cog, name='fun'):

    def __init__(self,bot):
        self.bot = bot
    # say command
    @commands.command()
    
    async def say(self,ctx, *, question):
        await ctx.message.delete()
        await ctx.send(f'{question}')

    @commands.command()
    async def avatar(self, ctx, *, user : discord.Member=None):
        if user is None:
            user = ctx.message.author
        embed = discord.Embed()
        embed.add_field(name=user.name,value=f'[Downlaod]({user.avatar.url})')
        embed.set_image(url=user.avatar.url)
        embed.set_footer(text=f"Requested By {ctx.author.name}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=embed)
        
    @commands.command()
    async def guild_icon(self, ctx):
        embed = discord.Embed()
        embed.set_image(url=ctx.guild.icon.url)
        await ctx.send(embed=embed)
        



async def setup(bot):
    await bot.add_cog(fun(bot))



print("fun_commands is loaded")



