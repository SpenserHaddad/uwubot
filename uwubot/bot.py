import logging
from discord import Colour, Embed, Message
from discord.ext import commands
from uwufier import uwufy
from uwubot.remove_mentions import remove_mentions

file_handler = logging.FileHandler("uwubot.log")
stream_handler = logging.StreamHandler()
logging.basicConfig(handlers=[file_handler, stream_handler])

bot = commands.Bot(command_prefix="!")

chaos_channels = set()

CHAOS_ON_MESSAGE = uwufy("Giving this channel some nice chaos energy ༼ つ ◕_◕ ༽つ")
CHAOS_OFF_MESSAGE = uwufy("Chaos energy depleted, chilling for now")
NO_CHAOS_MESSAGE = uwufy("Gotta ask for that chaos energy first V_V")
EMBED_FOOTER = uwufy("Sent with ❤️ from UwuBot")


@bot.event
async def on_ready():
    print(f"Bot started as {bot.user}")


@bot.command(name="uwu")
async def uwufy_message(ctx: commands.Context):
    message = ctx.message.content.replace("!uwu ", "", 1)
    uwufy_message = uwufy(message)
    await ctx.reply(uwufy_message)


@bot.command(name="chaos")
async def start_chaos(ctx: commands.Context):
    chaos_channels.add(ctx.channel.id)
    await ctx.send(CHAOS_ON_MESSAGE)


@bot.command(name="unchaos")
async def stop_chaos(ctx: commands.Context):
    if ctx.channel.id in chaos_channels:
        chaos_channels.remove(ctx.channel.id)
        await ctx.reply(CHAOS_OFF_MESSAGE)
    else:
        await ctx.reply(NO_CHAOS_MESSAGE)


@bot.event
async def on_message(message: Message):
    channel = message.channel
    if (
        message.channel.id in chaos_channels
        and message.author != bot.user
        and not message.content.startswith("!unchaos")
    ):
        author_name = message.author.display_name
        message_without_mentions = remove_mentions(
            message.content, bot, guild=message.guild
        )
        uwufy_message = uwufy(message_without_mentions)
        embed = Embed(title=uwufy_message, colour=Colour(0xFF69B4))
        embed.set_author(name=author_name, icon_url=message.author.avatar_url)
        embed.set_footer(text=EMBED_FOOTER)
        await message.delete()
        await channel.send(embed=embed)

    else:
        await bot.process_commands(message)
