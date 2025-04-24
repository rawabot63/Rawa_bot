from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 توکن رباتت رو اینجا بذار
TOKEN = "7784599888:AAGe3eb5XazFkmSwXpzFOoepRidtLi1n1u4"

# 📌 دستور start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من راوا هستم 🤖\nمی‌خوای درباره‌ی داستان بدونی؟ فقط ازم بپرس!")

# 💬 واکنش به هر پیام متنی معمولی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    # اینجا می‌تونی هوشمندش کنی یا به ربات شخصیت راوا وصل کنی
    reply = f"تو گفتی: «{user_message}»\nولی فعلاً من دارم تمرین می‌کنم که بهتر پاسخ بدم :)"
    await update.message.reply_text(reply)

# ▶️ اجرای اصلی ربات
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # اضافه کردن هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرای ربات
    app.run_polling()

if __name__ == "__main__":
    main()
