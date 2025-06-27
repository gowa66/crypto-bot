# jobs/alert_checker.py

from telegram.ext import ContextTypes
from services.crypto_service import CryptoService
from handlers.alert_handler import alerts

crypto_service = CryptoService()

async def check_alerts(context: ContextTypes.DEFAULT_TYPE):
    for user_id, user_alerts in alerts.items():
        for alert in user_alerts[:]:
            result = crypto_service.get_current_price(alert["symbol"])
            if "error" not in result and result["price"] >= alert["price"]:
                try:
                    await context.bot.send_message(
                        chat_id=user_id,
                        text=f"🔔 {alert['symbol']} reached ${result['price']:.2f}! Target was ${alert['price']:.2f}"
                    )
                    user_alerts.remove(alert)
                except:
                    continue