import os
import sys
import asyncio 
from database import db
from config import config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaDocument
from main import LOGGER, prefixes, AUTH_USERS

main_buttons = [[
        InlineKeyboardButton('📜 Support Group', url='https://t.me/venombotupdates'),
        InlineKeyboardButton('📢 Update Channel ', url='https://t.me/venombotsupport')
        ],[
        InlineKeyboardButton('❗️Help', callback_data='help') 
        ],[
        
]]

#===================Start Function===================#

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
    user = message.from_user
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await client.send_message(
        chat_id=message.chat.id,
        reply_markup=reply_markup,
        text=Translation.START_TXT.format(
                message.from_user.first_name))

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
