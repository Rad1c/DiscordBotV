from dotenv import  load_dotenv
from bot import DiscordBot
import os

load_dotenv()

_token = os.getenv("DISCORD_TOKEN")

bot = DiscordBot(_token)

bot.run()
