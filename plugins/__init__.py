from pyrogram import filters
from pyrogram import Client 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from main import LOGGER, prefixes, AUTH_USERS
from config import Config
import os
import sys
from translation import Translation

main_buttons = [[
        InlineKeyboardButton('📜 Support Group', url=''),
        InlineKeyboardButton('📢 Update Channel ', url='')
        ],[
        InlineKeyboardButton('❗️Help', callback_data='help') 
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

#==================Restart Function==================#

@Client.on_message(filters.private & filters.command(['cancel']) & filters.user(AUTH_USERS))
async def restart(client, message):
    await message.reply_text("**Process Cancelled Succefully !**")
    os.execl(sys.executable, sys.executable, *sys.argv)

#==================Callback Functions==================#

@Client.on_callback_query(filters.regex(r'^help'))
async def helpcb(bot, query):
    buttons = [[
            InlineKeyboardButton('💠 About 💠', callback_data='about'),
            InlineKeyboardButton('💠 Status 💠', callback_data='status'),
            ],[
            InlineKeyboardButton('💠 Settings 💠', callback_data='settings#main')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Translation.HELP_TXT,
        reply_markup=reply_markup)

@Client.on_callback_query(filters.regex(r'^back'))
async def back(bot, query):
    reply_markup = InlineKeyboardMarkup(main_buttons)
    await query.message.edit_text(
       reply_markup=reply_markup,
       text=Translation.START_TXT.format(
                query.from_user.first_name))

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    buttons = [[InlineKeyboardButton('• back', callback_data='help')]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Translation.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )
@Client.on_callback_query(filters.regex(r'^settings'))
async def settings_query(bot, query):
    buttons = [[
            InlineKeyboardButton('✚ Add bot ✚', callback_data='addbot')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await query.message.edit_text(
        text=Translation.ABOUT_TXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
    )
@Client.on_callback_query() 
async def cb_handler(bot, query):
    if query.data =="addbot":
     await query.message.delete()
     bot = await CLIENT.add_bot(bot, query)
     if bot != True: return
     await query.message.reply_text(
        "<b>bot token successfully added to db</b>",
        reply_markup=InlineKeyboardMarkup(buttons))
