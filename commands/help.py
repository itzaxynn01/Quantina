import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self,ctx):
        embed=discord.Embed(title= "Here To Help You", description= "Developing", color=discord.Colour.random())
        embed.set_thumbnail(url="https://media.tenor.com/-CNuxf82_SUAAAAi/janssenmorethanblue-morethanblue.gif")
        embed.add_field(name="Commands :-" , value="on making\n <#990552288701587466>" , inline = True)
        embed.add_field(name="Contribution:-" , value="on construction", inline = False)
        embed.set_footer(text="Created With ❤️ by Axy")
        await ctx.send(embed=embed)


async def setup(bot:commands.Bot):
    await bot.add_cog(help(bot))


print("help is loaded ")