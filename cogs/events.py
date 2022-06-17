import re, discord, requests

from discord.ext import commands
from discord.ext.commands import Cog

from utils.useful import custom, get_data, success, failure

from rich import box, print
from rich.table import Table

class events(commands.Cog):
  """Events handled by the bot."""
  def __init__(self, bot : discord.Client):
    self.bot = bot
    self.hidden = True
    self.gift_regex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
    self.link_regex = re.compile("http://.*..*|https://.*..*")
    self.scam_links = requests.get("https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/domain-list.json").json()


  @Cog.listener("on_message")
  async def nitro_snipe(self, message):
    data = get_data()
    if data['nitrosnipe'] is False:
      return
    if self.gift_regex.search(message.clean_content):
      code = self.gift_regex.search(message.clean_content).group(2)
      headers = {
        'Authorization': data['token'],
        'user-agent': 'Mozilla/5.0'
      }
      json_ = {
        'channel_id': str(message.channel.id)
      }
      if 16 <= len(message.clean_content.lower().split('.gift/')[1]) <= 24:
        response = requests.post(
            f'https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem',
            json=json_,
            headers=headers
        )
        table = Table(
          title="Nitro Sniper \[Guild]" if isinstance(message.channel, discord.TextChannel) else "Nitro Sniper \[DM]",
          caption = f"Run {data['prefix']}nitrosnipe to disable this feature\n",
          box = box.HEAVY,
          style = "bold green"
        )
        data = response.json()
        table.add_column("Nitro Code", justify = "center")
        table.add_column("Nitro Redeem Response", justify = "center")
        table.add_column("Message ID", justify = "center")
        table.add_row(code, data['message'], str(message.id))
        print(table)

  @Cog.listener("on_message_delete")
  async def deleted_log(self, message : discord.Message):
    data = get_data()
    if data['deleted'] is False:
      return
    if (
        message.channel.id in data['blacklisted_channels']
        or len(message.clean_content) == 0
        or message.author.id == self.bot.user.id
        or message.author.id in data['owner_ids']
    ):
      return
    if (
        data['ignore_bots'] is True
        and message.author.bot
    ):
      return
    table = Table(
      title="Message Deletion Logger \[Guild]" if isinstance(message.channel, discord.TextChannel) else "Message Deletion Logger \[DM]",
      caption = f"Run {data['prefix']}deleted to disable this feature\n",
      box = box.HEAVY,
      style = "bold red"
    )
    if isinstance(message.channel, discord.TextChannel):
      table.add_column("Message Author", justify = "center")
      table.add_column("Channel", justify = "center")
      table.add_column("Content", justify = "center")
      table.add_column("Channel ID", justify = "center")
      table.add_column("Guild Name", justify = "center")
      table.add_row(str(message.author), f"#{str(message.channel.name)}", str(message.clean_content), str(message.channel.id), str(message.guild.name))
    else:
      table.add_column("DM Author", justify = "center")
      table.add_column("Content", justify = "center")
      table.add_column("Channel ID", justify = "center")
      table.add_row(str(message.author), str(message.clean_content), str(message.channel.id))

    if (
        data['log_all'] is True
    ):
      print(table)
    else:
      if (
          message.channel.id in data['logged_channels']
          or message.guild.id in data['logged_guilds']
      ):
        print(table)

  @Cog.listener("on_message")
  async def anti_scam_links(self, message : discord.Message):
    data = get_data()
    if data['antiscam'] is False:
      return
    if (
        self.link_regex.search(message.clean_content) is not None
        and message.author.id != self.bot.user.id
        and message.author.id not in data['owner_ids']
    ):
      link = self.link_regex.search(message.clean_content).group()
      if link is None:
        return
      link_ = link.replace('https://', '').replace('http://', '').replace('/', '')
      table = Table(
        title="Anti Scam Links \[Guild]" if isinstance(message.channel, discord.TextChannel) else "Anti Scam Links \[DM]",
        caption = f"Run {data['prefix']}antiscam to disable this feature\n",
        box = box.HEAVY,
        style = "bold magenta"
      )
      for index, splitted in enumerate(link_.split(' '), start = 0):
        if splitted in self.scam_links['domains']:
          table.add_column("Message Author", justify = "center")
          table.add_column("Scam Link", justify = "center")
          table.add_column("Message ID", justify = "center")
          table.add_row(str(message.author), link.split(' ')[index], str(message.id))
          print(table)
          return await message.author.block()

async def setup(bot):
  await bot.add_cog(events(bot))