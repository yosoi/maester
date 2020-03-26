import boto3
import discord
from dotenv import load_dotenv
import os


load_dotenv()


TOKEN = os.getenv("TOKEN")
BOT = os.getenv("BOT")
ALIAS = os.getenv("ALIAS")


def get_lex_response(lex_client, bot_name, bot_alias, user_id, input_text):
	return lex_client.post_text(
		botName = bot_name,
		botAlias = bot_alias,
		userId = user_id,
		inputText = input_text
	)


lex = boto3.client("lex-runtime")


user_id = "dev"
message = "roll"
response = get_lex_response(lex, BOT, ALIAS, user_id, message)


print(response["message"])
