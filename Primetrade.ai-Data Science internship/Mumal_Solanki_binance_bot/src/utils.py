# src/utils.py

from binance.client import Client
from config import API_KEY, API_SECRET, BASE_URL

def init_client():
    client = Client(API_KEY, API_SECRET)
    client.FUTURES_URL = f'{BASE_URL}/fapi'
    return client

def validate_symbol(symbol):
    return symbol.upper().endswith("USDT")

def validate_quantity(qty):
    try:
        return float(qty) > 0
    except:
        return False
