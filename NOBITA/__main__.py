import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from NOBITA import LOGGER, app, userbot
from NOBITA.core.call import NOBITA
from NOBITA.misc import sudo
from NOBITA.plugins import ALL_MODULES
from NOBITA.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("String Session Not Filled, Please Fill A Pyrogram Session")
        exit()

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("NOBITA.plugins." + all_module)
    LOGGER("NOBITA.plugins").info("All Features Loaded Baby🥳...")

    await userbot.start()
    await NOBITA.start()

    try:
        await NOBITA.stream_call("https://te.legra.ph/file/...")
    except NoActiveGroupCall:
        LOGGER("NOBITA").error(
            "PIZ START YOUR LOG GROUP VOICECHAT / CHANNEL\n\nNOBITA BOT STOP........"
        )
        exit()
    except Exception as e:
        LOGGER("NOBITA").error(f"Unexpected error during stream_call: {e}")

    await NOBITA.decorators()
    LOGGER("NOBITA").info(
        "\n╔═════ஜ۩۞۩ஜ════╗\n  ☘︎MADE BY NOBITA☘︎\n╚═════ஜ۩۞۩ஜ════╝"
    )

    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NOBITA").info("STOP NOBITA MUSIC🎼 BOT..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
