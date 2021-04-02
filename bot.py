import logging
from discord import Message
from discord.ext import commands
from uwufier import uwufy

file_handler = logging.FileHandler("uwubot.log")
stream_handler = logging.StreamHandler()
logging.basicConfig(handlers=[file_handler, stream_handler])

bot = commands.Bot(command_prefix="!")

chaos_channels = set()

CHAOS_ON_MESSAGE = uwufy("Giving this channel some nice chaos energy ༼ つ ◕_◕ ༽つ")
CHAOS_OFF_MESSAGE = uwufy("Chaos energy depleted, chilling for now")
NO_CHAOS_MESSAGE = uwufy("Gotta ask for that chaos energy first V_V")


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
        uwufy_message = uwufy(message.content)
        await message.delete()
        await channel.send(uwufy_message)
    await bot.process_commands(message)


if __name__ == "__main__":
    import argparse
    from os import getenv

    env_token = getenv("UWUBOT_DISCORD_TOKEN")
    parser = argparse.ArgumentParser(description="Start Uwufier Discord bot")
    parser.add_argument(
        "token",
        type=str,
        nargs="?",
        default=env_token,
        help="Discord token. Defaults to UWUBOT_DISCORD_TOKEN envvar",
    )

    args = parser.parse_args()
    if args.token is None:
        raise ValueError(
            "Please supply a Discord token as either an arg or "
            / "the UWUBOT_DISCORD_TOKEN envvar"
        )

    bot.run(args.token)
