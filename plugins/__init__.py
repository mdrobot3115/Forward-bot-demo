from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
        insert(int(message.chat.id))
        await message.reply_text(text =f"""
        Hello {message.from_user.first_name }
        __I'm an advanced forward bot. click /help__
        """,reply_to_message_id = message.message_id ,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Support 🇮🇳" ,url="https://t.me/VysakhXD"),
                 InlineKeyboardButton("⚡️ Updates", url="https://t.me/VysakhXD")],
                [InlineKeyboardButton("Help", callback_data="help")],
            ],
        )
        ) 
                 
@Client.on_message(filters.private & filters.command(["help])) 
async def help(client,message): 
        insert(int(message.chat.id))
        await message.reply_text(text =f"""
        __I can Forward message from one chat to another\nf"Available Commands are\n /forward to start forwarding__
        """
        
