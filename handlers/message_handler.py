# handlers/message_handler.py

from telegram import Update
from telegram.ext import ContextTypes

from services.crypto_service import CryptoService
from services.chart_service import create_price_chart
from handlers.alert_handler import set_price_alert
from utils.moving_average import calculate_moving_average

crypto_service = CryptoService()

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip().upper()
    awaiting = context.user_data.get("awaiting")

    if awaiting == "get_price":
        result = crypto_service.get_current_price(user_input)
        if "error" in result:
            await update.message.reply_text(f"❌ {result['error']}")
        else:
            await update.message.reply_text(
                f"💰 {result['symbol']} Price: ${result['price']:.2f}\n"
                f"24h Change: {result['change']:+.2f}%"
            )

    elif awaiting == "moving_avg":
        history = crypto_service.get_historical_data(user_input)
        if isinstance(history, dict) and "error" in history:
            await update.message.reply_text(f"❌ {history['error']}")
        else:
            ma7 = calculate_moving_average(history, 7)
            ma14 = calculate_moving_average(history, 14)
            await update.message.reply_text(
                f"📊 {user_input} Moving Averages:\n"
                f"7-day: ${ma7:.2f}\n14-day: ${ma14:.2f}"
            )

    elif awaiting == "price_chart":
        history = crypto_service.get_historical_data(user_input)
        if isinstance(history, dict) and "error" in history:
            await update.message.reply_text(f"❌ {history['error']}")
        else:
            chart = create_price_chart(history, user_input)
            await update.message.reply_photo(photo=chart, caption=f"📈 {user_input} Price Chart")

    elif awaiting == "set_alert":
        await set_price_alert(update, context)

    else:
        await update.message.reply_text("Please choose an option from /start.")

    context.user_data["awaiting"] = None