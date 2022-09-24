#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 


from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import time
import os 
import os 
import os 
import os 

@Client.on_message(filters.command('forward') & filters.user(AUTH_USERS))
async def forward(bot, message):
    msg = await bot.ask(message.chat.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat
    msg1 = await bot.ask(message.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.ask(message.chat.id, "**Send Ending Message from same chat**")
   # print(msg1.forward_from_message_id, msg1.forward_from_chat.id, msg1.forward_from_message_id)
    i_chat = msg1.forward_from_chat
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id)+1
    await message.reply_text('Your Current settings are:\n\n➥ From Chat:')
    try:
        for i in range(s_msg, f_msg):
            try:
                await bot.copy_message(
                    chat_id= t_chat,
                    from_chat_id= i_chat,
                    message_id= i 
                )
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await message.reply_text(str(e))
    await message.reply_text("🎉 ғᴏʀᴡᴀᴅɪɴɢ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
