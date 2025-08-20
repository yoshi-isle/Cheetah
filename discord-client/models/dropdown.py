import discord


class Dropdown(discord.ui.Select):
    def __init__(self, options, custom_id: str | None = None):
        super().__init__(
            placeholder="Select an item to view PBs 🕒",
            min_values=1,
            max_values=1,
            options=options,
            custom_id=custom_id,
        )

    async def callback(self, select_interaction: discord.Interaction):
        embed = discord.Embed()
        embed.set_author(name="Zulrah")
        embed.add_field(
            name="",
            value="🏆 0:27 - Tanjiro - 145d reign - (proof)\n🥈0:33 - Some User - (proof)\n🥉0:40 - Reptar - (proof)",
            inline=False,
        )
        embed.set_thumbnail(
            url="https://oldschool.runescape.wiki/images/Zulrah_%28serpentine%29.png?29a54"
        )
        embeds = []

        embeds.append(embed)
        embed = discord.Embed()
        embed.set_author(name="Vorkath")
        embed.add_field(
            name="",
            value="🏆 0:27 - Tanjiro - 145d reign - (proof)\n🥈0:33 - Some User - (proof)\n🥉0:40 - Reptar - (proof)",
            inline=False,
        )
        embed.set_thumbnail(
            url="https://oldschool.runescape.wiki/images/thumb/Vorkath.png/560px-Vorkath.png?1ce3f"
        )
        embeds.append(embed)
        embed = discord.Embed()
        embed.set_author(name="Araxxor")
        embed.add_field(
            name="",
            value="🏆 0:27 - Tanjiro - 145d reign - (proof)\n🥈0:33 - Some User - (proof)\n🥉0:40 - Reptar - (proof)",
            inline=False,
        )
        embed.set_thumbnail(
            url="https://oldschool.runescape.wiki/images/thumb/Araxxor.png/560px-Araxxor.png?35d2e"
        )
        embeds.append(embed)

        for option in self.options:
            option.default = False
        await select_interaction.response.edit_message(view=self.view)

        await select_interaction.followup.send(embeds=embeds, ephemeral=True)
