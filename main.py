from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")  # از محیط بخونه

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📸 گالری تصاویر", callback_data='gallery')],
        # اینجا بقیه دکمه‌ها رو اضافه می‌کنی
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("به ربات راوا خوش اومدی! یکی از گزینه‌ها رو انتخاب کن:", reply_markup=reply_markup)

def gallery_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    images = [
        "https://i.ibb.co/YBQWWmL/sample1.jpg",
        "https://i.ibb.co/Y3p8XtR/sample2.jpg",
        "https://i.ibb.co/NZhJgkS/sample3.jpg"
    ]

    media = [InputMediaPhoto(url) for url in images]
    context.bot.send_media_group(chat_id=query.message.chat_id, media=media)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(gallery_handler, pattern='^gallery$'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
