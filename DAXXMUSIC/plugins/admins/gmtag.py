from DAXXMUSIC import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]

TAGMES = [ " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ 🌚** ",
           " **➠ ɢᴜᴘ ᴄʜᴜᴘ ᴘᴀᴅᴜᴋᴏᴏ 🙊** ",
           " **➠ ᴘʜᴏɴᴇ ᴘᴀᴋᴋᴀɴᴀ ᴘᴇᴛᴛɪ ᴘᴀᴅᴜᴋᴏ , ʟᴇᴅᴀɴᴛᴇʏ ᴅᴀʏᴀᴍ ᴠᴀsᴛᴀᴅɪ..👻** ",
           " **➠ ᴏʜʜ ʙᴀʙʏ ᴘᴏᴅᴅᴜɴᴀ ᴘʜᴏɴᴇ ᴄʜᴜsᴋᴏ ɪᴘᴘᴜᴅᴜ ᴘᴀᴅᴜᴋᴏᴏ..?? 🥲** ",
           " **➠ ᴍᴜᴍᴍʏ ᴠɪᴅᴜ ᴄʜᴜᴅᴜ ɢғ ᴛʜᴏ ᴍᴀᴛʟᴀᴅᴜ ᴛᴜɴɴᴀᴅᴜ ʙᴇᴅ sʜᴇᴇᴛ ʟᴏᴘᴀʟᴀ ᴘʜᴏɴᴇ ᴘᴇᴛᴛɪ , ᴘᴀᴅᴜᴋᴏᴠᴀᴛ ʟᴇᴅᴜ 😜** ",
           " **➠ ᴅᴀᴅᴅʏ ᴠɪᴅᴜ ᴄʜᴜᴅᴜ ɴɪɢʜᴛ ᴀɴᴛᴀ ᴘʜᴏɴᴇ ᴄʜᴜsᴛᴜɴɴᴀᴅᴜ 🤭** ",
           " **➠ ʙᴀʙʏ , ɴɪɢʜᴛ ᴇᴍ ᴘʟᴀɴɪɴɢs..?? 🌠** ",
           " **➠ ɢɴ sᴅ ᴛᴄ.. 🙂** ",
           " **➠ ɢᴏᴏᴅ ɴɪɢʜᴛ sᴡᴇᴇᴛ ᴅʀᴇᴀᴍ ᴛᴀᴋᴇ ᴄᴀʀᴇ..?? ✨** ",
           " **➠ ᴄʜᴀʟᴀ ɴɪɢʜᴛ ᴀɪɴᴅɪ , ᴘᴀᴅᴜᴋᴏᴏᴏ, ɢɴ..?? 🌌** ",
           ]

