from collections.abc import Mapping
from typing import Any
from BaseClasses import Tutorial
# Imports of base Archipelago modules must be absolute.
from worlds.AutoWorld import World

class DogpileWebWorld:
    theme = "partyTime"
    rich_text_options_doc = True
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Dogpile on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Burndi"]
    )
    tutorials = [setup_en]

class DogpileWorld(World):
    """
    Dogpile is a roguelike deck builder about merging cute dogs into bigger dogs.
    You send checks buying cards in the shop, or completing goals/beating a deck
    """
    game="Dogpile"
    