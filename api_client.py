# 5sim API client
import requests
from config import SIM_API_KEY
import logging
import json

class SimAPIClient:
    BASE_URL = "https://5sim.net/v1"
    
    @staticmethod
    def get_countries():
        url = f"{SimAPIClient.BASE_URL}/guest/countries"
        headers = {"Accept": "application/json"}
        try:
            logging.info(f"Sending request to fetch countries: {url}")
            response = requests.get(url, headers=headers)
            logging.info(f"Response status code: {response.status_code}")
            logging.info(f"Response content: {response.text[:500]}...")  # Log first 500 characters
            if response.status_code == 200:
                countries = response.json()
                logging.info(f"Fetched {len(countries)} countries")
                return countries  # Return the raw response
            else:
                logging.error(f"Failed to fetch countries. Status code: {response.status_code}")
                return None
        except Exception as e:
            logging.exception(f"Exception occurred while fetching countries: {str(e)}")
            return None

    @staticmethod
    def get_products(country, operator):
        url = f"{SimAPIClient.BASE_URL}/guest/products/{country}/{operator}"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return None

    @staticmethod
    def get_prices(country=None, product=None):
        url = f"{SimAPIClient.BASE_URL}/guest/prices"
        headers = {"Accept": "application/json"}
        params = {}
        if country:
            params['country'] = country
        if product:
            params['product'] = product
        try:
            logging.info(f"Sending request to fetch prices: {url}")
            logging.info(f"Request params: {params}")
            response = requests.get(url, headers=headers, params=params)
            logging.info(f"Response status code: {response.status_code}")
            logging.info(f"Response content: {response.text[:500]}...")  # Log first 500 characters
            if response.status_code == 200:
                prices = response.json()
                logging.info(f"Successfully fetched prices. Keys: {list(prices.keys())}")
                return prices
            else:
                logging.error(f"Failed to fetch prices. Status code: {response.status_code}")
                return None
        except Exception as e:
            logging.exception(f"Exception occurred while fetching prices: {str(e)}")
            return None

    @staticmethod
    def purchase_number(country, operator, product):
        url = f"{SimAPIClient.BASE_URL}/user/buy/activation/{country}/{operator}/{product}"
        headers = {"Authorization": f"Bearer {SIM_API_KEY}", "Accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return {'id': data.get('id'), 'phone': data.get('phone')}
        return None

    @staticmethod
    def get_balance():
        url = f"{SimAPIClient.BASE_URL}/user/profile"
        headers = {"Authorization": f"Bearer {SIM_API_KEY}", "Accept": "application/json"}
        try:
            logging.info(f"Sending request to fetch balance: {url}")
            response = requests.get(url, headers=headers)
            logging.info(f"Response status code: {response.status_code}")
            logging.info(f"Response content: {response.text[:200]}...")  # Log first 200 characters
            if response.status_code == 200:
                data = response.json()
                return data.get('balance')
            else:
                logging.error(f"Failed to fetch balance. Status code: {response.status_code}")
                return None
        except Exception as e:
            logging.exception(f"Exception occurred while fetching balance: {str(e)}")
            return None

    @staticmethod
    def get_messages(phone_number):
        url = f"{SimAPIClient.BASE_URL}/user/check/{phone_number}"
        headers = {"Authorization": f"Bearer {SIM_API_KEY}", "Accept": "application/json"}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('sms', [])
        return None

    @staticmethod
    def cancel_number(order_id):
        url = f"{SimAPIClient.BASE_URL}/user/cancel/{order_id}"
        headers = {"Authorization": f"Bearer {SIM_API_KEY}", "Accept": "application/json"}
        try:
            logging.info(f"Sending cancel request to URL: {url}")
            logging.info(f"Headers: {headers}")
            response = requests.get(url, headers=headers)
            logging.info(f"Cancel number response: Status code: {response.status_code}")
            logging.info(f"Response headers: {response.headers}")
            logging.info(f"Response content: {response.text[:200]}...")  # Log only first 200 characters
            
            if response.status_code == 200:
                data = response.json()
                if data.get('status') == 'CANCELED':
                    return True
                else:
                    logging.error(f"Order not canceled. Status: {data.get('status')}")
                    return False
            elif response.status_code == 403:
                logging.error("Authorization failed. Check your API key.")
                return False
            else:
                logging.error(f"Failed to cancel number. Status code: {response.status_code}")
                return False
        except Exception as e:
            logging.exception(f"Exception occurred while cancelling number: {str(e)}")
            return False

    # Add methods for products and operators