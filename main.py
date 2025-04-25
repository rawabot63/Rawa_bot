import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

import os

# فعال‌سازی لاگ‌ها برای بررسی خطاها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# دستورات شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("📖 معرفی داستان", callback_data='intro')],
        [InlineKeyboardButton("👤 شخصیت‌ها", callback_data='characters')],
        [InlineKeyboardButton("🖼 گالری تصاویر", callback_data='gallery')],
        [InlineKeyboardButton("📝 ثبت نظرات", callback_data='feedback')],
        [InlineKeyboardButton("✉️ ارسال پیام", callback_data='contact')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("سلام! به ربات راوا خوش اومدی 🌟\nیکی از گزینه‌های زیر رو انتخاب کن:", reply_markup=reply_markup)

# مدیریت دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == 'intro':
        await query.edit_message_text("📖 خلاصه داستان: راوا داستانی‌ست درباره ...")
    elif data == 'characters':
        await query.edit_message_text("👤 شخصیت‌ها: راوا، نادیا، حامد ...")
    elif data == 'gallery':
        await query.edit_message_text("🖼 گالری به‌زودی فعال خواهد شد!")
    elif data == 'feedback':
        await query.edit_message_text("📝 نظر خودت رو بنویس و برای من بفرست 🌟")
    elif data == 'contact':
        await query.edit_message_text("✉️ پیام یا پیشنهادت رو بنویس تا به نویسنده برسه.")

# راه‌اندازی ربات
if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
