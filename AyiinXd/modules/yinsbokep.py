


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo

from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP, BLACKLIST_CHAT
from AyiinXd.ayiin import ayiin_cmd, eod, eor
from Stringyins import get_string


@ayiin_cmd(pattern="bokep$")
async def _(ayiin):
    if ayiin.chat_id in BLACKLIST_CHAT:
        return await eod(ayiin, get_string("ayiin_1"), time=45)
    yins = await ayiin.eor(get_string("com_1"))
    try:
        asuyins = [
            asupan
            async for asupan in ayiin.client.iter_messages(
                "@bokep_yins_xd", filter=InputMessagesFilterVideo
            )
        ]
        awake = await ayiin.client.get_me()
        await ayiin.client.send_file(
            ayiin.chat_id,
            file=choice(asuyins),
            caption=get_string("yibkp_1").format(awake.first_name, awake.id)
        )
        await yins.delete()
    except Exception:
        await yins.edit(get_string("yibkp_2"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "bokep": f"**Plugin :** `bokep`\
        \n\n  »  **Perintah :** {cmd}bokep\
        \n  »  **Kegunaan : **Untuk Mengirim bokp secara random.\
    "
    }
)
