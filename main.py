import os
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)

# مسیرهای فایل‌ها
BASE_DIR = "data"
SUMMARY_FILE = os.path.join(BASE_DIR, "kholase.txt")
CHARACTERS_DIR = os.path.join(BASE_DIR, "shakhsiyatha")

# شخصیت‌ها (برای دکمه‌سازی)
characters = [
    "راوا", "جادُ", "ثریا (سامیر)", "سامبا", "سونیت", "سارینتاکار", "کاتاک ها",
    "ماسوتا", "خانم جینک", "سیربا", "زوبیر", "سامبارو", "موماترا",
    "ماساکار و هودیش", "زاگورا", "تالیس", "دیورا", "ماسین", "شومین",
    "سامانتی", "یوتا", "یودم", "میپار", "آندو", "سیناس کور", "روکو",
    "میوری", "تاجوتا", "انگیس", "خاکیس", "سالوادور", "سارا و آرتور", "جیمز", "پائول"
]

# تابع برای خواندن فایل متنی
def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return "خطا در بارگذاری محتوا."

# دکمه برگشت‌ها
def back_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 بازگشت به شخصیت‌ها", callback_data="back_to_characters")],
        [InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")]
    ])

# منوی اصلی
def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("👤 شخصیت‌های رمان", callback_data="characters"),
            InlineKeyboardButton("📖 خلاصه داستان", callback_data="summary")
        ],
        [
            InlineKeyboardButton("🎨 تصویرگر", callback_data="designer"),
            InlineKeyboardButton("✍️ نویسنده رمان", callback_data="author")
        ],
        [
            InlineKeyboardButton("❓ چرا این رمان را بخوانم؟", callback_data="why_read"),
            InlineKeyboardButton("🗣 جمله‌ی امروز راوا", callback_data="quote")
        ],
        [
            InlineKeyboardButton("🖼 گالری تصاویر", callback_data="gallery"),
            InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data="audio")
        ],
        [
            InlineKeyboardButton("💔 شخصیت منفورت کی بود؟", callback_data="hated_character"),
            InlineKeyboardButton("💖 شخصیت محبوبت کی بود؟", callback_data="loved_character")
        ],
        [
            InlineKeyboardButton("📝 ثبت نظرات", callback_data="comments"),
            InlineKeyboardButton("✉️ ارتباط با نویسنده", callback_data="contact")
        ],
        [InlineKeyboardButton("🧠 برای راوا یک جمله بنویس", callback_data="write_to_rawa")],
        [InlineKeyboardButton("🤝 همکاری با راوا", callback_data="cooperation")],
        [InlineKeyboardButton("📥 دریافت اثر", callback_data="download")]
    ]
    return InlineKeyboardMarkup(keyboard)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به خانه‌ی راوا خوش آمدید",
        reply_markup=main_menu()
    )

# هندلر کلی دکمه‌ها
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "summary":
        text = read_file(SUMMARY_FILE)
        await query.edit_message_text(text=text, reply_markup=back_buttons())
    elif data == "characters":
        buttons = [[InlineKeyboardButton(name, callback_data=f"char_{i}")] for i, name in enumerate(characters)]
        await query.edit_message_text("شخصیتی را انتخاب کن:", reply_markup=InlineKeyboardMarkup(buttons))
    elif data.startswith("char_"):
        index = int(data.split("_")[1])
        name = characters[index]
        filename = f"{name.split()[0].lower()}.txt"
        filepath = os.path.join(CHARACTERS_DIR, filename)
        text = read_file(filepath)
        await query.edit_message_text(text=text, reply_markup=back_buttons())
    elif data == "back_to_characters":
        buttons = [[InlineKeyboardButton(name, callback_data=f"char_{i}")] for i, name in enumerate(characters)]
        await query.edit_message_text("شخصیتی را انتخاب کن:", reply_markup=InlineKeyboardMarkup(buttons))
    elif data == "main_menu":
        await query.edit_message_text("به خانه‌ی راوا خوش آمدید", reply_markup=main_menu())
    else:
        await query.answer("این بخش هنوز فعال نشده 🌱")

# راه‌اندازی اپلیکیشن
if __name__ == '__main__':
    import asyncio

    TOKEN = os.getenv("TOKEN")  # اسم متغیر در Render

    async def main():
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CallbackQueryHandler(handle_buttons))
        await app.run_polling()

    asyncio.run(main())
