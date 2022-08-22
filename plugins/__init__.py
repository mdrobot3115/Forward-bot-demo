from pyrogram import filters
from pyrogram import Client as ace
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys


@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("start", prefixes=prefixes)
)
async def Start_msg(bot: ace , m: Message):
    await bot.send_photo(
    m.chat.id,
    photo="https://telegra.ph/file/d77a3767a8d58da76f2df.jpg",
    caption = f"**Good Morning [{m.from_user.first_name}](tg://user?id={m.from_user.id})✨️**\n" +
    f"**I'm an advanced forward bot with some useful features!**" +
    f"\n**Check /help menu to know more 😼**",
    # parse_mode="md",
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("❤ Support", url="https://t.me/VysakhXD"),
             InlineKeyboardButton("⚡️ Updates", url="https://t.me/VysakhXD")],
            [InlineKeyboardButton("❓️ Help ❓️", callback_data="help")],
        ]
    )
    )

@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("help", prefixes=prefixes)
)
async def help_msg(bot: ace , m: Message):   
    await bot.send_message(
        m.chat.id,
        f"**!/usr/bin/env python \n(c) ACE**" +
        f"\n\nI can Forward message from one chat to another\n"+
        f"Available Commands are :"+
        f"\n\n/forward to start forwarding\n/log - To get Log file\n/restart - To Restart the bot"
    )

@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("cancel", prefixes=prefixes)
)
async def restart_handler(_, m):
    await m.reply_text("Forwarding stopped", True)
    os.execl(sys.executable, sys.executable, *sys.argv)

@ace.on_message(
    filters.chat(AUTH_USERS) & filters.private &
    filters.incoming & filters.command("log", prefixes=prefixes)
)
async def log_msg(bot: ace , m: Message):   
    await bot.send_document(m.chat.id, "log.txt")
