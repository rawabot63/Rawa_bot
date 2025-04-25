import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, ContextTypes, CommandHandler
from dotenv import load_dotenv

load_dotenv()

# توکن و آی‌دی ادمین از env
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# لیست شخصیت‌ها
characters = [
    "راوا", "جادُ", "ثریا (سامیر)", "سامبا", "سونیت", "سارینتاکار", "کاتاک ها",
    "ماسوتا", "خانم جینک", "سیربا", "زوبیر", "سامبارو", "موماترا", "ماساکار و هودیش",
    "زاگورا", "تالیس", "دیورا", "ماسین", "شومین", "سامانتی", "یوتا", "یودم",
    "میپار", "آندو", "سیناس کور", "روکو", "میوری", "تاجوتا", "انگیس", "خاکیس",
    "سالوادور", "سارا و آرتور", "جیمز", "پائول"
]

# ساخت کیبورد شخصیت‌ها
def build_characters_keyboard():
    keyboard = []
    for name in characters:
        keyboard.append([InlineKeyboardButton(name, callback_data=f"char_{name}")])
    keyboard.append([InlineKeyboardButton("🔙 بازگشت به منوی اصلی", callback_data="main_menu")])
    return InlineKeyboardMarkup(keyboard)

# نمایش منوی اصلی
def build_main_menu():
    keyboard = [
        [InlineKeyboardButton("👤 شخصیت‌های رمان", callback_data="shakhsiyatha")],
    ]
    return InlineKeyboardMarkup(keyboard)

# شروع ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text="سلام! به ربات راوا خوش اومدی 🌟",
        reply_markup=build_main_menu()
    )

# نمایش لیست شخصیت‌ها
async def show_characters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🌟 شخصیت مورد نظرت رو انتخاب کن:",
        reply_markup=build_characters_keyboard()
    )

# انتخاب یک شخصیت
async def character_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    character_name = query.data.replace("char_", "")
    await query.edit_message_text(
        text=f"📖 اطلاعات مربوط به «{character_name}» به‌زودی اضافه می‌شود.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 بازگشت به فهرست شخصیت‌ها", callback_data="shakhsiyatha")],
            [InlineKeyboardButton("🏠 بازگشت به منوی اصلی", callback_data="main_menu")]
        ])
    )

# بازگشت به منو
async def back_to_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        text="🏠 برگشتی به منوی اصلی",
        reply_markup=build_main_menu()
    )

# اجرای اصلی ربات
def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(show_characters, pattern="^shakhsiyatha$"))
    application.add_handler(CallbackQueryHandler(character_selected, pattern="^char_"))
    application.add_handler(CallbackQueryHandler(back_to_menu, pattern="^main_menu$"))

    print("ربات اجرا شد...")
    application.run_polling()

if __name__ == "__main__":
    main()
