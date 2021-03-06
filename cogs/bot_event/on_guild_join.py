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


class bot_join_guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild): 
        

        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()
            
            cursor.execute(f'INSERT INTO public."myBD" (guild_id, prefix_guild) VALUES ({guild.id}, \'t!\');')
            conn.commit()
        
            cursor.execute(f'INSERT INTO public."Texts_For_Welcome" (guild_id) VALUES ({guild.id});')
            conn.commit()
        
        except Exception as e:
            print(f'[Event: on_guild_join] [{guild.name}] [{guild.owner}] - [{e}]')
        finally:
            if(conn):
                cursor.close()
                conn.close()
                
def setup(bot):
    bot.add_cog(bot_join_guild(bot))