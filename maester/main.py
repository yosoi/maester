from dotenv import load_dotenv
from maester import MaesterClient
import os
import sys


load_dotenv()

ALIAS = os.getenv("ALIAS")
BOT = os.getenv("BOT")
TOKEN = os.getenv("TOKEN")

with open(os.path.join(sys.path[0], "pms_only_plz.txt"), "r") as f:
	messages = f.readlines()

client = MaesterClient(BOT, ALIAS, messages)
client.run(TOKEN)

