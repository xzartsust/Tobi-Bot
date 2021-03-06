######################################################## libraries #########################################################


import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import os
from datetime import datetime
import time
import asyncio
from itertools import cycle
from Cybernator import Paginator as pag
import psycopg2
import asyncpg
import youtube_dl
import shutil
import logging


########################################################## Connect to SQL ###################################################


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


########################################################################################################################


def get_prefix(bot, message):
    guildid = message.guild.id
    cursor.execute(f'SELECT prefix_guild FROM public."myBD" WHERE guild_id = \'{guildid}\';')
    prefix = cursor.fetchone()
    conn.commit()
    
    return prefix

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = get_prefix, help_command = None, intents = intents)

logging.basicConfig()


############################################################# Events bot #################################################


async def change_status():
    await bot.wait_until_ready()
    msg = cycle(status)

    while not bot.is_closed():
        next_status= next(msg)
        await bot.change_presence(activity = discord.Game(name=next_status))
        await asyncio.sleep(9)
status=['t!help', 'Модернизирует свой код', 'Сайт: https://github.com/xzartsust/Tobi-Bot#tobi-bot', 'Серевер поддержки: https://discord.gg/8f4KUp']
        
        
################################################## Cogs Info commands ############################################################


bot.load_extension('cogs.commands.info.user')
bot.load_extension('cogs.commands.info.help_commands')
bot.load_extension('cogs.commands.info.invite')
bot.load_extension('cogs.commands.info.infobot')
bot.load_extension('cogs.commands.info.serverinfo')
bot.load_extension('cogs.commands.info.prefixserver')
bot.load_extension('cogs.commands.info.avatar')


################################################## Cogs Moderation commands ######################################################


bot.load_extension('cogs.commands.moderation.command.rwlc')
bot.load_extension('cogs.commands.moderation.command.ban')
bot.load_extension('cogs.commands.moderation.command.muterole')
bot.load_extension('cogs.commands.moderation.commands_for_welcome.welcome')
bot.load_extension('cogs.commands.moderation.utilit.news')
bot.load_extension('cogs.commands.moderation.utilit.prefix')
bot.load_extension('cogs.commands.moderation.utilit.clear')
bot.load_extension('cogs.commands.moderation.command.kick')
bot.load_extension('cogs.commands.moderation.command.unban')
bot.load_extension('cogs.commands.moderation.utilit.vote')
bot.load_extension('cogs.commands.moderation.command.mute')
bot.load_extension('cogs.commands.moderation.command.unmute')
bot.load_extension('cogs.commands.moderation.commands_for_welcome.welcometexttitle')
bot.load_extension('cogs.commands.moderation.commands_for_welcome.welcometextdescription')
bot.load_extension('cogs.commands.moderation.commands_for_welcome.welcometextfooter')
bot.load_extension('cogs.commands.moderation.warns.warn')
bot.load_extension('cogs.commands.moderation.warns.mywarn')
bot.load_extension('cogs.commands.moderation.warns.resetwarn')
bot.load_extension('cogs.commands.moderation.utilit.send')
bot.load_extension('cogs.commands.moderation.created_privat_channel.private_channel')
bot.load_extension('cogs.commands.moderation.created_privat_channel.lock')
bot.load_extension('cogs.commands.moderation.created_privat_channel.unlock')
bot.load_extension('cogs.commands.moderation.report_system.report')
bot.load_extension('cogs.commands.moderation.report_system.report_channel')


################################################## Cogs Music commands ###########################################################


#bot.load_extension('cogs.commands.music.join')
#bot.load_extension('cogs.commands.music.leave')
#bot.load_extension('cogs.commands.music.pause')
#bot.load_extension('cogs.commands.music.resume')
#bot.load_extension('cogs.commands.music.stop')
#bot.load_extension('cogs.commands.music.next')
#bot.load_extension('cogs.commands.music.play')
#bot.load_extension('cogs.commands.music.play')


################################################## Cogs Owner commands ############################################################


bot.load_extension('cogs.cogs_owner.out')
bot.load_extension('cogs.cogs_owner._eval')
bot.load_extension('cogs.test')
bot.load_extension('cogs.cogs_owner.tuser')


################################################# Cogs Event ######################################################################


bot.load_extension('cogs.bot_event.ready')
bot.load_extension('cogs.bot_event.on_guild_join')
bot.load_extension('cogs.bot_event.on_guild_remove')


################################################# Cogs Fun commands ##############################################################


bot.load_extension('cogs.commands.fun.simply.fox')
bot.load_extension('cogs.commands.fun.simply.memes')
bot.load_extension('cogs.commands.fun.simply.dog')
bot.load_extension('cogs.commands.fun.simply.cat')
bot.load_extension('cogs.commands.fun.simply.hug')
bot.load_extension('cogs.commands.fun.simply.panda')
bot.load_extension('cogs.commands.fun.simply.pat')
bot.load_extension('cogs.commands.fun.simply.redpanda')
bot.load_extension('cogs.commands.fun.simply.wink')
bot.load_extension('cogs.commands.fun.simply.koala')
bot.load_extension('cogs.commands.fun.simply.neko')
bot.load_extension('cogs.commands.fun.nsfw.neko_nsfw')
bot.load_extension('cogs.commands.fun.simply.textcat')
bot.load_extension('cogs.commands.fun.nsfw.holo_nsfw')
bot.load_extension('cogs.commands.fun.simply.holo')
bot.load_extension('cogs.commands.fun.simply.tickle')
bot.load_extension('cogs.commands.fun.nsfw.classic')
bot.load_extension('cogs.commands.fun.nsfw.aniero')
bot.load_extension('cogs.commands.fun.nsfw.kitsune_ero')
bot.load_extension('cogs.commands.fun.simply.poke')
bot.load_extension('cogs.commands.fun.nsfw.les')
bot.load_extension('cogs.commands.fun.nsfw.lewd_kitsune')
bot.load_extension('cogs.commands.fun.nsfw.keta')
#bot.load_extension('cogs.commands.fun.simply.neko_gif')


#####################################################################################################################################


TOKEN = os.environ.get('TOKEN')

bot.loop.create_task(change_status())
bot.run(TOKEN)
