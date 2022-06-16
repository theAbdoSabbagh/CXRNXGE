import re, discord, requests

from discord.ext import commands
from discord.ext.commands import Cog

from utils.useful import custom, get_data, success, failure



class events(commands.Cog):
  """Events handled by the bot."""
  def __init__(self, bot : discord.Client):
    self.bot = bot
    self.hidden = True
    self.data = get_data()
    self.gift_regex = re.compile("(discord.com/gifts/|discordapp.com/gifts/|discord.gift/)([a-zA-Z0-9]+)")
    self.link_regex = re.compile("http://.*..*|https://.*..*")
    self.scam_links = requests.get("https://raw.githubusercontent.com/nikolaischunk/discord-phishing-links/main/domain-list.json").json()


  @Cog.listener("on_message")
  async def nitro_snipe(self, message):
    if self.gift_regex.search(message.clean_content):
      code = self.gift_regex.search(message.clean_content).group(2)
      headers = {
        'Authorization': self.data['token'],
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
        success(f"Sniped code: {code}", header = 'Nitro Sniper')
        data = response.json()
        if 'This gift has been redeemed already' in data['message']:
          custom('[Nitro Sniper] The code has already been used previously.')
        elif 'Unknown Gift Code' in data['message']:
          custom('[Nitro Sniper] The code is invalid.')
        else:
          custom(f'[Nitro Sniper] {data["message"]}')

  @Cog.listener("on_message_delete")
  async def deleted_log(self, message : discord.Message):
    if (len(message.clean_content) > 0
    and message.author.id != self.bot.user.id
    and message.author.id not in self.data['owner_ids']):
      if (message.channel.id in self.data['logged_channels']
      or message.guild.id in self.data['logged_guilds']):
        msg = f"{message.clean_content[:100]}...".split("\n")[0] if len(message.clean_content) > 100 else message.clean_content.split("\n")[0]
        custom(f'[Deleted Message] Author: {message.author} | Channel: {f"#{message.channel.name}" if isinstance(message.channel, discord.TextChannel) else f"DM with {message.author.name}"} | Content: {msg}', color = "bright_red")

  @Cog.listener("on_message")
  async def anti_scam_links(self, message : discord.Message):
    if (self.link_regex.search(message.clean_content) is not None
    and message.author.id != self.bot.user.id
    and message.author.id not in self.data['owner_ids']):
      link = self.link_regex.search(message.clean_content).group()
      if link is None:
        return
      link_ = link.replace('https://', '').replace('http://', '').replace('/', '')
      for index, splitted in enumerate(link_.split(' '), start = 0):
        if splitted in self.scam_links['domains']:
          custom(f"[Anti Scam Links] Found a scam link sent by {message.author}. Link: {link.split(' ')[index]}", color = 'magenta')
          await message.author.block()
          return

async def setup(bot):
  await bot.add_cog(events(bot))