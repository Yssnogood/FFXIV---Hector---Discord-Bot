from discord.ext import commands
from Src.Recipes import *
from config import Config

class Configs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='SetLanguage:', help='Set on which language items should be printed.')
    async def SetLANG(self, ctx, lang):
        if lang in Config.LANGAVAILABLE:
            print("Language was changed from " + Config.get_lang() + "to " + lang)
            Config.set_lang(lang)
            await ctx.send("Language changed to : " + Config.get_lang())
        else:
            await ctx.send("Please choose one of theses available langages : "+ [ x + "," for x in Config.LANGAVAILABLE])

    @commands.command(name='CurrentLanguage', help='Show current language selected.')
    async def CurrentLANG(self, ctx):
        await ctx.send("Language currently in use : " + Config.get_lang())

    @commands.command(name='ChangeListing', help='Change number of items that should be display on the "CostOf:" command.')
    async def SetListing(self, ctx, howMany):

        if howMany.isdigit():
            if int(howMany)>=1 and int(howMany)<=10:
                Config.set_listing(int(howMany))
                await ctx.send("New listing set to : " + Config.get_listing())
        else:
            print("Type of how Many : ",type(howMany), howMany)
            await ctx.send("Please write a number. It must be between 1 and 10")

    @commands.command(name="ApiInfo", help="Show Api used for this project")
    async def ApiInfo(self, ctx):
        await ctx.send("Api used from Universalils : https://docs.universalis.app \n && from SaddleBag : https://github.com/ff14-advanced-market-search/saddlebag-with-pockets/wiki#ffxiv-alert-guides")
            
async def setup(bot):
    await bot.add_cog(Configs(bot))
