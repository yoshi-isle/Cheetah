import discord
from models.dropdown import Dropdown
from constants.emojis import EMOJIS


class DropdownView(discord.ui.View):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Boss PBs", value="boss_pbs", emoji=EMOJIS.BOSSES
            ),
            discord.SelectOption(
                label="Raid PBs", value="raid_pbs", emoji=EMOJIS.RAIDS
            ),
        ]
        super().__init__(timeout=None)
        self.add_item(Dropdown(options=options, custom_id="cheetah:dropdown:pbs"))
