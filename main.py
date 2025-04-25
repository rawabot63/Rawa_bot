from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import CallbackContext

import os

# مسیر فایل‌های شخصیت‌ها
CHARACTER_DIR = "data/shakhsiyatha"

# لیست شخصیت‌ها و نام فایل‌ها
characters = [
    ("راوا", "rawa"),
    ("جادُ", "jado"),
    ("ثریا (سامیر)", "soraya"),
    ("سامبا", "samba"),
    ("سونیت", "sonit"),
    ("سارینتاکار", "sarintakar"),
    ("کاتاک ها", "katakha"),
    ("ماسوتا", "masota"),
    ("خانم جینک", "jink"),
    ("سیربا", "sirba"),
    ("زوبیر", "zobir"),
    ("سامبارو", "sambaro"),
    ("موماترا", "momatra"),
    ("ماساکار و هودیش", "masakar_hoodish"),
    ("زاگورا", "zagora"),
    ("تالیس", "talis"),
    ("دیورا", "divora"),
    ("ماسین", "masin"),
    ("شومین", "shomin"),
    ("سامانتی", "samanti"),
    ("یوتا", "yota"),
    ("یودم", "yodam"),
    ("میپار", "mipar"),
    ("آندو", "ando"),
    ("سیناس کور", "sinas"),
    ("روکو", "roko"),
    ("میوری", "miori"),
    ("تاجوتا", "tajota"),
    ("انگیس", "angis"),
    ("خاکیس", "khakis"),
    ("سالوادور", "salvador"),
    ("سارا و آرتور", "sara_arthur"),
    ("جیمز", "james"),
    ("پائول", "paul")
]

def show_characters_menu(update: Update, context: CallbackContext):
    keyboard = []
    for title, filekey in characters:
        keyboard.append([InlineKeyboardButton(text=title, callback_data=f"char_{filekey}")])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.callback_query.message.edit_text("شخصیت‌های رمان:", reply_markup=reply_markup)

def character_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    data = query.data

    if data.startswith("char_"):
        filekey = data.replace("char_", "")
        filepath = os.path.join(CHARACTER_DIR, f"{filekey}.txt")

        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        else:
            text = "❌ متن این شخصیت پیدا نشد."

        keyboard = [
            [InlineKeyboardButton("🔙 بازگشت به فهرست شخصیت‌ها", callback_data="back_to_characters")],
            [InlineKeyboardButton("🏠 بازگشت به منوی اصلی", callback_data="main_menu")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.edit_text(text=text, reply_markup=reply_markup)

    elif data == "back_to_characters":
        show_characters_menu(update, context)

# توی dispatcher این هندلرها رو ثبت کن
dispatcher.add_handler(CallbackQueryHandler(character_callback, pattern="^(char_|back_to_characters)$"))
