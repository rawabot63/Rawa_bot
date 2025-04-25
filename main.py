import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# فعال‌سازی لاگ‌ها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# تابع استارت با منوی دو ستونه (جای دکمه‌ها عوض شده)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    welcome_text = "🎉 به خانه‌ی راوا خوش آمدید 🌿\nاز بین گزینه‌های زیر، هر کدوم که دوست داشتی رو انتخاب کن:"

    # ستون سمت چپ (خلاصه داستان و ...)
    left_column = [
        InlineKeyboardButton("📖 خلاصه داستان", callback_data='intro'),
        InlineKeyboardButton("✍️ نویسنده رمان", callback_data='author'),
        InlineKeyboardButton("💬 جمله‌ی امروز راوا", callback_data='daily_quote'),
        InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data='audio_preview'),
        InlineKeyboardButton("❤️ شخصیت محبوبت کی بود؟", callback_data='fav_character'),
        InlineKeyboardButton("📩 ارتباط با نویسنده", callback_data='contact')
    ]

    # ستون سمت راست (شخصیت‌ها و گالری و ...)
    right_column = [
        InlineKeyboardButton("🧍‍♀️ شخصیت‌های رمان", callback_data='characters'),
        InlineKeyboardButton("🎨 تصویرگر", callback_data='illustrator'),
        InlineKeyboardButton("❓ چرا این رمان را بخوانم؟", callback_data='why_read'),
        InlineKeyboardButton("🖼 گالری تصاویر", callback_data='gallery'),
        InlineKeyboardButton("💢 شخصیت منفورت کی بود؟", callback_data='hate_character'),
        InlineKeyboardButton("📝 ثبت نظرات", callback_data='feedback')
    ]

    # جفت‌سازی دکمه‌ها
    paired_buttons = [[left, right] for left, right in zip(left_column, right_column)]

    # دکمه‌های بزرگ پایین
    large_buttons = [
        [InlineKeyboardButton("🖋 برای راوا یک جمله بنویس", callback_data='write_for_rawa')],
        [InlineKeyboardButton("🤝 همکاری با راوا", callback_data='collab')],
        [InlineKeyboardButton("📥 دریافت اثر", callback_data='download')]
    ]

    keyboard = paired_buttons + large_buttons
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# هندلر دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    data = query.data

    # پاسخ‌های اولیه
    responses = {
        'intro': "📖 خلاصه داستان: راوا داستانی‌ست درباره ...",
        'author': "✍️ نویسنده: اطلاعات به‌زودی افزوده می‌شود.",
        'daily_quote': "💬 جمله‌ی امروز راوا: «زندگی یعنی بلند شدن پس از هر سقوط.»",
        'audio_preview': "🔊 پیش‌نمایش صوتی: به‌زودی در دسترس قرار می‌گیرد.",
        'fav_character': "❤️ شخصیت محبوبت کی بود؟ لطفاً برام بنویس 🌟",
        'contact': "📩 پیامت رو بنویس، مستقیم به نویسنده می‌رسه ✉️",
        'characters': "🧍‍♀️ شخصیت‌های رمان: راوا، نادیا، حامد، ...",
        'illustrator': "🎨 تصویرگر: جوانه پیشکاری",
        'why_read': "❓ چون متفاوت، عمیق و الهام‌بخشه.",
        'gallery': "🖼 گالری تصاویر: به‌زودی فعال خواهد شد.",
        'hate_character': "💢 شخصیت منفورت کی بود؟ لطفاً با دلیل برام بگو!",
        'feedback': "📝 نظرت رو بنویس، خود نویسنده می‌خونه 🌟",
        'write_for_rawa': "🖋 جمله‌ات برای راوا رو بنویس، با افتخار منتشرش می‌کنیم.",
        'collab': "🤝 دوست داری همکاری کنی؟ بنویس بهم چی تو ذهنته!",
        'download': "📥 لینک دریافت اثر به‌زودی قرار می‌گیره."
    }

    await query.edit_message_text(responses.get(data, "❗ گزینه‌ی نامشخصی انتخاب شده."))

# راه‌اندازی ربات
if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")  # یا مستقیماً مقدار توکن

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()
