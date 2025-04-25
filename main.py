import logging
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    ApplicationBuilder,
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)
from dotenv import load_dotenv

# بارگذاری متغیرها از فایل .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# تنظیمات لاگ‌گیری
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# هندلر شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📖 خلاصه داستان", callback_data="summary"),
            InlineKeyboardButton("🧑‍🤝‍🧑 شخصیت‌ها", callback_data="characters"),
        ],
        [
            InlineKeyboardButton("🖼 گالری تصاویر", callback_data="gallery"),
            InlineKeyboardButton("📝 ثبت نظرات", callback_data="feedback"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("به راوابات خوش اومدی! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

# پاسخ به دکمه‌ها
async def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "summary":
        await query.edit_message_text("اینجا خلاصه‌ای از داستان نمایش داده میشه...")
    elif data == "characters":
        await query.edit_message_text("اینجا لیستی از شخصیت‌های داستان راوا رو می‌تونی ببینی...")
    elif data == "gallery":
        await query.edit_message_text("اینجا قراره گالری تصاویر کتاب رو ببینی...")
    elif data == "feedback":
        await query.edit_message_text("نظرتو درباره‌ی کتاب برامون بنویس!")

# شروع ربات
def main():
    if not TOKEN:
        print("❌ خطا: توکن یافت نشد. لطفاً در فایل .env مقدار BOT_TOKEN را تنظیم کنید.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
