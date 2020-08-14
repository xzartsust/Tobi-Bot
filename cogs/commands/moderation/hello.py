import discord
from discord.ext import commands
import asyncpg, asyncio
import psycopg2
import os

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
    async def on_guild_join(self, ctx):
        pass


    @commands.command()
    async def greet(self, ctx, channel: discord.TextChannel):
        guild_channel_id = ctx.message.guild.id
        cursor.execute(f'UPDATE public."prefixDB" SET channel_for_greet=\'{channel}\' WHERE guild_id = \'{guild_channel_id}\';')
        conn.commit()
        
    @commands.command()
    async def print(self, ctx, channel: discord.TextChannel):
        guild_channel_id = ctx.message.guild.id
        cursor.execute(f'SELECT channel_for_greet FROM public."prefixDB" WHERE guild_id = \'{guild_channel_id}\';')
        channel = cursor.fetchone()
        
        await channel.send('ok')


def setup(bot):
    bot.add_cog(member_greeting(bot))