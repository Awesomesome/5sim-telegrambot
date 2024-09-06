# 5sim Telegram Bot

This bot allows users to access information about countries, products, and operators using the 5sim API through Telegram.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a `.env` file with your Telegram bot token and 5sim API key
3. Run the bot: `python main.py`

## Usage

- `/start`: Get a welcome message
- `/country`: Get a list of available countries
- `/product`: Get a list of available products
- `/operator`: Get a list of available operators

## File Structure

- `main.py`: Entry point for the bot
- `config.py`: Configuration settings
- `bot.py`: Bot setup and main logic
- `api_client.py`: 5sim API client
- `handlers.py`: Command handlers for the bot
- `utils.py`: Utility functions

## Dependencies

- python-telegram-bot
- requests
- python-dotenv

Make sure to replace the placeholder values in the `.env` file with your actual Telegram bot token and 5sim API key.

Sample of .env
TELEGRAM_TOKEN= your bot key
SIM_API_KEY= your 5sim api key
