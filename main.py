import json
from bot import EPCBot

with open("config.json") as f:
    config = json.load(f)
    epc_bot = EPCBot(config)
    epc_bot.run()
