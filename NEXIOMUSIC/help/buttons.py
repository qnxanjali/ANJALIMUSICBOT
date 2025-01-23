from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

import config
from NEXIOMUSIC import app

class BUTTONS(object):
    MBUTTON = [
        [
            InlineKeyboardButton("˹ ᴧηᴊᴧʟɪ ˼", url="https://t.me/AnjaliOwnerBot")
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    SBUTTON = [
 
        [
            InlineKeyboardButton("ᴧηᴊᴧʟɪ ηєᴛᴡσʀᴋ", url="https://t.me/SANATANI_TECH"),
        ],
        [
            
            InlineKeyboardButton("ᴧηᴊᴧʟɪ ᴡσʀʟᴅ", url="https://t.me/ANJALIWORLD"),
        ],
        [
            InlineKeyboardButton("ᴄʜᴧᴛ ɢᴄ", url="https://t.me/+b1gc4qrvfLZlNGI1"),
       
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
    
    ABUTTON = [
        [
            InlineKeyboardButton("ᴧʙσυᴛ", url="https://t.me/qnxanjaliabout"),
            InlineKeyboardButton("ʜєʟᴘ | ɪηғσ", callback_data="settings_back_helper"),
        ],
        [
            InlineKeyboardButton("ʙᴧsɪᴄ ɢυɪᴅє", callback_data="ABOUT_BACK HELP_GUIDE"),
            InlineKeyboardButton("ᴅσηᴧᴛє", callback_data="ABOUT_BACK HELP_DONATE"),
        ],
        [
            InlineKeyboardButton("⌯ ʙᴧᴄᴋ ᴛσ ʜσϻє ⌯", callback_data="settingsback_helper"),
            
        ]
        ]
