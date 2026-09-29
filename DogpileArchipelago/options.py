from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions, DefaultOnToggle, OptionSet
from .items import decks
class Goal(Choice):
    """
    Select your goal:
    - Classic : you need to complete each deck in "Chill" difficulty (selected by default)
    - All Modes : you need to compltete each deck in eall the difficulties (for now, 3)
    - Classic whit skins : same as "Classic", but you need to do it twice, with the other dog skin
    - Chaos : All decks, all modes and all skins
    """
    display_name="Goal"
    classic=0
    all_modes=1
    classic_with_skins=2
    chaos=3

    default=0
    

class Bundles(DefaultOnToggle):
    """
    Place all the tags into bundles, to limit the number of items in the item pool (241 without bundles)
    You can define the bundle size here
    """
    display_name="Bundles"

class BundleSize(Range):
    """
    Works only if "Bundles" is True
    You can here choose the size of the Tags Bundles.
    Default value is 5
    """
    display_name="Bundle Size"
    range_start=1
    range_end=30
    default=5
    
class StartingDeck(OptionSet):
    """
    Select your starting deck.
    By default, the deck is randomly chosen, but you can enter a value here
    as "{DECK NAME} Deck" (ex : "Classic Deck")
    """
    display_name="Starting Deck"
    default=[]
    valid_keys = [key for key in decks]

class DeathLink(Toggle):
    """
    Enable Death Link : if you lose, everyone dies, but if someone die, you lose
    """
    display_name="Death Link"
