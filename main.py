import json
import sys

from bot import EPCBot

config_path = sys.argv[1]

with open(config_path) as f:
    config = json.load(f)
    epc_bot = EPCBot(config)
    epc_bot.start()
    epc_bot.join()
