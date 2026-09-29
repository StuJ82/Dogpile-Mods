from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items
from . import regions
    
if TYPE_CHECKING:
    from .world import DogpileWorld


#code inspiré d'ULTRAKILL https://github.com/TRPG0/ArchipelagoULTRAKILL/blob/main/apworld/


class LocationType:
    Card=0
    Goal=1
    Win=2
    Tag=3
    #peut-être d'autres, ou moins ?

class DogpileLocations:
    name:str
    region:Dogpile
    
