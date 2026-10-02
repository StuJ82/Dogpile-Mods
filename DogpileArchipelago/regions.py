from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

from . import options

if TYPE_CHECKING:
    from .world import DogpileWorld

class DogpileRegion:
    short_name:str
    full_name:str


def create_and_connect_regions(world: DogpileWorld) -> None:
    create_all_regions(world)
    #connect_regions(world)

def create_all_regions(world: DogpileWorld)->None:
    classic_deck_chill = Region("Classic Deck : Chill",world.player,world.multiworld)
    classic_deck_clever = Region("Classic Deck : Clever",world.player,world.multiworld)
    classic_deck_turbo = Region("Classic Deck : Turbo",world.player,world.multiworld)
    misfits_deck_chill = Region("Misfits Deck : Chill",world.player,world.multiworld)
    misfits_deck_clever = Region("Misfits Deck : Clever",world.player,world.multiworld)
    misfits_deck_turbo = Region("Misfits Deck : Turbo",world.player,world.multiworld)
    shampoos_deck_chill = Region("Goody Two Shampoos Deck : Chill",world.player,world.multiworld)
    shampoos_deck_clever = Region("Goody Two Shampoos Deck : Clever",world.player,world.multiworld)
    shampoos_deck_turbo = Region("Goody Two Shampoos Deck : Turbo",world.player,world.multiworld)
    friendly_deck_chill = Region("Friendly Deck : Chill",world.player,world.multiworld)
    friendly_deck_clever = Region("Friendly Deck : Clever",world.player,world.multiworld)
    friendly_deck_turbo = Region("Friendly Deck : Turbo",world.player,world.multiworld)
    #autres régions à rajouter

    #ATTENTION : rajouter le fait que pour débloquer la difficulté 2, il faut avoir débloqué la difficulté 1
    regions=[classic_deck_chill,misfits_deck_chill,shampoos_deck_chill,friendly_deck_chill]
    

    if options.Goal=="all_modes": #un mode de jeu où il faut finir tout dans toutes les difficultés. Celle de base seulement sinon.
        regions.extend([classic_deck_clever,classic_deck_turbo,misfits_deck_clever,misfits_deck_turbo,
                shampoos_deck_clever,shampoos_deck_turbo,friendly_deck_clever,friendly_deck_turbo])

    world.multiworld.regions+=regions

#Pas besoin de connect_regions(), car pas de régions à connecter dans ce jeu, mais la progression existe.
    def connect_regions(world:DogpileWorld):
        pass
        
