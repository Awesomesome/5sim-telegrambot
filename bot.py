# Bot setup and main logic
import logging
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from config import TELEGRAM_TOKEN
from handlers import start, handle_choice, cancel, get_country_info, get_product_info, get_operator_info, CHOOSING, SELECTING_COUNTRY, SELECTING_OPERATOR, SELECTING_PRODUCT, CONFIRMING_PURCHASE, CONFIRMING_CANCEL, select_country, select_operator, select_product, confirm_purchase, cancel_order

def handle_message(update, context):
    # This function will handle all text messages
    return handle_choice(update, context)

def run_bot():
    print(f"Bot script TELEGRAM_TOKEN: {TELEGRAM_TOKEN[:10]}...") # Print only the first 10 characters

    try:
        updater = Updater(TELEGRAM_TOKEN, use_context=True)
        dp = updater.dispatcher

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                CHOOSING: [MessageHandler(Filters.text & ~Filters.command, handle_choice)],
                SELECTING_COUNTRY: [MessageHandler(Filters.text & ~Filters.command, select_country)],
                SELECTING_PRODUCT: [MessageHandler(Filters.text & ~Filters.command, select_product)],
                SELECTING_OPERATOR: [MessageHandler(Filters.text & ~Filters.command, select_operator)],
                CONFIRMING_PURCHASE: [MessageHandler(Filters.regex('^(Yes|No)$'), confirm_purchase)],
                CONFIRMING_CANCEL: [MessageHandler(Filters.regex('^(Yes|No)$'), cancel_order)],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        dp.add_handler(conv_handler)
        dp.add_handler(CommandHandler("country", get_country_info))
        dp.add_handler(CommandHandler("product", get_product_info))
        dp.add_handler(CommandHandler("operator", get_operator_info))

        # Add a general message handler for text messages outside the conversation
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

        updater.start_polling()
        updater.idle()
    except Exception as e:
        logging.error(f"Error starting the bot: {str(e)}")