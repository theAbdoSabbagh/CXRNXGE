import os, json, time, discord, asyncio

from rich import print

def get_version():
    return '0.1'

def get_data():
    original_data = """{
    "prefix" : "",
    "owner_ids": [],
    "token": "",
    "logged_guilds": [],
    "logged_channels": [],
    "blacklisted_channels": []
}"""
    if not os.path.isfile('config.json'):
        with open("config.json", "w+") as file:
            file.write(original_data)
    with open('config.json', 'r+') as file:
        data = json.loads(file.read())
    return data

def success(text : str, timestamp : bool = True, header = None):
    header_ = 'Success' if header is None else f'{header} | Success'
    text = text.replace('\n', f'\n[{header_}] ')
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold green][{header_}] {text}[/bold green]" if timestamp else f"[bold green][{header_}] {text}[/bold green]")

def failure(text : str, timestamp : bool = True, header = None):
    header_ = 'Failure' if header is None else f'{header} | Failure'
    text = text.replace('\n', f'\n[{header_}] ')
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold red][{header_}] {text}[/bold red]" if timestamp else f"[bold red][{header_}] {text}[/bold red]")

def custom(text : str, timestamp : bool = True, color = 'blue'):
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold {color}]{text}[/bold {color}]" if timestamp else f"[bold {color}]{text}[/bold {color}]")

async def auto_bump(channel : discord.TextChannel, command : str, delay : int):
    name = channel.name
    while True:
        try: await channel.send(command)
        except discord.Forbidden: failure(f"Stopped bumping at #{name} due to an unsolvable error.", header = "Auto Bump"); break
        except discord.HTTPException: await asyncio.sleep(delay)
        else: await asyncio.sleep(delay)