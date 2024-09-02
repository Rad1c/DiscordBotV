import discord
from MessageFilter import filter_message


async def on_message(message):
    censored_content = filter_message(message.content)
    if censored_content != message.content:
        await message.delete()

        await message.channel.send(f"{message.author.mention} said: {censored_content}")


class DiscordBot:
    def __init__(self, token):
        self.token = token

        intents = discord.Intents.default()
        intents.message_content = True

        self.client = discord.Client(intents=intents)
        self.client.event(self.on_ready)
        self.client.event(on_message)

    async def on_ready(self):
        print(f"Logged in as {self.client.user}")

    def run(self):
        self.client.run(self.token)