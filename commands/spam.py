import discord
from discord.ext import commands
from discord.utils import get
import asyncio


class spam(commands.Cog, name='spam'):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def spam(self,ctx, seconds):
        try:
            secondint = int(seconds)
            if secondint > 300:
                embed=discord.Embed(title="Error" , description="you need to mention number for timer-spam", color=discord.Colour.random())
                await ctx.send(" i dont think i can go over 300 seconds")
                raise BaseException
            if secondint <=0:
                embed=discord.Embed(title="0" , description="you need to mention number for timer-spam", color=discord.Colour.random())
                await ctx.send(embed=embed)
                raise BaseException
        
            message = await ctx.send(f"spam: {seconds}")

            while True:
                secondint -= 1
                if secondint == 0:
                    await message.edit(content="ended!")
                    break

                await message.edit(content=f"spam: {secondint}")
                await asyncio.sleep(0.1)
                embed=discord.Embed(title="gg", description=f"{ctx.author.mention},your spam has been ended", color=discord.Colour.random())
                embed.set_thumbnail(url=None)
                embed.add_field(name= None, value= None, inline = True)
                embed.add_field(name=None , value=None , inline = False)
                embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                await ctx.send(embed=embed)
            
        except ValueError:
             embed=discord.Embed(title="Error" , description="you need to mention number for spam-spam", color=discord.Colour.random())
             embed.set_thumbnail(url=f"https://media.tenor.com/p36E4Uwq7BUAAAAM/error.gif")
             embed.add_field(name=f"{ctx.author.mention}", value="You Have Entered A Wrong Value" , inline = True)
             embed.add_field(name="this is field 1" , value="this field  inline False" , inline = False)
             embed.set_footer(text="Error Exception Footer")

        
        await ctx.send(embed=embed)






async def setup(bot):
    await bot.add_cog(spam(bot))



print("Spam is loaded")