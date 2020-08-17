import discord
from discord.ext import commands
import asyncpg, asyncio
import psycopg2
import os
from discord import utils
from discord.utils import get

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

conn = psycopg2.connect(
    database = f"{database}", 
    user = f"{user}", 
    password = f"{password}", 
    host = f"{host}", 
    port = "5432"
)

cursor = conn.cursor()

class member_greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self):
        for guild in self.bot.guilds:
            await guild.system_channel.send("I'm ready to go!")


    @commands.command()
    async def greet(self, ctx):
        await ctx.send(str(ctx.guild.system_channel))



def setup(bot):
    bot.add_cog(member_greeting(bot))