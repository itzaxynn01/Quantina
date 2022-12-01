import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from datetime import datetime

class GeneralCommands(commands.Cog, name='GeneralCommands'):

    def __init__(self,bot):
        self.bot = bot

    
    #greet command -- status -- Done
    @commands.command()
    async def servertour(self,ctx):
        embed=discord.Embed(title=f"𝙶𝚛𝚎𝚎𝚝𝚒𝚗𝚐𝚜,𝙼𝚛." + ctx.author.mention , description=f"𝙷𝚒,__{ctx.author.name}__ !! 𝚃𝚑𝚊𝚗𝚔 𝚈𝚘𝚞 𝙵𝚘𝚛 𝙹𝚘𝚒𝚗𝚒𝚗𝚐 𝙾𝚞𝚛 𝚂𝚎𝚛𝚟𝚎𝚛,𝙷𝚘𝚙𝚎 𝚈𝚘𝚞'𝚛𝚎 𝙷𝚊𝚟𝚒𝚗𝚐 𝙰 𝙶𝚘𝚘𝚍 𝚃𝚒𝚖𝚎 𝚆𝚒𝚝𝚑 𝚄𝚜" "😊", color=discord.Colour.random())
        embed.set_thumbnail(url=f"https://media.tenor.com/NqKn2UhXzU0AAAAi/get-greeting-say-hi.gif{ctx.author.mention}")
        embed.add_field(name="𝚃𝚘 𝙵𝚒𝚗𝚍 𝙵𝚛𝚎𝚒𝚗𝚍𝚜 𝚈𝚘𝚞 𝙲𝚊𝚗 𝙴𝚡𝚙𝚕𝚘𝚛𝚎 :-" , value="``` #Testing ``` \n <#990552288701587466>" , inline = True)
        embed.add_field(name="𝚃𝚘 𝙰𝚜𝚜𝚒𝚐𝚗 𝚈𝚘𝚞𝚛 𝚂𝚎𝚕𝚏 𝚁𝚘𝚕𝚎 𝙺𝚒𝚗𝚍𝚕𝚢 𝙶𝚘 𝚃𝚘 :-" , value="``` #self-role ```\n <#1040957030774616084>", inline = False)
        embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
        await ctx.send(embed=embed)
    
    #countdown command
    @commands.command()
    async def countdown(self,ctx, seconds):
        try: 
            secondint = int(seconds)
            if secondint > 300:
                embed=discord.Embed(title="𝙸𝚗𝚟𝚊𝚕𝚒𝚍 - 𝙸𝚗𝚜𝚒𝚜𝚝𝚎𝚗𝚌𝚎" , description="⚠️𝐀𝐝𝐦𝐢𝐧𝐏𝐞𝐫𝐦𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝⚠️ \n-> 𝘖𝘯𝘭𝘺 𝘉𝘰𝘵 𝘈𝘥𝘮𝘪𝘯𝘴 𝘊𝘢𝘯 𝘎𝘰 𝘖𝘷𝘦𝘳 300 𝘚𝘦𝘤𝘰𝘯𝘥𝘴", color=discord.Colour.random())
                embed.set_thumbnail(url="https://media.tenor.com/swTDQJ85dDEAAAAC/aaaa.gif")
                embed.add_field(name="```---------------------------```" , value=" -> 𝘗𝘭𝘦𝘢𝘴𝘦 𝘌𝘯𝘵𝘦𝘳 𝘈 𝘝𝘢𝘭𝘶𝘦 𝘞𝘩𝘪𝘤𝘩 𝘐𝘴 𝘓𝘦𝘴𝘴 𝘛𝘩𝘢𝘯 300 𝘚𝘦𝘤𝘰𝘯𝘥𝘴 ", inline = True)
                embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                await ctx.send(embed=embed)
                raise BaseException
            if secondint <=0:
                embed=discord.Embed(title="𝙸𝚗𝚟𝚊𝚕𝚒𝚍 - 𝙸𝚗𝚜𝚒𝚜𝚝𝚎𝚗𝚌𝚎" , description="-> 𝚈𝚘𝚞 𝙲𝚊𝚗 𝙾𝚗𝚕𝚢 𝚃𝚊𝚔𝚎 𝚁𝚎𝚊𝚕𝙽𝚞𝚖", color=discord.Colour.random())
                embed.set_thumbnail(url="https://media.tenor.com/iROp8uu-48IAAAAj/bloodbros-error.gif")
                embed.add_field(name="𝙳𝚛𝚊𝚠𝚋𝚊𝚌𝚔-𝙾𝚛𝚒𝚐𝚒𝚗", value = "-> 𝘞𝘩𝘰𝘭𝘦𝘕𝘶𝘮 𝘈𝘯𝘥 𝘐𝘯𝘵𝘦𝘨𝘦𝘳𝘴 𝘈𝘳𝘦 𝘗𝘳𝘰𝘩𝘪𝘣𝘪𝘵𝘦𝘥 𝘛𝘰 𝘜𝘴𝘦 \n 𝘪.𝘦 ->0,-1,-2 𝘌𝘵𝘤 " , inline = False)
                embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                await ctx.send(embed=embed)
                raise BaseException
        
            message = await ctx.send(f"𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗: {seconds}")
            embed=discord.Embed(title="𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗", description=f"{ctx.author.mention},𝚈𝚘𝚞𝚛 𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗 𝙷𝚊𝚜 𝙱𝚎𝚎𝚗 𝚂𝚝𝚊𝚛𝚝𝚎𝚍", color=discord.Colour.random())
            embed.set_thumbnail(url="https://media.tenor.com/5DMUa8nHcLYAAAAi/smartparcel-stop-watch.gif")
            embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
            await ctx.send(embed=embed)

            while True:
                secondint -= 1
                if secondint == 3:               
                    embed=discord.Embed(title="𝚃𝚒𝚌𝚔-𝚃𝚘𝚌𝚔", description= "3", color=discord.Colour.random())
                    embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                    await ctx.send(embed=embed)
                    
                if secondint == 2:
                    embed=discord.Embed(title="𝙸𝚝𝚜 𝙶𝚎𝚝𝚝𝚒𝚗𝚐 𝙲𝚕𝚘𝚜𝚎", description= "2", color=discord.Colour.random())
                    embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                    await ctx.send(embed=embed)
                if secondint == 1:          
                    embed=discord.Embed(title="T̷i̷m̷e̷ ̷O̷v̷e̷r̷", description= "1", color=discord.Colour.random())
                    embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
                    await ctx.send(embed=embed)
                if secondint == 0:
                    await message.edit(content=f"**Σ𝚗𝚍𝚎𝚍! 𝙰𝚝** :-```{datetime.utcnow()}```")
                    break

                await message.edit(content=f"**𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗:** __{secondint}__")
                
            
                await asyncio.sleep(1)
            
            embed=discord.Embed(title="𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗 𝙾𝚟𝚎𝚛", description= "𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗 𝙸𝚜 𝙾𝚟𝚎𝚛 𝙽𝚘𝚠,\n𝚃𝚘 𝙼𝚊𝚔𝚎 𝙰𝚗𝚘𝚝𝚑𝚎𝚛 𝙲𝚘𝚞𝚗𝚝𝙳𝚘𝚠𝚗 𝙴𝚟𝚎𝚗𝚝\n𝙺𝚒𝚗𝚍𝚕𝚢 𝚄𝚜𝚎 𝙲𝚘𝚖𝚖𝚊𝚗𝚍:-\n```!countdown <seconds>```", color=discord.Colour.random())
            embed.set_thumbnail(url="https://media.tenor.com/TblsP308FpgAAAAi/anayaka-defjam.gif")
            embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
            await ctx.send(embed=embed)
        
                
        except ValueError:
             embed=discord.Embed(title="𝙴𝚛𝚛𝚘𝚛 𝙾𝚌𝚌𝚞𝚛𝚎𝚍" , description="𝚈𝚘𝚞 𝙽𝚎𝚎𝚍 𝚃𝚘 𝙼𝚎𝚗𝚝𝚒𝚘𝚗 𝙰 𝚅𝚊𝚕𝚒𝚍 𝙽𝚞𝚖𝚋𝚎𝚛 𝙵𝚘𝚛 𝙲𝚘𝚞𝚗𝚝𝚍𝚘𝚠𝚗", color=discord.Colour.random())
             embed.set_thumbnail(url=f"https://media.tenor.com/p36E4Uwq7BUAAAAM/error.gif")
             embed.add_field(name=f"{ctx.author.mention}", value="YOᑌ ᕼᗩᐯE EᑎTEᖇEᗪ ᗩ ᗯᖇOᑎG ᐯᗩᒪᑌE!" , inline = True)
             embed.set_footer(text="Created With ❤️ by DevOPS_i-AxYnn#0023")
             await ctx.send(embed=embed)
       

        


async def setup(bot):
    await bot.add_cog(GeneralCommands(bot))



print("General Commands is loaded")