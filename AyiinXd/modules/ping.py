# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# ReCode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de


import time
from datetime import datetime

from speedtest import Speedtest

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, StartTime
from AyiinXd.ayiin import edit_or_reply, humanbytes, ayiin_cmd
from time import sleep


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@ayiin_cmd(pattern="ping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    Ayiin = await edit_or_reply(ping, "**🅼**")
    await Ayiin.edit("**🅼🆈**")
    await Ayiin.edit("**🅼🆈-🆄**")
    await Ayiin.edit("**🅼🆈-🆄🆂**")
    await Ayiin.edit("**🅼🆈-🆄🆂🅴**")
    await Ayiin.edit("**🅼🆈-🆄🆂🅴🆁**")
    await Ayiin.edit("**🅼🆈-🆄🆂🅴🆁🅱**")
    await Ayiin.edit("**🅼🆈-🆄🆂🅴🆁🅱🅾**")
    await Ayiin.edit("**🅼🆈-🆄🆂🅴🆁🅱🅾🆃**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    await Ayiin.edit(
        f"**✧ 🅼🆈-🆄🆂🅴🆁🅱🅾🆃 ✧**\n\n"
        f"✧ **𝙿𝙸𝙽𝙶𝙴𝚁 :** `%sms`\n"
        f"✧ **𝚄𝙿𝚃𝙸𝙼𝙴 :** `{uptime}` \n"
        f"✧ **𝙾𝚆𝙽𝙴𝚁 :** [{user.first_name}](tg://user?id={user.id})" % (duration)
    )




@ayiin_cmd(pattern="speedtest$")
async def _(speed):
    xxnx = await edit_or_reply(speed, "`Running speed test...`")
    test = Speedtest()
    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()
    msg = (
        f"**Started at {result['timestamp']}**\n\n"
        "**Client**\n"
        f"**ISP :** `{result['client']['isp']}`\n"
        f"**Country :** `{result['client']['country']}`\n\n"
        "**Server**\n"
        f"**Name :** `{result['server']['name']}`\n"
        f"**Country :** `{result['server']['country']}`\n"
        f"**Sponsor :** `{result['server']['sponsor']}`\n\n"
        f"**Ping :** `{result['ping']}`\n"
        f"**Upload :** `{humanbytes(result['upload'])}/s`\n"
        f"**Download :** `{humanbytes(result['download'])}/s`"
    )
    await xxnx.delete()
    await speed.client.send_file(
        speed.chat_id,
        result["share"],
        caption=msg,
        force_document=False,
    )


@ayiin_cmd(pattern="pong$")
async def _(pong):
    start = datetime.now()
    xx = await edit_or_reply(pong, "`Sepong`")
    await xx.edit("Sepong Sayang.....")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await xx.edit("🥵")
    sleep(3)
    await xx.edit("**𝙿𝙸𝙽𝙶!**\n`%sms`" % (duration))


CMD_HELP.update(
    {
        "ping": f"**Plugin : **`ping`\
        \n\n  »  **Perintah :** `{cmd}ping` ; `{cmd}lping` ; `{cmd}xping` ; `{cmd}kping`\
        \n  »  **Kegunaan : **Untuk menunjukkan ping userbot.\
        \n\n  »  **Perintah :** `{cmd}pong`\
        \n  »  **Kegunaan : **Sama seperti perintah ping\
    "
    }
)


CMD_HELP.update(
    {
        "speedtest": f"**Plugin : **`speedtest`\
        \n\n  »  **Perintah :** `{cmd}speedtest`\
        \n  »  **Kegunaan : **Untuk Mengetes kecepatan server userbot.\
    "
    }
)
