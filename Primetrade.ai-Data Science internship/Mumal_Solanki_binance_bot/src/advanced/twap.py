# src/advanced/twap.py

import time

def twap_strategy(symbol, side, total_qty, splits, interval_sec):
    qty_per_order = total_qty / splits
    for i in range(splits):
        place_market_order(symbol, side, qty_per_order)
        time.sleep(interval_sec)
