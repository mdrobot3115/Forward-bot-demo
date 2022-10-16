#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 


from pyrogram import filters
from pyrogram import Client as ace
from pyrogram.types import Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import time
import os

def custom_caption(msg, caption):
  if msg.media:
    if (msg.video or msg.document or msg.audio or msg.photo):
      media = getattr(msg, msg.media.value, None)
      if media:
        file_name = getattr(media, 'file_name', '')
        file_size = getattr(media, 'file_size', '')
        fcaption = getattr(msg, 'caption', '')
        if fcaption:
          fcaption = fcaption.html
        if caption:
          return caption.format(filename=file_name, size=get_size(file_size), caption=fcaption)
        return fcaption
  return None

def get_size(size):
  units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
  size = float(size)
  i = 0
  while size >= 1024.0 and i < len(units):
     i += 1
     size /= 1024.0
  return "%.2f %s" % (size, units[i]) 


@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("ace", prefixes=prefixes)
)
async def forward(bot: ace , m: Message):
    msg = await bot.ask(m.chat.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat.id
    msg1 = await bot.ask(m.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.ask(m.chat.id, "**Send Ending Message from same chat**")
   # print(msg1.forward_from_message_id, msg1.forward_from_chat.id, msg1.forward_from_message_id)
    i_chat = msg1.forward_from_chat.id
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id)+1
    await m.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file')
    try:
        for i in range(s_msg, f_msg):
            try:
                await bot.copy_message(
                    chat_id= t_chat,
                    from_chat_id= i_chat,
                    message_id= i,
                    caption=CAPTION
                )
                time.sleep(2)
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done Forwarding")
