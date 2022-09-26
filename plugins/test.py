import os
import re 
import sys
import asyncio 
import logging 

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message 
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from pyrogram.errors import FloodWait 
from config import Config
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)]\[buttonurl:/{0,2}(.+?)(:same)?])")
BOT_TOKEN_TEXT = "<b>1) create a bot using @BotFather\n2) Then you will get a message with bot token\n3) Forward that message to me</b>"
SESSION_STRING_SIZE = 351 

class Client(Methods):
def __init__(
   self.api_id = API_ID
   self.api_hash = API_HASH

async def authorize(self) -> User:
        if self.bot_token:
            return await self.sign_in_bot(self.bot_token

