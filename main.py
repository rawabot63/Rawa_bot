import os
import asyncio
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

CHARACTER_DIR = "data/shakhsiyatha"

character_files = {
    "راوا": "rawa.txt",
    "جادُ": "jadu.txt",
    "ثریا (سامیر)": "samir.txt",
    "سامبا": "samba.txt",
    "سونیت": "sonit.txt",
    "سارینتاکار": "sarin.txt",
    "کاتاک ها": "katak.txt",
    "ماسوتا": "masota.txt",
    "خانم جینک": "jink.txt",
    "سیربا": "sirba.txt",
    "زوبیر": "zubir.txt",
    "سامبارو": "sambaro.txt",
    "موماترا": "momatra.txt",
    "ماساکار و هودیش": "masakar.txt",
    "زاگورا": "zagora.txt",
    "تالیس": "talis.txt",
    "دیورا": "divora.txt",
    "ماسین": "masin.txt",
    "شومین": "shomin.txt",
    "سامانتی": "samanti.txt",
    "یوتا": "yuta.txt",
    "یودم": "yodam.txt",
    "میپار": "mipar.txt",
    "آندو": "ando.txt",
    "سیناس کور": "sinas.txt",
    "روکو": "roko.txt",
    "میوری": "miori.txt",
    "تاجوتا": "tajota.txt",
    "انگیس": "engis.txt",
    "خاکیس": "khakis.txt",
    "سالوادور": "salvador.txt",
    "سارا و آرتور": "sara_arthur.txt",
    "جیمز": "james.txt",
    "پائول": "paul.txt",
}

def build_character_keyboard():
    keyboard = [
        [InlineKeyboardButton(name, callback_data=f"character_{file}")]
        for name, file in character_files.items()
    ]
    return InlineKeyboardMarkup(keyboard)

def build_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 بازگشت به فهرست شخصیت‌ها", callback_data="back_to_list")],
        [InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")]
    ])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! از فهرست زیر یکی از شخصیت‌های داستان را انتخاب کن:",
        reply_markup=build_character_keyboard()
    )

async def character_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data.startswith("character_"):
        filename = data.replace("character_", "")
        path = os.path.join(CHARACTER_DIR, filename)

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
            await query.message.edit_text(
                text=text,
                reply_markup=build_back_keyboard()
            )
        else:
            await query.message.edit_text("متن این شخصیت پیدا نشد.")

    elif data == "back_to_list":
        await query.message.edit_text(
            "دوباره یکی از شخصیت‌ها رو انتخاب کن:",
            reply_markup=build_character_keyboard()
        )
    elif data == "main_menu":
        await query.message.edit_text("بازگشت به منوی اصلی 🌟 (در حال توسعه...)")

async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(character_handler))

    print("ربات در حال اجراست...")
    await app.run_polling()

# حل مشکل event loop در رندر:
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError as e:
        if "already running" in str(e):
            loop = asyncio.get_event_loop()
            loop.create_task(main())
            loop.run_forever()
        else:
            raise
