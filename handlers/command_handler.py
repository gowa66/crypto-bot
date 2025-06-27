# handlers/command_handler.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("💰 Get Crypto Price", callback_data="get_price"),
        InlineKeyboardButton("📊 Moving Averages", callback_data="moving_avg")
    ], [
        InlineKeyboardButton("🔔 Set Price Alert", callback_data="set_alert"),
        InlineKeyboardButton("🖼️ Price Chart", callback_data="price_chart")
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome to CryptoBot!\n\nSelect an option:",
        reply_markup=reply_markup
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "This bot allows you to: \n"
        "- Check current cryptocurrency prices \n"
        "- Calculate 7/14-day moving averages \n"
        "- Set price alerts \n"
        "- View simple price charts \n\n"
        "Use /start to begin."
    )