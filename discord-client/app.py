from logging import Logger
import logging
import discord
import asyncio
from discord.ext import commands
from cogs.submission import SubmissionCog
import os

import redis


class Startup:
    def __init__(self):
        # Discord boilerplate
        self.intents = discord.Intents.all()
        self.intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=self.intents)

        # Logging setup
        self.logger = logging.getLogger("discord")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )
        self.logger.addHandler(handler)

        self.logger.info("Bot is starting...")

        self.redis_client = redis.Redis(
            host=os.getenv("REDIS_HOST", "localhost"),
            port=os.getenv("REDIS_PORT", 9001),
            db=os.getenv("REDIS_DB", 0),
        )

    async def start_bot(self):
        await self.bot.add_cog(SubmissionCog(self.bot, self.logger, self.redis_client))
        try:
            await self.bot.start(os.getenv("BOT_TOKEN"))
        except Exception as e:
            print(f"An error occurred while starting the bot: {e}")

    async def main():
        startup = Startup()
        await startup.start_bot()

    if __name__ == "__main__":
        asyncio.run(main())
