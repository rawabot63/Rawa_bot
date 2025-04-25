import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# فعال‌سازی لاگ‌ها برای بررسی خطاها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# پیام خوش‌آمدگویی و منو
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("📖 خلاصه داستان", callback_data='intro'),
            InlineKeyboardButton("🎨 تصویرگر", callback_data='illustrator')
        ],
        [
            InlineKeyboardButton("🗣 جمله‌ی امروز راوا", callback_data='quote'),
            InlineKeyboardButton("✍️ نویسنده رمان", callback_data='author')
        ],
        [
            InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data='audio'),
            InlineKeyboardButton("👤 شخصیت‌های رمان", callback_data='characters')
        ],
        [
            InlineKeyboardButton("💖 شخصیت محبوبت کی بود؟", callback_data='fav_character'),
            InlineKeyboardButton("💔 شخصیت منفورت کی بود؟", callback_data='hated_character')
        ],
        [
            InlineKeyboardButton("📷 گالری تصاویر", callback_data='gallery'),
            InlineKeyboardButton("❓ چرا این رمان را بخوانم؟", callback_data='why_read')
        ],
        [
            InlineKeyboardButton("📝 ثبت نظرات", callback_data='feedback'),
            InlineKeyboardButton("✉️ ارتباط با نویسنده", callback_data='contact')
        ],
        [InlineKeyboardButton("🖋 برای راوا یک جمله بنویس", callback_data='write_to_rava')],
        [InlineKeyboardButton("🤝 همکاری با راوا", callback_data='cooperate')],
        [InlineKeyboardButton("📥 دریافت اثر", callback_data='download')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_text = "🌟 به خانه‌ی راوا خوش آمدید 🌟\n\nیکی از گزینه‌های زیر رو انتخاب کن:"
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# مدیریت کلیک روی دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == 'intro':
        await query.edit_message_text("📖 خلاصه داستان: راوا داستانی‌ست درباره ...")
    elif data == 'author':
        await query.edit_message_text("✍️ نویسنده: این رمان توسط ... نوشته شده است.")
    elif data == 'illustrator':
        await query.edit_message_text("🎨 تصویرگر: طراحی‌های کتاب توسط جوانه پیشکاری انجام شده‌اند.")
    elif data == 'quote':
        await query.edit_message_text("🗣 جمله امروز راوا: «هرکسی درون خودش راوایی دارد...»")
    elif data == 'audio':
        await query.edit_message_text("🔊 پیش‌نمایش صوتی به‌زودی در دسترس قرار می‌گیرد.")
    elif data == 'characters':
        await query.edit_message_text("👤 شخصیت‌ها: راوا، نادیا، حامد و ...")
    elif data == 'fav_character':
        await query.edit_message_text("💖 کدوم شخصیت داستان رو دوست داشتی؟ چرا؟ برام بنویس 🌟")
    elif data == 'hated_character':
        await query.edit_message_text("💔 کدوم شخصیت رو اصلاً دوست نداشتی؟ دلیلش چیه؟ برام بفرست.")
    elif data == 'gallery':
        await query.edit_message_text("📷 گالری تصاویر به‌زودی فعال خواهد شد!")
    elif data == 'why_read':
        await query.edit_message_text("❓ چرا این رمان را بخوانی؟ چون متفاوت است، چون الهام‌بخش است ...")
    elif data == 'feedback':
        await query.edit_message_text("📝 نظر خودت رو بنویس و برای من بفرست 🌟")
    elif data == 'contact':
        await query.edit_message_text("✉️ پیام یا پیشنهادت رو بنویس تا به نویسنده برسه.")
    elif data == 'write_to_rava':
        await query.edit_message_text("🖋 برای راوا یک جمله بنویس و برام بفرست. شاید در نسخه بعدی کتابت بیاد 😉")
    elif data == 'cooperate':
        await query.edit_message_text("🤝 دوست داری با راوا همکاری کنی؟ نوع همکاری رو بنویس تا باهات تماس بگیریم.")
    elif data == 'download':
        await query.edit_message_text("📥 برای دریافت اثر نسخه نهایی، به این لینک مراجعه کن: ...")

# اجرای ربات
if __name__ == '__main__':
    TOKEN = os.environ.get("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))

    application.run_polling()
