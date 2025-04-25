# فایل اصلی بوت: main.py (یا هر اسمی که داری)

import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# فعال‌سازی لاگ‌ها برای دیباگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# هندلر استارت با منوی سفارشی‌شده
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = "🎉 به خانه‌ی راوا خوش آمدید 🌿\nاز بین گزینه‌های زیر، هر کدوم که دوست داشتی رو انتخاب کن:"

    right_column = [
        InlineKeyboardButton("📖 خلاصه داستان", callback_data='intro'),
        InlineKeyboardButton("✍️ نویسنده رمان", callback_data='author'),
        InlineKeyboardButton("💬 جمله‌ی امروز راوا", callback_data='daily_quote'),
        InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data='audio_preview'),
        InlineKeyboardButton("❤️ شخصیت محبوبت کی بود؟", callback_data='fav_character'),
        InlineKeyboardButton("📩 ارتباط با نویسنده", callback_data='contact')
    ]

    left_column = [
        InlineKeyboardButton("🧍‍♀️ شخصیت‌های رمان", callback_data='characters'),
        InlineKeyboardButton("🎨 تصویرگر", callback_data='illustrator'),
        InlineKeyboardButton("❓ چرا این رمان را بخوانم؟", callback_data='why_read'),
        InlineKeyboardButton("🖼 گالری تصاویر", callback_data='gallery'),
        InlineKeyboardButton("💢 شخصیت منفورت کی بود؟", callback_data='hate_character'),
        InlineKeyboardButton("📝 ثبت نظرات", callback_data='feedback')
    ]

    # جفت‌کردن دکمه‌های دو ستونه
    paired_buttons = [[right, left] for right, left in zip(right_column, left_column)]

    # دکمه‌های بزرگ پایین
    large_buttons = [
        [InlineKeyboardButton("🖋 برای راوا یک جمله بنویس", callback_data='write_for_rawa')],
        [InlineKeyboardButton("🤝 همکاری با راوا", callback_data='collab')],
        [InlineKeyboardButton("📥 دریافت اثر", callback_data='download')]
    ]

    keyboard = paired_buttons + large_buttons
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)


# هندلر کلی دکمه‌ها (فعلاً ساده برای تست)
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"شما این گزینه رو انتخاب کردید: {query.data}")

# اجرای ربات
if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")  # در رندر یا گیت‌هاب ست شده
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
