from discord.ext import commands
from rich import print

from utils.console import data, title
from utils.useful import get_data

import os

config_data = get_data()

bot = commands.Bot(
    command_prefix = config_data['prefix'],
    strip_after_prefix = True,
    case_insensitive=True,
    cache_guilds_at_startup = False,
    owner_ids = config_data['owner_ids'],
    user_bot = True
)
bot._BotBase__cogs = commands.core._CaseInsensitiveDict()
bot.help_command = None # Might make a better one soon. Will use the subclassed version obviously.
bot.prefix = config_data['prefix']
bot.bumping_channels = [] # Do not change this
bot.hype_safe = True # Do not change this

@bot.listen('on_ready')
async def ready():
    os.system('cls')
    print(title(), flush = True)
    print(data(bot), flush = True)
    barrier = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                   Made By Sxvxge                                 
                             https://github.com/Sxvxgee                           
                         https://github.com/Sxvxgee/CXRNXGE                       
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""[1:]
    print(barrier, flush = True)
