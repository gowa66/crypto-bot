# handlers/button_handler.py

from telegram import Update
from telegram.ext import ContextTypes

from services.crypto_service import CryptoService

crypto_service = CryptoService()

async def handle_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "get_price":
        await query.edit_message_text("Send me a crypto symbol (e.g., BTC, ETH):")
        context.user_data["awaiting"] = "get_price"

    elif query.data == "moving_avg":
        await query.edit_message_text("Send me a crypto symbol to calculate moving averages:")
        context.user_data["awaiting"] = "moving_avg"

    elif query.data == "set_alert":
        await query.edit_message_text("Send alert in format SYMBOL PRICE (e.g., BTC 50000):")
        context.user_data["awaiting"] = "set_alert"

    elif query.data == "price_chart":
        await query.edit_message_text("Send a symbol to generate a chart:")
        context.user_data["awaiting"] = "price_chart"
