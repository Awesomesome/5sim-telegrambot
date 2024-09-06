# Command handlers for the bot
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import CallbackContext, ConversationHandler
from api_client import SimAPIClient
import logging

CHOOSING, SELECTING_COUNTRY, SELECTING_OPERATOR, SELECTING_PRODUCT, CONFIRMING_PURCHASE, CONFIRMING_CANCEL = range(6)

def get_main_keyboard():
    return ReplyKeyboardMarkup([['Buy Number', 'Check Balance', 'Show Messages', 'Cancel Order']], one_time_keyboard=False)

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Welcome! What would you like to do?',
        reply_markup=get_main_keyboard(),
    )
    return CHOOSING

def handle_choice(update: Update, context: CallbackContext) -> int:
    user_choice = update.message.text.lower()
    if user_choice == 'buy number':
        countries = SimAPIClient.get_countries()
        if countries:
            country_keyboard = [[countries[country]['text_en']] for country in countries]
            update.message.reply_text(
                'Please select a country:',
                reply_markup=ReplyKeyboardMarkup(country_keyboard, one_time_keyboard=True)
            )
            logging.info(f"Presenting countries to user. First few: {country_keyboard[:5]}")
            return SELECTING_COUNTRY
        else:
            update.message.reply_text('Unable to fetch countries. Please try again later.', reply_markup=get_main_keyboard())
            return CHOOSING
    elif user_choice == 'check balance':
        return check_balance(update, context)
    elif user_choice == 'show messages':
        return show_messages(update, context)
    elif user_choice == 'cancel order':
        return confirm_cancel_order(update, context)
    else:
        update.message.reply_text('Invalid choice. Please try again.', reply_markup=get_main_keyboard())
        return CHOOSING

def select_country(update: Update, context: CallbackContext) -> int:
    selected_country = update.message.text
    logging.info(f"User selected country: {selected_country}")
    
    countries = SimAPIClient.get_countries()
    if countries is None:
        logging.error("Failed to fetch countries")
        update.message.reply_text('Unable to fetch countries. Please try again.', reply_markup=get_main_keyboard())
        return CHOOSING
    
    logging.info(f"Available countries: {list(countries.keys())}")
    
    country_code = None
    for code, details in countries.items():
        if details['text_en'].lower() == selected_country.lower():
            country_code = code
            break
    
    if country_code is None:
        logging.warning(f"Invalid country selection: {selected_country}")
        update.message.reply_text('Invalid country selection. Please choose from the provided options.', 
                                  reply_markup=ReplyKeyboardMarkup([[countries[c]['text_en']] for c in countries], one_time_keyboard=True))
        return SELECTING_COUNTRY
    
    logging.info(f"Selected country code: {country_code}")
    context.user_data['country'] = country_code
    
    prices = SimAPIClient.get_prices(country=country_code)
    logging.info(f"Fetched prices for country {country_code}: {prices}")
    
    if prices and country_code in prices:
        products = list(prices[country_code].keys())
        logging.info(f"Available products: {products}")
        product_keyboard = [[product] for product in products]
        update.message.reply_text(
            'Please select a product:',
            reply_markup=ReplyKeyboardMarkup(product_keyboard, one_time_keyboard=True)
        )
        return SELECTING_PRODUCT
    else:
        logging.error(f"Failed to fetch products for country {country_code}")
        update.message.reply_text(f'Unable to fetch products for {selected_country}. Please try again.', reply_markup=get_main_keyboard())
        return CHOOSING

def select_product(update: Update, context: CallbackContext) -> int:
    product = update.message.text
    context.user_data['product'] = product
    country = context.user_data['country']
    prices = SimAPIClient.get_prices(country=country, product=product)
    if prices and country in prices and product in prices[country]:
        operators = list(prices[country][product].keys())
        operator_keyboard = [[operator] for operator in operators]
        operator_keyboard.append(['Any'])
        update.message.reply_text(
            'Please select an operator:',
            reply_markup=ReplyKeyboardMarkup(operator_keyboard, one_time_keyboard=True)
        )
        return SELECTING_OPERATOR
    else:
        update.message.reply_text('Unable to fetch operators. Please try again.', reply_markup=get_main_keyboard())
        return CHOOSING

def select_operator(update: Update, context: CallbackContext) -> int:
    operator = update.message.text
    context.user_data['operator'] = operator
    country = context.user_data['country']
    product = context.user_data['product']
    prices = SimAPIClient.get_prices(country=country, product=product)
    if prices and country in prices and product in prices[country] and operator in prices[country][product]:
        price_info = prices[country][product][operator]
        update.message.reply_text(
            f'You are about to purchase a number for {product} in {country} using {operator} operator.\n'
            f'Price: {price_info["cost"]}\n'
            f'Available: {price_info["count"]}\n'
            f'Success rate: {price_info["rate"]}%\n'
            f'Do you want to proceed?',
            reply_markup=ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True)
        )
        return CONFIRMING_PURCHASE
    else:
        update.message.reply_text('Unable to fetch price information. Please try again.', reply_markup=get_main_keyboard())
        return CHOOSING

