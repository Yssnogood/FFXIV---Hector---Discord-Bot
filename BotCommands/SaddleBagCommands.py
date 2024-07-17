import requests

from discord.ext import commands
from Src.Item import *
from Src.Recipes import *
from config import Config

class SaddleBag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ListCost:')
    async def ListCost(self, ctx, name, craft_amount=1, hq=False, home_server="Moogle", job=0):

        try:
            id = getId(name, DATAID)
            if not id:
                raise ItemNotFoundError(f" '{name}' doesn't seem to exist.")
        except ItemNotFoundError as e:
            print(e)
            await ctx.send(f"I'm sorry,{e}")
            return

        self.item= Item(int(id), name, craft_amount, hq, home_server,job )
        await ctx.send("Please wait while I'm fetching data.")
        self.itemShoppingListRequest = requests.post("http://api.saddlebagexchange.com/api/v2/shoppinglist", json=self.item.details)
        self.itemShoppingList = self.itemShoppingListRequest.json()["data"]
        self.itemShoppingListTotalCost = self.itemShoppingListRequest.json()["total_cost"]
        self.itemShoppingListAverageCost = self.itemShoppingListRequest.json()["average_cost_per_craft"]

        msg = "===== Listing minimun Price Per Unit Mats needed =====" + '\n'+ '\n'

        self.itemWithout = [{"total_cost":0}]
        for i in self.itemShoppingList:
            if i['name'] not in self.item.cristalData:
                msg += "Name : "+ getName(i['itemID'], DATAID) + "  |  Price Per Unit :  "+ str(i['pricePerUnit']) + "  |  Quantity : "+ str(i['quantity']) + "  |  Hq : "+ str(i['hq'])  + '\n'
                self.itemWithout[0]["total_cost"] += i['pricePerUnit']*i['quantity']

        msg += "\n Total cost : " + str(self.itemWithout[0]["total_cost"]) + " \n For : "+ str(self.item.details["shopping_list"][0]["craft_amount"])+" "+ str(self.item.details["shopping_list"][0]["name"]) + " crafted" 

        await ctx.send(msg)

async def setup(bot):
    await bot.add_cog(SaddleBag(bot))