VC_TAG = [ "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ , ᴇʟᴀᴀ ᴜɴɴᴀᴠ 🐱**",
         "**➠ ᴍᴏʀɴɪɴɢ ᴀʏɪɴᴅɪ ɪɴᴋᴀ ᴅᴜɴᴘᴏᴛᴜɴᴀ ᴘᴀᴅᴜᴋᴜɴᴀᴠ ᴀɴᴛɪ ʟᴇɢᴜ 🌤️**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʙᴀɴɢᴀʀᴀᴍ ʟᴇɢᴜ ɴɪ ᴋᴏsᴀᴍ ʙʀᴇᴀᴋғᴀsᴛ ʀᴇᴀᴅʏ ᴄʜᴇsᴀ **",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ Pᴜʟɪʜᴏʀᴀ ʀᴀᴊᴀ 🏫**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ Pᴜʟɪʜᴏʀᴀ ʀᴀɴɪ 🏫**",
         "**➠ ᴛᴏɴᴅᴀʀɢᴀ ʟᴇɢᴜ ʟᴇᴅᴀɴᴛᴇʏ ʙᴇᴅsʜᴇᴇᴛ ʟᴏ ᴡᴀᴛᴇʀ ᴠᴇsᴇsᴛᴀ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ  🧊**",
         "**➠ ᴍᴀɴᴀ ᴀɴᴜᴋᴜɴᴇ ᴠᴀʀɪɴɪ ᴠᴜᴅʜʏᴀɴᴇ ᴘᴀʟɪᴋɪsᴛʜᴇ ᴍᴀɴᴀsᴜᴋᴜ ᴠᴀᴄʜᴇ ᴀɴᴀᴅᴀʜᴍᴀ ᴇʏ ᴠᴇʀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🫶 **",
         "**➠ ᴀ sᴍɪʟᴇ ᴛᴏ sᴛᴀʀᴛ ʏᴏᴜʀ ᴅᴀʏ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ 🌄 **",
         "**➠ ɢᴍ ᴅᴏsᴛ, ᴄᴏғғᴇᴇ/ᴛᴇᴀ ᴇᴍ ᴛɪsᴋᴜɴᴛᴀʀᴜ ☕🍵**",
         "**➠ ʙᴀʙʏ 8 ᴀᴠᴛᴜɴᴅɪ , ɴᴜᴠ  ɪᴘᴘᴀᴛɪ ᴅᴀᴀᴋᴀ ʟᴇᴠᴀʟᴇᴅᴜ 🕖**",
         "**➠ ᴏʏᴇᴇ ᴋᴜᴍʙᴀᴋᴀʀɴᴀ ɪɴᴋᴀ ᴇɴᴛᴀ sᴇᴘᴜ ᴘᴀᴅᴜᴋᴜɴᴛᴀᴠ... ☃️**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ʜᴀᴠᴇ ᴀ ɴɪᴄᴇ ᴅᴀʏ... 🌄**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʜᴀᴠᴇ ᴀ ɢᴏᴏᴅ ᴅᴀʏ... 🪴**",
         "**➠ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ ʙᴀʙʏ 😇**",
         "**➠ ᴛᴇʟᴀʀɪɴᴅᴏᴏ ᴍᴏᴡᴀ ᴄʜᴀᴛᴛɪɴɢ ᴄʜᴇsᴋᴜɴᴅʜᴀᴍ ʟᴇɢᴀᴠᴏɪ... 😵‍💫**",
         "**➠ ɴɪɢʜᴛ ᴀɴᴛᴀ ɢғ ᴛʜᴏ ᴍᴀᴛʟᴀᴅᴜᴛᴀᴅᴜ , ᴍᴏʀɴɪɴɢ ʟᴇᴠᴀɴᴇ ʟᴇᴠᴀᴠᴜ... 😏**",
         "**➠ ʙᴀʙʏ , ʟᴇɢᴜ ɪɴᴋᴀ ɢʀᴏᴜᴘ ʟᴏᴏ ᴀɴᴅᴀʀᴋɪ ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴡɪsʜ ᴄʜᴇʏ ... 🌟**",
         "**➠ ᴅᴀᴅᴅʏ ᴠɪᴅᴜ ɪᴘᴘᴀᴛɪ ᴅᴀᴀᴋᴀ ᴘᴀᴅᴜᴋᴜɴᴛᴜɴɴᴀᴅᴜ , sᴄʜᴏᴏʟ ᴋɪ ᴛɪᴍᴇ ᴀᴠᴛᴜɴᴅɪ... 🥲**",
         "**➠ ᴇɴᴛʜᴀ sᴇᴘᴜ ᴘᴀᴅᴜᴋᴜɴᴛᴀʀᴜ ᴀʏʏᴀ ʟᴇᴠᴀɴᴅɪ 🙆‍♀️ ... 😅**",
         "**➠ ɢᴍ ʙᴇsᴛɪᴇ, ʙʀᴇᴀᴋғᴀsᴛ ʜᴜᴀ ᴋʏᴀ... 🍳**",
        ]


@app.on_message(filters.command(["gntag", "tagmember" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")

    if message.reply_to_message and message.text:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ғᴏᴛ ᴛᴀɢɢɪɴɢ...")
    else:
        return await message.reply("/tagall ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴛʏᴘᴇ ʟɪᴋᴇ ᴛʜɪs / ʀᴇᴘʟʏ ᴀɴʏ ᴍᴇssᴀɢᴇ ɴᴇxᴛ ᴛɪᴍᴇ ʙᴏᴛ ᴛᴀɢɢɪɴɢ...")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["gmtag"], prefixes=["/", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("๏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴘs.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs. ")
    if chat_id in spam_chats:
        return await message.reply("๏ ᴘʟᴇᴀsᴇ ᴀᴛ ғɪʀsᴛ sᴛᴏᴘ ʀᴜɴɴɪɴɢ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass



@app.on_message(filters.command(["gmstop", "gnstop", "cancle"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("๏ ᴄᴜʀʀᴇɴᴛʟʏ ɪ'ᴍ ɴᴏᴛ ᴛᴀɢɢɪɴɢ ʙᴀʙʏ.")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("๏ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ʙᴀʙʏ, ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴛᴀɢ ᴍᴇᴍʙᴇʀs.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("๏ ᴍᴇɴᴛɪᴏɴ ᴘʀᴏᴄᴇss sᴛᴏᴘᴘᴇᴅ ๏")


