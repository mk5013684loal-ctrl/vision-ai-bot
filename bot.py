from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

 BOT_TOKEN = "8927436948:AAHhHwuFph3qupGJDyvXR5MG0Szi9St--6Q"

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال 🔥")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, reply))

print("Bot Started")

app.run_polling()
