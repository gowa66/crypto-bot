# main.py

import logging
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters

from handlers.command_handler import start, help_command
from handlers.button_handler import handle_button
from handlers.message_handler import handle_text
from jobs.alert_checker import check_alerts

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    application = Application.builder().token('TELEGRAM_TOKEN').build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(handle_button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    application.job_queue.run_repeating(check_alerts, interval=300, first=10)

    logger.info("CryptoBot started.")
    application.run_polling()

if __name__ == "__main__":
    main()
