module_name = "parameters"

import re


def replace_deco(func, bot):
    def replace_paras(*args, **kwargs):
        replace_dict = {
            "$PREFIX": bot.prefix,
            "$OWNER_NAME": bot.owner_name,
            "$BOT_NAME": bot.chatbot_name,
            "$GITHUB": bot.github
        }

        regex = re.compile("(%s)" % "|".join(map(re.escape, replace_dict.keys())))
        out = func(*args, **kwargs)
        if out is None:
            return None
        return regex.sub(lambda mo: replace_dict[mo.string[mo.start():mo.end()]], out)
    return replace_paras


def on_bot_load(bot):
    bot.command = replace_deco(bot.command, bot)

commands = []