def confirm_purchase(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == 'yes':
        country = context.user_data['country']
        operator = context.user_data['operator']
        product = context.user_data['product']
        result = SimAPIClient.purchase_number(country, operator, product)
        if result and 'id' in result and 'phone' in result:
            context.user_data['order_id'] = result['id']
            context.user_data['purchased_number'] = result['phone']
            update.message.reply_text(
                f'Great! You have purchased a number for {product} in {country}: {result["phone"]}',
                reply_markup=get_main_keyboard(),
            )
        else:
            update.message.reply_text(
                'Sorry, unable to purchase a number at this time.',
                reply_markup=get_main_keyboard(),
            )
    else:
        update.message.reply_text('Purchase cancelled.', reply_markup=get_main_keyboard())
    return CHOOSING

def check_balance(update: Update, context: CallbackContext) -> int:
    balance = SimAPIClient.get_balance()
    if balance is not None:
        update.message.reply_text(f'Your current balance is: {balance}', reply_markup=get_main_keyboard())
    else:
        update.message.reply_text('Unable to retrieve balance at this time.', reply_markup=get_main_keyboard())
    return CHOOSING

def show_messages(update: Update, context: CallbackContext) -> int:
    number = context.user_data.get('purchased_number')
    if not number:
        update.message.reply_text('You haven\'t purchased a number yet.', reply_markup=get_main_keyboard())
        return CHOOSING

    messages = SimAPIClient.get_messages(number)
    if messages:
        message_text = '\n'.join([f"From: {msg['sender']}, Text: {msg['text']}" for msg in messages])
        update.message.reply_text(f'Messages for number {number}:\n{message_text}', reply_markup=get_main_keyboard())
    else:
        update.message.reply_text(f'No messages found for number {number}.', reply_markup=get_main_keyboard())
    return CHOOSING

def confirm_cancel_order(update: Update, context: CallbackContext) -> int:
    number = context.user_data.get('purchased_number')
    if not number:
        update.message.reply_text('You don\'t have an active order to cancel.', reply_markup=get_main_keyboard())
        return CHOOSING

    keyboard = ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True)
    update.message.reply_text(f'Are you sure you want to cancel the order for number {number}?', reply_markup=keyboard)
    return CONFIRMING_CANCEL

def cancel_order(update: Update, context: CallbackContext) -> int:
    if update.message.text.lower() == 'yes':
        order_id = context.user_data.get('order_id')
        logging.info(f"Attempting to cancel order ID: {order_id}")
        if order_id:
            result = SimAPIClient.cancel_number(order_id)
            logging.info(f"Cancel result: {result}")
            if result:
                del context.user_data['order_id']
                del context.user_data['purchased_number']
                update.message.reply_text('Your order has been cancelled successfully.', reply_markup=get_main_keyboard())
            else:
                update.message.reply_text('Failed to cancel the order. Please try again later or contact support.', reply_markup=get_main_keyboard())
        else:
            logging.warning("Attempted to cancel order, but no order ID found in user data.")
            update.message.reply_text('No active order found to cancel.', reply_markup=get_main_keyboard())
    else:
        update.message.reply_text('Order cancellation aborted.', reply_markup=get_main_keyboard())
    return CHOOSING

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'Operation cancelled.',
        reply_markup=get_main_keyboard(),
    )
    return CHOOSING

# Keep the existing handlers
def get_country_info(update: Update, context: CallbackContext) -> None:
    countries = SimAPIClient.get_countries()
    if countries and 'netherlands' in countries:
        code = countries['netherlands']
        update.message.reply_text(f"Country: Netherlands\nCode: {code}", reply_markup=get_main_keyboard())
    else:
        update.message.reply_text("Failed to retrieve information for Netherlands.", reply_markup=get_main_keyboard())

def get_product_info(update: Update, context: CallbackContext) -> None:
    products = SimAPIClient.get_products()
    if products and 'uber' in products:
        uber_info = products['uber']
        update.message.reply_text(f"Product: Uber\nInformation: {uber_info}", reply_markup=get_main_keyboard())
    else:
        update.message.reply_text("Failed to retrieve information for Uber.", reply_markup=get_main_keyboard())

def get_operator_info(update: Update, context: CallbackContext) -> None:
    operators = SimAPIClient.get_operators()
    if operators and 'virtual51' in operators:
        update.message.reply_text("Operator: Virtual51 is available.", reply_markup=get_main_keyboard())
    else:
        update.message.reply_text("Failed to retrieve information for Virtual51 operator.", reply_markup=get_main_keyboard())