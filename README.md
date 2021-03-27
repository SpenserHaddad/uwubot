# uwubot
Uwufier Discord bot. Uses the wonderful [uwuify](https://github.com/Daniel-Liu-c0deb0t/uwu/)/[uwufierpy](https://github.com/SpenserHaddad/uwufierpy) package to uwuify any message.

# Usage

Install the bot and then use the command `!uwu` to have it reply with the enhanced message:


    !uwu hello world!

# Setup

Requires Rust nightly or 1.51.0 to build uwufierpy and Python 3.7+.

```bash
# Need to install setuptools_rust first so uwufierpy is actually built.
pip install setuptools_rust
pip install -r requirements.txt
```

# Running

Either pass in your Discord token as the first arg to `bot.py` or set the `UWUBOT_DISCORD_TOKEN` environment variable.

```bash
# Pass in the token directly.
python bot.py <token>

# Or using environment variable
set UWUBOT_DISCORD_TOKEN <token>
python bot.py
```