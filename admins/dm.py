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
                    embed=discord.Embed(title="Σ𝚡𝚌𝚎𝚌𝚞𝚝𝚒𝚘𝚗 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕", description="",color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/AFLSNpQpHVcAAAAi/my-melody.gif")
                    embed.add_field(name="𝙳𝚖 𝙷𝚊𝚟𝚎 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚝 𝚃𝚘", value=f'**{user.name}**', inline = True)
                    embed.set_footer(text="Created With ❤️ by Axy#0872")
                    await ctx.send(embed=embed)
            
            except:
                    embed=discord.Embed(title="Σ𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚎𝚍", description= "𝙵𝚊𝚒𝚕𝚎𝚍 𝚃𝚘 𝚂𝚎𝚗𝚝", color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/fzCt8ROqlngAAAAC/error-error404.gif")
                    embed.add_field(name= "Σ𝚛𝚛𝚘𝚛:-", value= f"**{user.name}** 𝙷𝚊𝚟𝚎 𝙳𝚖 𝙲𝚕𝚘𝚜𝚎𝚍!!", inline = False)
                    embed.set_footer(text="Created With ❤️ by Axy#0872")
                    await ctx.send(embed=embed)
            
                    
   
                
                
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dmall(self,ctx,*args):
        if args != None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.send(args)
                    embed=discord.Embed(title="Σ𝚡𝚌𝚎𝚌𝚞𝚝𝚒𝚘𝚗 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕", description="",color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/AFLSNpQpHVcAAAAi/my-melody.gif")
                    embed.add_field(name="𝙳𝚖 𝙷𝚊𝚟𝚎 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚂𝚎𝚗𝚝 𝚃𝚘", value=f'**{members}**', inline = True)
                    embed.set_footer(text="Created With ❤️ by Axy#0872")
                    await ctx.send(embed=embed)
                except:
                    embed=discord.Embed(title="Σ𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚎𝚍", description= "𝙵𝚊𝚒𝚕𝚎𝚍 𝚃𝚘 𝚂𝚎𝚗𝚝", color=discord.Colour.random())
                    embed.set_thumbnail(url="https://media.tenor.com/fzCt8ROqlngAAAAC/error-error404.gif")
                    embed.add_field(name= "List Of User Whom Dm Are Closed:-", value= f"**{members}** \n Specified Users Had 𝙳𝚖 𝙲𝚕𝚘𝚜𝚎𝚍!!", inline = True)
                    embed.set_footer(text="Created With ❤️ by Axy#0872")
                    await ctx.send(embed=embed)




async def setup(bot):
    await bot.add_cog(dm(bot))



print("dm is loaded")