# src/logger.py

import logging

def setup_logger():
    logger = logging.getLogger("BinanceBotLogger")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler("bot.log")
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
