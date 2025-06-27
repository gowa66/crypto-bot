# handlers/alert_handler.py

from telegram import Update
from telegram.ext import ContextTypes

alerts = {}

async def set_price_alert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        parts = update.message.text.strip().upper().split()
        symbol, price_str = parts[0], parts[1]
        price = float(price_str)
        user_id = update.effective_user.id

        if user_id not in alerts:
            alerts[user_id] = []

        alerts[user_id].append({"symbol": symbol, "price": price})
        await update.message.reply_text(f"✅ Alert set for {symbol} at ${price:.2f}")
    except Exception:
        await update.message.reply_text("❌ Invalid format. Use SYMBOL PRICE, e.g., BTC 50000")
