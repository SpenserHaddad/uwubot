from uwubot.bot import bot

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
