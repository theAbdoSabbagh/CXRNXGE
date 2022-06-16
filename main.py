import asyncio, os

from rich import print

from utils.selfbot import bot
from utils.useful import get_data


config_data = get_data()

async def main():
    if len(config_data['token']) <= 0:
        raise ValueError("Expected a valid Token in the config settings but it was empty.")
    else:
        for filename in os.listdir('cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[:-3]}')
        await bot.start(config_data['token'].replace('\n', '').replace(' ', ''))

if __name__ == '__main__':
    asyncio.run(main())