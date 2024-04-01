from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from Bikash import config
from Bikash import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="❰ Commands❱",
                url=f"https://t.me/{BOT_USERNAME}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙ Bot settings ⚙", callback_data="settings_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 Channel 💖", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="💖 Group 💖", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 vijay sahu 📱", url=f"https://t.me/vijaysahu_2"
            )
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ❰ Add Your Group ❱ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="💖 Help 💖", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 Channel 💥", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="🥀 Group 💥", url=config.SUPPORT_GROUP
            )
        ],
        [           
            InlineKeyboardButton(
                text="📱 Vijay sahu 📱", url=f"https://t.me/vijaysahu_2"
            )
        ],
        [
            InlineKeyboardButton(
                text="♕ Owner ♕", user_id=OWNER
            )
        ]
     ]
    return buttons
