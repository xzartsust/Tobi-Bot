import discord
from discord.ext import commands
import asyncpg
import psycopg2
import os

database = os.environ.get('DATABASE')
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')


class Warns(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def warn(self, ctx, member: discord.Member, *, reason = None):
        
        
        guild = ctx.message.guild
        member_id = member.id
        userr = ctx.message.author.id

        try:
            conn = psycopg2.connect(
                database = f"{database}", 
                user = f"{user}", 
                password = f"{password}", 
                host = f"{host}", 
                port = "5432"
            )

            cursor = conn.cursor()
            
            if member.bot is True:
                await ctx.send('Ей, боту нельзя выдать предупреждение')
                return
            
            if member_id is userr:
                await ctx.send('Ей, нельзя самому себе выдать предупреждение')
                return 
            
            if member_id is ctx.guild.owner.id:
                await ctx.send('Ей, нельзя владельцу сервера выдать предупреждение')
                return

            cursor.execute(f'SELECT member_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            memberDB = cursor.fetchone()
            conn.commit()
            
            cursor.execute(f'SELECT guild_id FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
            guildDB = cursor.fetchone()
            conn.commit()
            
            if memberDB is None and guildDB is None:
                
                cursor.execute(f'INSERT INTO public."Warns" (guild_id, member_id) VALUES (\'{guild.id}\',\'{member_id}\');')
                conn.commit()

                cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
                count = cursor.fetchone()
                conn.commit()
                
                count_now = count[0] + 1
            
                cursor.execute(f'UPDATE public."Warns" SET counts = \'{count_now}\' WHERE guild_id= \'{guild.id}\' AND member_id = \'{member_id}\';')
                conn.commit()

                if reason is None:
                    warn = discord.Embed(
                        title = f'{member} предупреждения :exclamation::exclamation:',
                        timestamp = ctx.message.created_at,
                        colour = discord.Color.red()
                    )
                    warn.add_field(
                        name = 'Пользователь',
                        value = f'{member.mention}'
                    )
                    warn.set_thumbnail(
                        url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                    )
                    warn.add_field(
                        name = 'Модератор',
                        value = f'{ctx.message.author.mention}'
                    )
                    warn.add_field(
                        name = 'Причина',
                        value = 'Не указана'
                    )
                    await ctx.send(embed = warn)
                
                else:
                    warn = discord.Embed(
                        title = f'{member} предупреждения :exclamation::exclamation:',
                        timestamp = ctx.message.created_at,
                        colour = discord.Color.red()
                    )
                    warn.add_field(
                        name = 'Пользователь',
                        value = f'{member.mention}'
                    )
                    warn.add_field(
                        name = 'Модератор',
                        value = f'{ctx.message.author.mention}'
                    )
                    warn.set_thumbnail(
                        url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                    )
                    warn.add_field(
                        name = 'Причина',
                        value = f'{reason}'
                    )
                    await ctx.send(embed = warn)
            
            else:
            
                cursor.execute(f'SELECT counts FROM public."Warns" WHERE guild_id = \'{guild.id}\' AND member_id = \'{member_id}\';')
                count = cursor.fetchone()
                conn.commit()
            
                count_now = count[0] + 1
            
                cursor.execute(f'UPDATE public."Warns" SET counts = \'{count_now}\' WHERE guild_id= \'{guild.id}\' AND member_id = \'{member_id}\';')
                conn.commit()

                if reason is None:
                    warn = discord.Embed(
                        title = f'{member} предупреждения :exclamation::exclamation:',
                        timestamp = ctx.message.created_at,
                        colour = discord.Color.red()
                    )
                    warn.add_field(
                        name = 'Пользователь',
                        value = f'{member.mention}'
                    )
                    warn.set_thumbnail(
                        url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                    )
                    warn.add_field(
                        name = 'Модератор',
                        value = f'{ctx.message.author.mention}'
                    )
                    warn.add_field(
                        name = 'Причина',
                        value = 'Не указана'
                    )
                    await ctx.send(embed = warn)
                
                else:
                    warn = discord.Embed(
                        title = f'{member} предупреждения :exclamation::exclamation:',
                        timestamp = ctx.message.created_at,
                        colour = discord.Color.red()
                    )
                    warn.add_field(
                        name = 'Пользователь',
                        value = f'{member.mention}'
                    )
                    warn.add_field(
                        name = 'Модератор',
                        value = f'{ctx.message.author.mention}'
                    )
                    warn.set_thumbnail(
                        url = 'https://github.com/xzartsust/Tobi-Bot/blob/master/files/image/warn.jpg?raw=true'
                    )
                    warn.add_field(
                        name = 'Причина',
                        value = f'{reason}'
                    )
                    await ctx.send(embed = warn)
        
        except Exception as e:
            print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{e}]')
        
        finally:
            if(conn):
                cursor.close()
                conn.close()
                

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        await ctx.send('Произошла ошибка: {}'.format(str(error)))
        print(f'[{ctx.message.created_at}] [{ctx.message.guild.name}] [{ctx.message.guild.owner}] - [{error}]')

def setup(bot):
    bot.add_cog(Warns(bot))