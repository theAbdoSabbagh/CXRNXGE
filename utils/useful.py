import asyncio, time, os, json, discord

from rich import print, box

original_data = """{
  "antiscam": true,
  "blacklisted_channels": [],
  "deleted": true,
  "ignore_bots": true,
  "log_all": false,
  "logged_channels": [],
  "logged_guilds": [],
  "nitrosnipe": true,
  "owner_ids": [],
  "prefix": "",
  "token": ""
}"""

def get_version():
    return '0.1'

def get_data():
    if not os.path.isfile('config.json'):
        with open("config.json", "w+") as file:
            file.write(original_data)
    with open('config.json', 'r+') as file:
        data = json.loads(file.read())
    return data

def save_data(data):
    if not os.path.isfile('config.json'):
        with open("config.json", "w+") as file:
            file.write(original_data)
    with open("config.json", "w+") as file:
        file.write(json.dumps(data, indent = 2, sort_keys = True))

def success(text : str, timestamp : bool = True, header = None):
    header_ = 'Success' if header is None else f'{header} | Success'
    text = str(text).replace('\n', f"\n[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] \[{header_}] " if timestamp else f"\n\[{header_}] ")
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold green]\[{header_}] {text}[/bold green]" if timestamp else f"[bold green]\[{header_}] {text}[/bold green]")

def failure(text : str, timestamp : bool = True, header = None):
    header_ = 'Failure' if header is None else f'{header} | Failure'
    text = str(text).replace('\n', f"\n[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] \[{header_}] " if timestamp else f"\n\[{header_}] ")
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold red]\[{header_}] {text}[/bold red]" if timestamp else f"[bold red]\[{header_}] {text}[/bold red]")

def cmd_error(text : str, timestamp : bool = True, header = None):
    header_ = 'Command Error' if header is None else f'{header} | Command Error'
    text = str(text).replace('\n', f"\n[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] \[{header_}] " if timestamp else f"\n\[{header_}] ")
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white] [bold red]\[{header_}] {text}[/bold red]" if timestamp else f"[bold red]\[{header_}] {text}[/bold red]")

def custom(text : str, timestamp : bool = True, color = 'blue', header = None):
    header_ = '' if header is None else f' \[{header}] '
    text = str(text).replace('\n', f"\n[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white]{header_}" if timestamp else f"\n{header_[1:]}")
    print(f"[bold white]{time.strftime('[%H:%M:%S]')}:[/bold white][bold {color}]{header_}{text}[/bold {color}]" if timestamp else f"[bold {color}]{header_}{text}[/bold {color}]")


async def auto_bump(channel : discord.TextChannel, command : str, delay : int):
    name = channel.name
    while True:
        try: await channel.send(command)
        except discord.Forbidden: failure(f"Stopped bumping at #{name} due to an unsolvable error.", header = "Auto Bump"); break
        except discord.HTTPException: await asyncio.sleep(delay)
        else: await asyncio.sleep(delay)