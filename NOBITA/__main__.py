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

async def safe_start(bot):
    try:
        await bot.start()
    except Exception as e:
        print(f"Error while starting: {e}")
        await asyncio.sleep(2)
        await bot.start()
async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 𝐒𝐞𝐬𝐬𝐢𝐨𝐧")
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
    await safe.start(app)
    for all_module in ALL_MODULES:
        importlib.import_module("NOBITA.plugins" + all_module)
    LOGGER("NOBITA.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await safe.start(userbot)
    await safe.start(NOBITA)
    try:
        await NOBITA.stream_call("https://te.legra.ph/file/...")
except asyncio.TimeoutError:
    LOGGER("NOBITA").error("❌ Timeout while trying to stream.")
            "𝗣𝗹𝗭 𝗦𝗧𝗔𝗥𝗧 𝗬𝗢𝗨𝗥 𝗟𝗢𝗚 𝗚𝗥𝗢𝗨𝗣 𝗩𝗢𝗜𝗖𝗘𝗖𝗛𝗔𝗧\𝗖𝗛𝗔𝗡𝗡𝗘𝗟\n\n𝗡𝗢𝗕𝗜𝗧𝗔 𝗕𝗢𝗧 𝗦𝗧𝗢𝗣........"
        )
        exit()
    except:
        pass
    await NOBITA.decorators()
    LOGGER("NOBITA").info(
        "╔═════ஜ۩۞۩ஜ════╗\n  ☠︎︎𝗠𝗔𝗗𝗘 𝗕𝗬 𝗡𝗢𝗕𝗜𝗧𝗔☠︎︎\n╚═════ஜ۩۞۩ஜ════╝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("NOBITA").info("𝗦𝗧𝗢𝗣 𝗡𝗢𝗕𝗜𝗧𝗔 𝗠𝗨𝗦𝗜𝗖🎻 𝗕𝗢𝗧..")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
