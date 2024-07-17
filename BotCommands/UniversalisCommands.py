import requests
from config import *
from discord.ext import commands
from Src.Recipes import *

class Universalis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='CostOf:', help='Show cost of a specific item.')
    async def CostOf(self, ctx, name, hq="", home_server="Chaos" ):

        try:
            id = getId(name, DATAID)
            if not id:
                raise ItemNotFoundError(f" '{name}' doesn't seem to exist.")
        except ItemNotFoundError as e:
            print(e)
            await ctx.send(f"I'm sorry,{e}")
            return

        if hq not in ["False", "True", ""] or home_server not in Config.SERVERLIST:
            await ctx.send("Hq argument should be : True, False or left blank not : ", hq, "\n ===== \n Function arguments are : name, hq, server \n Command Example : $CostOf: 'Soupe de légumes' True Chaos")
            return

        if len(hq)>0 and hq !=" " :
            resultReq = requests.get("https://universalis.app/api/v2/" + str(home_server) + "/" + str(getId(name,DATAID)+"?listings="+Config.get_listing())+"&hq="+hq).json()["listings"] 
        else:
            resultReq = requests.get("https://universalis.app/api/v2/" + str(home_server) + "/" + str(getId(name,DATAID)+"?listings="+Config.get_listing())).json()["listings"] 
        msg = "==== Listing all items Found ====" + '\n'

        for item in resultReq:
            msg += '\n' + "World : "+ item["worldName"] + '\n' + "Price Per Unit : " + str(item["pricePerUnit"]) + '\n' + "Quantity : " + str(item["quantity"]) + '\n' + "Hq : " + str(item["hq"]) + '\n' + "Total without taxes : "+ str(item["total"]) + '\n' + "Total with taxes : " + str(item["total"] +item["tax"]) +  '\n'

        await ctx.send(msg)

async def setup(bot):
   await bot.add_cog(Universalis(bot))
