import io
import logging
import os
from typing import List
import discord
from discord.ext import commands
from discord import app_commands
from flask import json
from constants.emojis import EMOJIS
from views.dropdown_view import DropdownView
from redis import Redis
from urllib.parse import urlparse


class SubmissionCog(commands.Cog):
    def __init__(self, bot: commands.Bot, logger: logging.Logger | None = None):
        self.bot = bot
        self.logger = logger or logging.getLogger(__name__)
        self.logger.info("Submission cog initialized")

        redis_url = os.getenv("REDIS_CONNECTION_STRING", "redis://localhost:6379")
        parsed_url = urlparse(redis_url)
        self.redis_host = parsed_url.hostname
        self.redis_port = parsed_url.port

    bingo_items = [
        "Zulrah",
        "Amoxilatl",
    ]

    async def bingo_item_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str,
    ) -> List[app_commands.Choice[str]]:
        return [
            app_commands.Choice(name=item, value=item)
            for item in self.bingo_items
            if current.lower() in item.lower()
        ]

    @app_commands.command(name="submit", description="Submit a PB")
    @app_commands.autocomplete(item=bingo_item_autocomplete)
    async def submit(self, interaction: discord.Interaction, item: str):
        r = Redis(host=self.redis_host, port=self.redis_port, db=0)
        sample = {"id": 3, "url": "http://example.com"}
        r.lpush("mylist", json.dumps(sample))
        await interaction.response.send_message(
            f"Your PB request has been submitted: {item}!"
        )

    @app_commands.command(name="dropdown", description="Choose an item from a dropdown")
    async def dropdown(self, interaction: discord.Interaction):

        await interaction.channel.send(view=DropdownView())
        await interaction.response.defer(ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(SubmissionCog(bot))
