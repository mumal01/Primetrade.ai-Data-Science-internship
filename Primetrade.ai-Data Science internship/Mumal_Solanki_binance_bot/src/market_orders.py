# src/market_orders.py

from utils import init_client, validate_symbol, validate_quantity
from binance.enums import *
from logger import setup_logger
import sys

logger = setup_logger()

def place_market_order(symbol, side, quantity):
    client = init_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=quantity
        )
        logger.info("Market order placed: %s", order)
        print("Order placed successfully!")
        return order
    except Exception as e:
        logger.error("Market order failed: %s", e)
        print("Error placing order.")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python market_orders.py BTCUSDT BUY 0.01")
    else:
        _, symbol, side, quantity = sys.argv
        if validate_symbol(symbol) and validate_quantity(quantity):
            place_market_order(symbol.upper(), side.upper(), float(quantity))
        else:
            print("Invalid input.")
