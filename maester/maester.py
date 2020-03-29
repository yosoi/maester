import boto3
import discord
import random


class MaesterClient(discord.Client):
	def __init__(self, bot_name, bot_alias, pm_only_messages):
		super().__init__()
		self.bot_alias = bot_alias
		self.bot_name = bot_name
		self.lex_client = boto3.client("lex-runtime")
		self.pm_only_messages = pm_only_messages

	async def on_ready(self):
		print("Logged on as", self.user)

	async def on_message(self, message):
		if message.author == self.user:
			return
		if message.channel.type is discord.ChannelType.private:
			response = self.get_lex_response(str(message.author.id), message.content)
			await message.channel.send(response["message"])
		elif message.content.lower().startswith("maester"):
			response = random.choice(self.pm_only_messages)
			await message.channel.send(response)

	def get_lex_response(self, user_id, input_text):
		return self.lex_client.post_text(
			botName = self.bot_name,
			botAlias = self.bot_alias,
			userId = user_id,
			inputText = input_text
		)
