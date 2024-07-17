from discord.ext import commands
from Src.Recipes import *

class Recipes(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='RecipeOf:', help='Send the recipe of an asked item.')
    async def RecipeOf(self, ctx, args, howMany=1):

        try:
            recipeResult = recipeFromName(args, howMany)
            if not recipeResult:
                raise ItemNotFoundError(f" '{args}' doesn't seem to exist.")
        except ItemNotFoundError as e:
            print(e)
            await ctx.send(f"I'm sorry,{e}")
            return
        
        msg = "You'll get : "+str(recipeResult[1])+" of "+ str(recipeResult[0]) + '\n' + "=== Mats needed ===" + '\n'+'\n'
        for x in range(2, len(recipeResult),2):
            msg = msg + str(recipeResult[x]) + " : " + str(recipeResult[x+1]) + '\n'
            
        await ctx.send(msg)
    
    @commands.command(name='RecipesOf:', help="show Recipe and SubRecipes for an item")
    async def RecipesOf(self, ctx, args, howMany=1):

        try:
            recipesResult = recipeFromName(args, howMany)
            if not recipesResult:
                raise ItemNotFoundError(f" '{args}' doesn't seem to exist.")
        except ItemNotFoundError as e:
            print(e)
            await ctx.send(f"I'm sorry,{e}")
            return
        
        msg = "You'll get : "+str(recipesResult[0][1])+" of "+ str(recipesResult[0][0]) + '\n' + "=== Mats needed ===" + '\n'
        for x in range(2, len(recipesResult[0]),2):
            msg = msg + str(recipesResult[0][x]) + " : " + str(recipesResult[0][x+1]) + '\n'

        msg += " \n == You can also need == \n "
        for x in range(0, len(recipesResult[1])):
            msg += '\n' + str(recipesResult[1][x][1]) + " x " + str(recipesResult[1][x][0]) + '\n'
            for y in range(2, len(recipesResult[1][x]),2):
                msg += str(recipesResult[1][x][y]) + " : "+ str(recipesResult[1][x][y+1]) + '\n'

        await ctx.send(msg)


async def setup(bot):
    await bot.add_cog(Recipes(bot))
