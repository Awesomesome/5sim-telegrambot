# Main entry point for the bot
import logging
from bot import run_bot
from api_client import SimAPIClient

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if __name__ == '__main__':
    balance = SimAPIClient.get_balance()
    logging.info(f"Current balance: {balance}")
    
    # Test get_countries functionality
    countries = SimAPIClient.get_countries()
    if countries:
        logging.info(f"Successfully fetched countries. First country: {list(countries.keys())[0]}")
    else:
        logging.error("Failed to fetch countries")
    
    run_bot()