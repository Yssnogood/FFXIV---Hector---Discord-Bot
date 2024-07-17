import discord
from discord.ext import commands

class Hello(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='Hello', help='Renvoie une réponse de salutation.')
    async def Hello(self, ctx):
        user_name = ctx.author.mention
        print('Hello function was used')
        await ctx.send(f"Greetings {user_name}, I'm Hector, your personal assistant designed to help you with various FFXIV needs.")

async def setup(bot):
    await bot.add_cog(Hello(bot))
