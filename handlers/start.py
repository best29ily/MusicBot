from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import sys
from threading import Thread
from pyrogram import idle, filters
from pyrogram.handlers import MessageHandler
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
       f"""🙃 Hi {message.from_user.first_name}!

✨ I am ᴜɴᴄʟᴇ ᴍᴜᴛʜᴜ Music Player. 

🥳 I can play music in your Telegram Group's Voice Chat😉

⚜️ Use these buttons below to know more. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📔 help 📔", url="https://realsht.mobi/ref/MMntRo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group 💬", url="https://realsht.mobi/qkH4G"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel 📣", url="https://realsht.mobi/H4lKz"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ᴜɴᴄʟᴇ ᴍᴜᴛʜᴜ I'm Working!!!\nUse me in Inline to search for a YouTube Video/Music. \n**Happy Streaming**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Search 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Close ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
