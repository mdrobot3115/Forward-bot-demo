import os
import sys
import asyncio 
from database import db
from config import config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
from main import LOGGER, prefixes, AUTH_USERS

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
