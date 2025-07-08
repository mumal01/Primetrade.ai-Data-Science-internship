# src/limit_orders.py

from utils import init_client, validate_symbol, validate_quantity
from binance.enums import *
from logger import setup_logger
import sys

logger = setup_logger()

def place_limit_order(symbol, side, quantity, price):
    client = init_client()
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=ORDER_TYPE_LIMIT,
            timeInForce=TIME_IN_FORCE_GTC,
            quantity=quantity,
            price=price
        )
        logger.info("Limit order placed: %s", order)
        print("Limit order placed.")
        return order
    except Exception as e:
        logger.error("Limit order failed: %s", e)
        print("Failed to place limit order.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python limit_orders.py BTCUSDT SELL 0.01 63000")
    else:
        _, symbol, side, quantity, price = sys.argv
        if validate_symbol(symbol) and validate_quantity(quantity):
            place_limit_order(symbol.upper(), side.upper(), float(quantity), price)
        else:
            print("Invalid input.")
