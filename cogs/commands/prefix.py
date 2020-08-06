import discord
from discord.ext import commands
import os
import asyncpg, asyncio

PREFIX=str('.')


class prefix(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    



    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        guildid= str(guild.id)
        async def main(self):
            conn = await asyncpg.connect(f'{url}')
            await conn.execute(f'INSERT INTO prefixDB (guild_id, prefix) VALUES ({guildid},{PREFIX})')
            await conn.close()
        

    @commands.Cog.listener()
    async def on_guild_remove(self):
        pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        pass






def setup(bot):
    bot.add_cog(prefix(bot))

url = os.environ.get('DATABASE_URL')
asyncio.get_event_loop().run_until_complete(main())