import discord
from discord.ext import commands

from datetime import datetime


class Mod(commands.Cog, name='Moderation'):

    def __init__(self, bot):
        self.bot = bot
# clear command

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount+1)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("please specify the ammount of messages")
            await ctx.message.delete()

    # kick commands

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} was successfully kicked for {reason}')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```please mention a user to kick.!!! or maybe you are missing reasons```')

    # ban command

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'{member.name} was successfully banned for \n given reason:-{reason}')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('```please mention a user to ban.!!! or maybe you are missing reasons```')
    

async def setup(bot: commands.Bot):
    await bot.add_cog(Mod(bot))

print("Moderation.py Is Loaded Successfully")