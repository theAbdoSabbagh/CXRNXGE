import discord

from discord.ext import commands
from discord.ext.commands import Cog

from utils.useful import cmd_error


class errors(commands.Cog):
  def __init__(self, bot):
    self.bot = bot 
    self.hidden = True


  @Cog.listener("on_command_error") 
  async def ErrorHandlers(self, ctx, error):
      if isinstance(error, commands.CommandNotFound):
        print(ctx.command.name)

      elif isinstance(error, commands.DisabledCommand):
        cmd_error(f"This command is disabled.", header = ctx.command.name)
        
      elif isinstance(error, commands.MessageNotFound):
        cmd_error(f"Message not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.MemberNotFound):
        cmd_error(f"Member not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.UserNotFound):
        cmd_error(f"User not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.ChannelNotFound):
        cmd_error(f"Channel not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.EmojiNotFound):
        cmd_error(f"Emoji not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.RoleNotFound):
        cmd_error(f"Role not found.", header = ctx.command.name)
        
      elif isinstance(error, commands.ChannelNotReadable):
        cmd_error(f"Insufficient permissions for reading messages in the channel", header = ctx.command.name)
        
      elif isinstance(error, commands.BadColourArgument):
        cmd_error(f"Invalid color.", header = ctx.command.name)
        
      elif isinstance(error, commands.BadInviteArgument):
        cmd_error(f"Invalid invite.", header = ctx.command.name)

      elif isinstance(error, commands.PartialEmojiConversionFailure):
        cmd_error(f"Couldn't covert [reverse]{error.argument}[/reverse] to PartialEmoji.", header = ctx.command.name)
        
      elif isinstance(error, commands.PrivateMessageOnly):
        cmd_error(f"This command can only be used in private messages.", header = ctx.command.name)
        
      elif isinstance(error, commands.NoPrivateMessage):
        cmd_error(f"This command cannot be used in private messages.", header = ctx.command.name)

      elif isinstance(error, commands.NotOwner):
        cmd_error(f"Command is runnable by owner only.", header = ctx.command.name)
        
      elif isinstance(error, commands.MissingPermissions):
        cmd_error(f"Insufficient permissions.", header = ctx.command.name)

      elif isinstance(error, commands.BotMissingPermissions):
        cmd_error(f"Insufficient permissions.", header = ctx.command.name)

      elif isinstance(error, commands.MissingRole):
        cmd_error(f"Missing role [reverse]{error.missing_role}[/reverse] that is required for running the command.", header = ctx.command.name)

      elif isinstance(error, commands.BotMissingRole):
        cmd_error(f"Missing role [reverse]{error.missing_role}[/reverse] that is required for running the command.", header = ctx.command.name)
        
      elif isinstance(error, commands.MissingAnyRole):
        cmd_error(f"Missing multiple roles required to run the command.", header = ctx.command.name)

      elif isinstance(error, commands.BotMissingAnyRole):
        cmd_error(f"Missing multiple roles required to run the command.", header = ctx.command.name)
        
      elif isinstance(error, commands.NSFWChannelRequired):
        cmd_error(f"Channel [reverse]{error.channel}[/reverse] needs to be NSFW for this command to work.", header = ctx.command.name)
        
      elif isinstance(error, commands.TooManyArguments):
        cmd_error(f"Too many arguments passed to the command.", header = ctx.command.name)
        
      elif isinstance(error, commands.BadArgument):
        cmd_error(f"Invalid argument passed to the command.", header = ctx.command.name)
        
      elif isinstance(error, commands.CommandOnCooldown):
        cmd_error(f"You are on cooldown. Try again in [reverse]{error.retry_after:.2f}[/reverse]s", header = ctx.command.name)
        
      elif isinstance(error, commands.MissingRequiredArgument):
        cmd_error(f"[reverse]{error.param.name}[/reverse] is a required argument that is missing.", header = ctx.command.name)
        
      elif isinstance(error, commands.CommandInvokeError):
        original_error = error.original
        cmd_error(f"Command raised an exception: {original_error}", header = ctx.command.name)



async def setup(bot):
  await bot.add_cog(errors(bot))