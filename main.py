import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# فعال‌سازی لاگ‌ها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# پیام استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("📖 خلاصه داستان", callback_data='intro'),
            InlineKeyboardButton("👤 شخصیت‌های رمان", callback_data='characters')
        ],
        [
            InlineKeyboardButton("✍️ نویسنده رمان", callback_data='author'),
            InlineKeyboardButton("🎨 تصویرگر", callback_data='illustrator')
        ],
        [
            InlineKeyboardButton("🗣 جمله‌ی امروز راوا", callback_data='daily_quote'),
            InlineKeyboardButton("❓ چرا این رمان را بخوانم؟", callback_data='why_read')
        ],
        [
            InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data='audio_preview'),
            InlineKeyboardButton("🖼 گالری تصاویر", callback_data='gallery')
        ],
        [
            InlineKeyboardButton("💖 شخصیت محبوبت کی بود؟", callback_data='fav_character'),
            InlineKeyboardButton("💔 شخصیت منفورت کی بود؟", callback_data='least_fav_character')
        ],
        [
            InlineKeyboardButton("✉️ ارتباط با نویسنده", callback_data='contact'),
            InlineKeyboardButton("📝 ثبت نظرات", callback_data='feedback')
        ],
        [InlineKeyboardButton("🖋 برای راوا یک جمله بنویس", callback_data='write_to_rawa')],
        [InlineKeyboardButton("🤝 همکاری با راوا", callback_data='collab')],
        [InlineKeyboardButton("📥 دریافت اثر", callback_data='get_book')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🌟 به خانه‌ی راوا خوش آمدید 🌟", reply_markup=reply_markup)

# مدیریت دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data
    responses = {
        'intro': "📖 خلاصه داستان: راوا داستانی‌ست درباره...",
        'characters': "👤 شخصیت‌های رمان: راوا، نادیا، حامد...",
        'author': "✍️ نویسنده رمان: [نام نویسنده] است...",
        'illustrator': "🎨 تصویرگر: جوانه پیشکاری",
        'daily_quote': "🗣 جمله‌ی امروز راوا: «زندگی، فصلِ آزمونِ صبر است.»",
        'why_read': "❓ این رمان رو بخون چون...",
        'audio_preview': "🔊 پیش‌نمایش صوتی به‌زودی فعال می‌شود!",
        'gallery': "🖼 گالری تصاویر در دست ساخت است...",
        'fav_character': "💖 شخصیت محبوبت رو برام بنویس!",
        'least_fav_character': "💔 کدوم شخصیت رو دوست نداشتی؟",
        'contact': "✉️ پیام یا پیشنهادت رو بنویس تا به نویسنده برسه.",
        'feedback': "📝 نظر خودت رو بنویس و برام بفرست 🌟",
        'write_to_rawa': "🖋 یه جمله برای راوا بنویس، شاید توی ربات نمایش داده شد!",
        'collab': "🤝 دوست داری چجوری با راوا همکاری کنی؟ بنویس برام.",
        'get_book': "📥 برای دریافت اثر، لطفاً لینک یا روش خرید رو دنبال کن (به‌زودی)."
    }

    await query.edit_message_text(responses.get(data, "گزینه نامعتبر است."))

# راه‌اندازی ربات
if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
