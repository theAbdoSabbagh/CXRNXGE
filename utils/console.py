from utils.useful import get_version

def title():
    title_ = """
[bold white]   █████████  █████ █████ ███████████   ██████   █████ █████ █████   █████████  ██████████
  ███░░░░░███░░███ ░░███ ░░███░░░░░███ ░░██████ ░░███ ░░███ ░░███   ███░░░░░███░░███░░░░░█
 ███     ░░░  ░░███ ███   ░███    ░███  ░███░███ ░███  ░░███ ███   ███     ░░░  ░███  █ ░ 
░███           ░░█████    ░██████████   ░███░░███░███   ░░█████   ░███          ░██████    
░███            ███░███   ░███░░░░░███  ░███ ░░██████    ███░███  ░███    █████ ░███░░█   
░░███     ███  ███ ░░███  ░███    ░███  ░███  ░░█████   ███ ░░███ ░░███  ░░███  ░███ ░   █
 ░░█████████  █████ █████ █████   █████ █████  ░░█████ █████ █████ ░░█████████  ██████████
  ░░░░░░░░░  ░░░░░ ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░ ░░░░░ ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ 
[/bold white]"""[1:]
    return title_

def data(bot):
    data_ = f"""
[bold white]Version: [bold blue]{get_version()}[/bold blue]
Prefix: [bold blue]{bot.prefix}[/bold blue]
Logged in as: [bold blue]{bot.user}[/bold blue] | [bold blue]{bot.user.id}[/bold blue]
Friends: [bold blue]{len(bot.user.friends)}[/bold blue]
Guilds: [bold blue]{len(bot.guilds)}[/bold blue]
[/bold white]"""[1:]
    return data_