import logging
import discord

file_handler = logging.FileHandler("uwubot.log")
stream_handler = logging.StreamHandler()
logging.basicConfig(handlers=[file_handler, stream_handler])

client = discord.Client()


@client.event
async def on_ready():
    print(f"Bot started as {client.user}")


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

    client.run(bot_token)
