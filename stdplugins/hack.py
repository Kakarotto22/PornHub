"""command: .هكر"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "هكر":

        await event.edit(input_str)

        animation_chars = [
        
            "`جاري الإتصال بالسيرفر الخاصّ بالاختراقات....`",
            "`Target Selected.`",
            "`جاري الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`جاري الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`جاري الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`جاري الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`جاري الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`جاري الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`تمّ كشف الثّغرة ... 84%\n█████████████████████▒▒▒▒ `",
            "`تمّ الحصول على جميع القيم 100%\n█████████HACKED███████████ `",
            "`تمّ اختراق هذا الحساب\n\nادفع 999$ To @channel22_22 لفكّ هذا الاختراق`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
