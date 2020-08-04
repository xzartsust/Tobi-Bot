# This Python file uses the following encoding: utf-8
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from config_for_bot import *
import youtube_dl
import os
from datetime import datetime
import logging
import time
import json
import asyncio
from itertools import cycle
from Cybernator import Paginator as pag
import moment
import arrow

########################################################## Logging ###################################################


logger= logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler= logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s: %(message)s'))
logger.addHandler(handler)


########################################################################################################################


bot=commands.Bot(command_prefix='.')
bot.remove_command('help')


############################################################# Events bot #################################################


async def is_owner(ctx):
    return ctx.author.id == 399851432221868033

async def change_status():
    await bot.wait_until_ready()
    msg= cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity= discord.Game(name=next_status))
        await asyncio.sleep(15)

@bot.event #включення бота
async def on_ready():
    print(f'Connect is {bot.user.name}')


######################################################### Commands bot ###################################################


@bot.command(aliases=['userinfo','ui','infouser'])#готовий
async def user(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    arrow.get()
    utc = arrow.utcnow()
    local = utc.to('Europe/Kiev')
    now_time = local.format('HH:mm')

    time_to_join_in_discord = member.created_at
    time_to_join_in_server = member.joined_at
    now = datetime.now()
    delta_s = now - time_to_join_in_server
    delta_d= now - time_to_join_in_discord
    b= delta_d.days
    a = delta_s.days
    print(now_time)


    if member.bot is False and member.nick is not None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',inline=False)
        emb.add_field(name='Присоединился к Discord',value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)',inline=False)
        emb.add_field(name='Присоединился к серверу',value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)',inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

        if member.activity is not None:
            emb.add_field(name='Кастом статус', value=member.activity, inline=False)
        else:
            emb.add_field(name='Кастом статус', value='Нету', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_author(name=member.nick)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' • Сегодня об: {now_time}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is False and member.nick is None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

        if member.activity is not None:
            emb.add_field(name='Кастом статус', value= member.activity,inline=False)
        else:
            emb.add_field(name='Кастом статус', value='Нету', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' • Сегодня об: {now_time}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is True and member.nick is None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

        emb.add_field(name='Кастомный статус', value=f'{member.activity}')

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' • Сегодня об: {now_time}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

    if member.bot is True and member.nick is not None:
        emb = discord.Embed(title=format(member), colour=discord.Color.green(), url=f'{member.avatar_url}',
                            inline=False)
        emb.add_field(name='Присоединился к Discord',
                      value=f'{time_to_join_in_discord.strftime("%d.%m.%Y %H:%M")}\n ({b} дней)', inline=False)
        emb.add_field(name='Присоединился к серверу',
                      value=f'{time_to_join_in_server.strftime("%d.%m.%Y %H:%M")}\n ({a} дней)', inline=False)
        emb.add_field(name='Самая высокая роль', value=str(member.top_role.mention), inline=False)
        emb.add_field(name='Айди', value=member.id, inline=False)

        if member.status == discord.Status.online:
            emb.add_field(name='Status', value=':green_circle: Онлайн', inline=False)
        elif member.status == discord.Status.dnd:
            emb.add_field(name='Status', value=':no_entry: Не беспокоить', inline=False)
        elif member.status == discord.Status.offline:
            emb.add_field(name='Status', value=':black_circle: Нет в сети', inline=False)
        elif member.status == discord.Status.idle:
            emb.add_field(name='Status', value=':crescent_moon: Отошол', inline=False)

        emb.add_field(name='Кастомный статус',value=f'{member.activity}', inline=False)

        emb.set_thumbnail(url=member.avatar_url)
        emb.set_author(name=member.nick)
        emb.set_footer(text='Заптрос от: ' + f'{ctx.author}' + f' Сегодня об: • {now_time}')

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@bot.command()
@commands.check(is_owner)
async def logout(ctx):
    await bot.logout()

@bot.command()
@commands.check(is_owner)
async def bot_servers(ctx):
    emb=discord.Embed(description=f'Присутствует на {str(len(bot.guilds))} серверах', colour=discord.Color.blurple())
    await ctx.send(embed= emb)

@bot.command(aliases=['i'])#команда .help
async def help(ctx):
    await ctx.channel.purge(limit=1)

    emb= discord.Embed(title='Помощ по использованию бота', description='Здесь вы можете узнать про осноные команды бота')

    emb1= discord.Embed(title='Команды бота')
    emb1.add_field(name='`{}help` или `{}info` или `{}i`'.format(PREFIX, PREFIX, PREFIX), value=' - Команды бота',inline=False)
    emb1.add_field(name='`{}prefix`'.format(PREFIX), value=' - Изменить префикс бота',inline=False)
    emb1.add_field(name='`{}user @имя`'.format(PREFIX),value=' - Информация про пользователя', inline=False)
    emb1.add_field(name='`{}ping`'.format(PREFIX),value=' - Посмотреть пинг бота', inline=False)
    emb1.add_field(name='`{}bot_servers`'.format(PREFIX),value=' - Посмотреть на скольких серверах есть етот бот', inline=False)
    emb1.add_field(name='`{}tuser`'.format(PREFIX), value=' - Посмотреть сколько всего человек используют этого бота',inline=False)

    emb2=discord.Embed(title='Команды для модерации', description='Скоро...')

    embeds=[emb,emb1,emb2]
    message= await ctx.send(embed= emb)
    page= pag(bot, message, only=ctx.author, use_more=False, embeds=embeds, color=0x008000, delete_message=True,time_stamp=True)

    await page.start()

@bot.command()#готовий
async def ping(ctx):
    time_1 = time.perf_counter()
    await ctx.trigger_typing()
    time_2 = time.perf_counter()
    ping = round((time_2 - time_1) * 1000)
    emb= discord.Embed(description=f'Pong: {ping}ms',colour=discord.Color.blurple())
    await ctx.channel.purge(limit=1)
    await ctx.send(embed= emb)

@bot.command()
async def clear(ctx, arg):
    await ctx.channel.purge(limit= int(arg))


@bot.command()
async def tuser(ctx):
    all_users = set([])
    for user in bot.get_all_members():
        all_users.add(user)
    await ctx.channel.purge(limit=1)
    await ctx.send('Total users in all my servers combined: ' + str(len(all_users)))


####################################################### Errors ###############################################


@clear.error
async def clear_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='У вас нет прав на ету команду')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@bot_servers.error
async def logout_error(ctx,error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='Эту команду имеет право использовать только создатель бота')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

@_eval.error
async def _eval_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        emb = discord.Embed(title='Ошибка!!!', colour=discord.Color.red(), description='Эту команду имеет право использовать только создатель бота')
        await ctx.channel.purge(limit=1)
        await ctx.send(embed=emb)

####################################################### Eval ###############################################


@bot.command(aliases=['eval'])
@commands.is_owner()
async def _eval(ctx,*,code):
    await ctx.send(eval(code))



TOKEN = os.environ.get('TOKEN')

bot.loop.create_task(change_status())
bot.run(TOKEN)
