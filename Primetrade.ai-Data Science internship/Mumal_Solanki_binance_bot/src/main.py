# src/main.py

import os

print("Select Order Type:")
print("1. Market Order")
print("2. Limit Order")
print("3. Stop-Limit (ADV)")
print("4. OCO (ADV)")
print("5. TWAP Strategy (ADV)")

choice = input("Choice: ")

if choice == "1":
    os.system("python src/market_orders.py BTCUSDT BUY 0.01")
elif choice == "2":
    os.system("python src/limit_orders.py BTCUSDT SELL 0.01 63000")
# Add others accordingly
