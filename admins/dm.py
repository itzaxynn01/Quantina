import discord
from discord.ext import commands
from discord.utils import get
import asyncio

class dm(commands.Cog, name='dm'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dm(self,ctx,user: discord.Member,*,args):

        if args != None:
            try:
                    await user.send(args)
                    embed=discord.Embed(title="Ξ£π‘ππππππππ πππππππππππ", description="",color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/AFLSNpQpHVcAAAAi/my-melody.gif")
                    embed.add_field(name="π³π π·πππ ππππππππππππ’ ππππ ππ", value=f'**{user.name}**', inline = True)
                    embed.set_footer(text="Created With β€οΈ by Axy#0872")
                    await ctx.send(embed=embed)
            
            except:
                    embed=discord.Embed(title="Ξ£ππππ πΎππππππ", description= "π΅πππππ ππ ππππ", color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/fzCt8ROqlngAAAAC/error-error404.gif")
                    embed.add_field(name= "Ξ£ππππ:-", value= f"**{user.name}** π·πππ π³π π²πππππ!!", inline = False)
                    embed.set_footer(text="Created With β€οΈ by Axy#0872")
                    await ctx.send(embed=embed)
            
                    
   
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dmall(self,ctx,*args):
        if args != None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                    embed=discord.Embed(title="Ξ£π‘ππππππππ πππππππππππ", description="",color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/AFLSNpQpHVcAAAAi/my-melody.gif")
                    embed.add_field(name="π³π π·πππ ππππππππππππ’ ππππ ππ", value=f'**{members}**', inline = True)
                    embed.set_footer(text="Created With β€οΈ by Axy#0872")
                    await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title="Ξ£ππππ πΎππππππ", description= "π΅πππππ ππ ππππ", color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/fzCt8ROqlngAAAAC/error-error404.gif")
                    embed.add_field(name= "List Of User Whom Dm Are Closed:-", value= f"**{members}** \n Specified Users Had π³π π²πππππ!!", inline = True)
                    embed.set_footer(text="Created With β€οΈ by Axy#0872")
                    await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(dm(bot))



print("dm is loaded")