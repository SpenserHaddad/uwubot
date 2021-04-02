"""Credit: https://github.com/remyjette/DiscordPollBot/blob/a0ee4a61fe2c204e903a84dcfbac772246a607b0/bot/utils.py#L5"""


def remove_mentions(str, bot, guild=None):
    def replace_id_string_with_username(id_string):
        user = bot.instance.get_user(int(id_string))
        if not user:
            return f"@{id_string}"
        return f"@{user.name}#{user.discriminator}"

    def replace_id_string_with_role(id_string):
        if guild and (role := guild.get_role(int(id_string))):
            return f"@{role.name}"
        else:
            return f"@{id_string}"

    def replace_id_string_with_channel(id_string):
        channel = bot.instance.get_channel(int(id_string))
        if not channel:
            return f"#{id_string}"
        return f"#{channel.name}"

    def remove_mentions_replacement(matchobj):
        if matchobj.group(1) == "@":
            return replace_id_string_with_username(int(matchobj.group(2)))
        if matchobj.group(1) == "@&":
            return replace_id_string_with_role(int(matchobj.group(2)))
        if matchobj.group(1) == "#":
            return replace_id_string_with_channel(int(matchobj.group(2)))

    return re.sub(r"<(@|@&|#)!?(\d+)>", remove_mentions_replacement, str)