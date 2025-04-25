from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# لیست شخصیت‌ها
characters = [
    "راوا", "جادُ", "ثریا (سامیر)", "سامبا", "سونیت", "سارینتاکار", "کاتاک ها", "ماسوتا",
    "خانم جینک", "سیربا", "زوبیر", "سامبارو", "موماترا", "ماساکار و هودیش", "زاگورا",
    "تالیس", "دیورا", "ماسین", "شومین", "سامانتی", "یوتا", "یودم", "میپار", "آندو", "سیناس کور",
    "روکو", "میوری", "تاجوتا", "انگیس", "خاکیس", "سالوادور", "سارا و آرتور", "جیمز", "پائول"
]

# هندلر شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "به ربات رسمی رمان راوا خوش اومدی 🌱\n\nاز منوی زیر یکی از گزینه‌ها رو انتخاب کن 👇"

    keyboard = [
        [
            InlineKeyboardButton("📘 خلاصه داستان", callback_data="kholase"),
            InlineKeyboardButton("✍️ نویسنده رمان", callback_data="nevisande"),
        ],
        [
            InlineKeyboardButton("💬 جمله‌ی امروز راوا", callback_data="jomle"),
            InlineKeyboardButton("🔊 پیش‌نمایش صوتی", callback_data="audio_preview"),
        ],
        [
            InlineKeyboardButton("🤔 شخصیت محبوبت کی بود؟", callback_data="fav_character"),
            InlineKeyboardButton("📩 ارتباط با نویسنده", callback_data="contact_writer"),
        ],
        [
            InlineKeyboardButton("🧙‍♀️ شخصیت‌های رمان", callback_data="shakhsiyat_ha"),
            InlineKeyboardButton("🎨 تصویرگر", callback_data="tasvirgar"),
        ],
        [
            InlineKeyboardButton("❓ چرا این رمان رو بخونم؟", callback_data="chera"),
            InlineKeyboardButton("🖼 گالری تصاویر", callback_data="gallery"),
        ],
        [
            InlineKeyboardButton("😤 شخصیت منفورت کی بود؟", callback_data="hate_character"),
            InlineKeyboardButton("📝 ثبت نظرات", callback_data="feedback"),
        ],
        [
            InlineKeyboardButton("✏️ برای راوا یک جمله بنویس", callback_data="write_jomle")
        ],
        [
            InlineKeyboardButton("🤝 همکاری با راوا", callback_data="hamkari"),
        ],
        [
            InlineKeyboardButton("📥 دریافت اثر", callback_data="get_book")
        ],
    ]

    await update.message.reply_text(welcome_text, reply_markup=InlineKeyboardMarkup(keyboard))

# هندلر دکمه‌ها
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "shakhsiyat_ha":
        character_buttons = [[InlineKeyboardButton(name, callback_data=f"char_{name}")] for name in characters]
        await query.edit_message_text("شخصیت مورد نظرت رو انتخاب کن:", reply_markup=InlineKeyboardMarkup(character_buttons))
    elif data.startswith("char_"):
        name = data[5:]
        await query.edit_message_text(f"🔹 توضیحی درباره‌ی {name} هنوز اضافه نشده.\n(به‌زودی فعال میشه!)", 
                                      reply_markup=InlineKeyboardMarkup([
                                          [InlineKeyboardButton("🔙 بازگشت به فهرست شخصیت‌ها", callback_data="shakhsiyat_ha")],
                                          [InlineKeyboardButton("🏠 بازگشت به منوی اصلی", callback_data="back_to_menu")]
                                      ]))
    elif data == "back_to_menu":
        await start(update, context)
    else:
        await query.edit_message_text("این بخش هنوز راه‌اندازی نشده 😉")

# راه‌اندازی بات
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("Bot started...")
    app.run_polling()

if __name__ == '__main__':
    main()
