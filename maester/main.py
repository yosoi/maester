import boto3
import discord

client = boto3.client("lex-runtime")

response = client.post_text(
	botName = "Maester",
	botAlias = "maester",
	userId = "dev", # replace this with some kind of id from discord
	inputText = "roll"
)

print("Greetings, my liege.")
print(response["message"])
