import logging
from discord.ext import commands
from uwufier import uwufy

file_handler = logging.FileHandler("uwubot.log")
stream_handler = logging.StreamHandler()
logging.basicConfig(handlers=[file_handler, stream_handler])

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"Bot started as {bot.user}")


@bot.command(name="uwu")
async def uwufy_message(ctx, *args):
    message = " ".join(args)
    uwufy_message = uwufy(message)
    await ctx.send(uwufy_message)


if __name__ == "__main__":
    import argparse
    from os import getenv

    env_token = getenv("UWUBOT_DISCORD_TOKEN")
    parser = argparse.ArgumentParser(description="Start Uwufier Discord bot")
    parser.add_argument(
        "token",
        type=str,
        default=env_token,
        help="Discord token. Defaults to UWUBOT_DISCORD_TOKEN envvar",
    )

    args = parser.parse_args()
    if bot_token := args.token is None:
        raise ValueError(
            "Please supply a Discord token as either an arg or "
            / "the UWUBOT_DISCORD_TOKEN envvar"
        )

    bot.run(bot_token)
