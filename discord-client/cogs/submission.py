import io
import logging
import discord
from discord.ext import commands
from discord import app_commands


class SubmissionCog(commands.Cog):
    def __init__(self, bot, logger: logging.Logger):
        self.bot = bot
        self.logger = logger
        self.logger.info("Main approvals cog initialized")

    bingo_items = [
        "Zulrah",
        "Amoxilatl",
    ]

    async def bingo_item_autocomplete(
        self,
        interaction: discord.Interaction,
        current: str,
    ) -> list[discord.app_commands.Choice[str]]:
        return [
            discord.app_commands.Choice(name=item, value=item)
            for item in self.bingo_items
            if current.lower() in item.lower()
        ]

    @app_commands.command(name="submit", description="Submit a PB")
    @app_commands.autocomplete(item=bingo_item_autocomplete)
    async def submit(self, interaction: discord.Interaction, item: str):
        interaction.response.send_message(
            f"Your PB request has been submitted: {item}!"
        )

    @app_commands.command(name="dropdown", description="Choose an item from a dropdown")
    async def dropdown(self, interaction: discord.Interaction):
        options = [
            discord.SelectOption(label=item, value=item) for item in self.bingo_items
        ]

        class Dropdown(discord.ui.Select):
            def __init__(self):
                super().__init__(
                    placeholder="Choose an item...",
                    min_values=1,
                    max_values=1,
                    options=options,
                )

            async def callback(self, select_interaction: discord.Interaction):
                await select_interaction.response.send_message(
                    f"You selected: {self.values[0]}", ephemeral=True
                )

        class DropdownView(discord.ui.View):
            def __init__(self):
                super().__init__()
                self.add_item(Dropdown())

        await interaction.response.send_message(
            "Pick an item from the dropdown:", view=DropdownView(), ephemeral=True
        )
