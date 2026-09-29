#from BaseClasses import Item
from . import options
import random

offset = 383_930_000 #représente l'ID steam du jeu x100. Il ne faut pas que 2 offsets soient les mêmes dans tous les AP.

decks=[
    "Classic Deck",
    "Misfits Deck",
    "Goody Two Shampoos Deck",
    "Overly Keen Deck",
    "Yap Battle Deck",
    "That's Showbiz Deck",
    "Many Moles Deck",
    "Street Hounds Deck",
    "Pet Rock Deck",
    "Squeaky Clean Deck",
    "The Means Of Production Deck",
    "Pauper Deck",
    "Games As A Service Deck",
    "Chemtrails Deck",
    "Mall Dogs Deck",
    "Canine Circle Of Hell Deck",
    "Pedigree Deck"
]

modes=[
    "Chill",
    "Clever",
    "Turbo"
]

def create_deck_list():
    deck_list={}
    count=1
    if options.Goal=="all modes" or options.Goal=="Chaos" :#si le mode choisi est le "all modes", on ajoute met tous les modes
    # on va ajouter le compteur "count" à l'offset, pour identifier clairement chaque item
        for deck in deck_list: #On crée une liste qui contient tous les decks, avec les modes.
            for mode in modes:
                deck_list[deck + " - " + mode] = offset+count
                count+=1
        
    else: #sinon, on met juste "Chill"
        for deck in deck_list:
            deck_list[deck + " - " + modes[0]] = offset+count
            count+=1

    offset+=count#on actualise l'offset pour qu'il corresponde à la valeur du prochain élément


traits={
    "Miniature":offset,
    "Showdog":offset+1,
    "Friendly":offset+2,
    "Barky":offset+3,
    "Royal":offset+4,
    "Extra Good":offset+5,
    "Zoomy":offset+6,
    "Fostered":offset+7,
    "Stinky":offset+8,
    "Timid":offset+9,
    "Crated":offset+10,
    "Sleepy":offset+11,
    "Pack":offset+12,
    "Fleas":offset+13,
    "Digs ?":offset+14,
    "Cool":offset+15
    }

offset+=16 #actualisation

trainers={
    "Cheese":offset,
    "DoorBell":offset+1,
    "Bone":offset+2,
    "Trimmer":offset+3,
    "Trophy":offset+4,
    "Ribbon":offset+5,
    "Leash":offset+6,
    "Dog Wash":offset+7,
    "Pet Shop":offset+8,
    "Shampoo":offset+9,
    "Treat":offset+10,
    "Scissors":offset+11
}



offset+=12 #actualisation
"""
dogs={
    "Ace": offset,
    "Two":offset+1,
    "Three":offset+2,
    "Four":offset+3,
    "Five":offset+4,
    "Six":offset+5,
    "Seven":offset+6,
    "Eight":offset+7,
    "Nine":offset+8,
    "Ten":offset+9,
    "Jack":offset+10,
    "Queen":offset+11,
    "King":offset+12
}
offset+=13

if options.Goal=="chaos" or options.Goal=="classic_with_skins":

    alternative_dogs={ #dans le mode où il faut tout faire avec les 2 skins de chiens
        "Alternative Ace": offset,
        "Alternative Two":offset+1,
        "Alternative Three":offset+2,
        "Alternative Four":offset+3,
        "Alternative Five":offset+4,
        "Alternative Six":offset+5,
        "Alternative Seven":offset+6,
        "Alternative Eight":offset+7,
        "Alternative Nine":offset+8,
        "Alternative Ten":offset+9,
        "Alternative Jack":offset+10,
        "Alternative Queen":offset+11,
        "Alternative King":offset+12
    }
    offset+=13
"""
tags = {
    "A Centre For Ants": offset + 0,
    "A Sleeve Full": offset + 1,
    "Abdicate": offset + 2,
    "Acepocalypse": offset + 3,
    "Aces High": offset + 4,
    "Acrobat": offset + 5,
    "Adopter": offset + 6,
    "Adoption Day": offset + 7,
    "After Image": offset + 8,
    "Air Bud": offset + 9,
    "All Fluff": offset + 10,
    "All Naturale": offset + 11,
    "Alpha": offset + 12,
    "Antihero": offset + 13,
    "Antiques Dogshow": offset + 14,
    "Apprentice": offset + 15,
    "Archeologist": offset + 16,
    "Bad Influence": offset + 17,
    "Bargain Hunter": offset + 18,
    "Beggar": offset + 19,
    "Behaviourist": offset + 20,
    "Best For Last": offset + 21,
    "Best Friends": offset + 22,
    "Best in Show": offset + 23,
    "Big Ben": offset + 24,
    "Big Paw": offset + 25,
    "Bigger & Better": offset + 26,
    "Born to Lead": offset + 27,
    "Bouncy Castle": offset + 28,
    "Bribe": offset + 29,
    "Buried Treasure": offset + 30,
    "Burp": offset + 31,
    "Business School": offset + 32,
    "By Example": offset + 33,
    "CEO": offset + 34,
    "Cacophony": offset + 35,
    "Cautious": offset + 36,
    "Chase Tail": offset + 37,
    "ChickenTenders": offset + 38,
    "Chit Chat": offset + 39,
    "Close Enough": offset + 40,
    "ConsolationPrize": offset + 41,
    "Construction Crew": offset + 42,
    "Contagious": offset + 43,
    "Cute as a...": offset + 44,
    "Dark Ritual": offset + 45,
    "Daycare": offset + 46,
    "Daydreamer": offset + 47,
    "Dig Deep": offset + 48,
    "Ding": offset + 49,
    "Dirty Shortcut": offset + 50,
    "DivineRight": offset + 51,
    "Dog Breath": offset + 52,
    "Double or Nothing": offset + 53,
    "Drop it!": offset + 54,
    "Dry Off": offset + 55,
    "Dynamic Duo": offset + 56,
    "Endless Joy": offset + 57,
    "Even More": offset + 58,
    "Everything's Fine": offset + 59,
    "Excavator": offset + 60,
    "Excitable": offset + 61,
    "Extra... Extra Good": offset + 62,
    "Fact!": offset + 63,
    "Cry On Cue": offset + 64,
    "False Start": offset + 65,
    "Fart": offset + 66,
    "Filthy Rich": offset + 67,
    "Flush": offset + 68,
    "Forever Home": offset + 69,
    "Friendly Folds": offset + 70,
    "Gnarly Combo": offset + 71,
    "Good Behaviour": offset + 72,
    "Greaseballs": offset + 73,
    "Grow Old": offset + 74,
    "Hidden Gem": offset + 75,
    "Hidden Pill": offset + 76,
    "High & Low": offset + 77,
    "High Fibre Diet": offset + 78,
    "Hop & A Skip": offset + 79,
    "Hop On Pop": offset + 80,
    "Hot Potato": offset + 81,
    "Hour Of Need": offset + 82,
    "Huddle": offset + 83,
    "Hyperdrive": offset + 84,
    "Inmates": offset + 85,
    "Inside Man": offset + 86,
    "Investor": offset + 87,
    "Jackpot": offset + 88,
    "Jailbreak": offset + 89,
    "Jupiter": offset + 90,
    "Jurassic Bark": offset + 91,
    "Karen": offset + 92,
    "Laika": offset + 93,
    "Lassie": offset + 94,
    "Last Chance": offset + 95,
    "Let Them Lie": offset + 96,
    "Lightheaded": offset + 97,
    "Littermates": offset + 98,
    "Little Buddy": offset + 99,
    "Little Litter": offset + 100,
    "Little Treat": offset + 101,
    "Living Rug": offset + 102,
    "Locksmith": offset + 103,
    "Long Leash": offset + 104,
    "Long Legs": offset + 105,
    "Idiot! Loser!": offset + 106,
    "Luxury Shopper": offset + 107,
    "Many Hands": offset + 108,
    "Mass Hysteria": offset + 109,
    "Mathematician": offset + 110,
    "Megaphone": offset + 111,
    "Meteor": offset + 112,
    "Microscope": offset + 113,
    "Middle Ground": offset + 114,
    "Mob Boss": offset + 115,
    "Monarch": offset + 116,
    "Mr Sandman": offset + 117,
    "Mudslide": offset + 118,
    "New Dog New Trick": offset + 119,
    "No Biggie": offset + 120,
    "Nuggets of Gold": offset + 121,
    "Obedience": offset + 122,
    "Odd Times": offset + 123,
    "101": offset + 124,
    "One With Nature": offset + 125,
    "Oodles": offset + 126,
    "Organised Play": offset + 127,
    "Ouroboros": offset + 128,
    "Outbreak": offset + 129,
    "Outlaw": offset + 130,
    "Over K-9000": offset + 131,
    "Overachiever": offset + 132,
    "Overstimulated": offset + 133,
    "Pack Strong": offset + 134,
    "Pair of Pups": offset + 135,
    "Paramedogs": offset + 136,
    "Passing Grade": offset + 137,
    "Patience": offset + 138,
    "Pay To Win": offset + 139,
    "Pebbles": offset + 140,
    "Pennies": offset + 141,
    "Perfectly Trained": offset + 142,
    "Perfumed Pooches": offset + 143,
    "Pesticide": offset + 144,
    "Poochy": offset + 145,
    "PopularFriend": offset + 146,
    "Powerful Funk": offset + 147,
    "Prescription": offset + 148,
    "Pretty Privelige": offset + 149,
    "Princelings": offset + 150,
    "Prized Lineage": offset + 151,
    "Prized Wieners": offset + 152,
    "Pro Walker": offset + 153,
    "Protest": offset + 154,
    "Pug Life": offset + 155,
    "Puppies": offset + 156,
    "Quantum Tunnelling": offset + 157,
    "Race Ahead": offset + 158,
    "Rags To Riches": offset + 159,
    "Razz Up": offset + 160,
    "Redecorator": offset + 161,
    "Relay Race": offset + 162,
    "Responsible Owner": offset + 163,
    "Rise & Shine": offset + 164,
    "Role Reversal": offset + 165,
    "Roll Over": offset + 166,
    "Royal Parade": offset + 167,
    "Run!": offset + 168,
    "Scram Kid": offset + 169,
    "Secret Tunnel": offset + 170,
    "Settle Down": offset + 171,
    "Seven Did WHAT?": offset + 172,
    "Shelter": offset + 173,
    "Shepherd": offset + 174,
    "Shiver": offset + 175,
    "Short Leash": offset + 176,
    "Should've Been Fixed": offset + 177,
    "Showing Hole": offset + 178,
    "Show's Over": offset + 179,
    "Silent But Deadly": offset + 180,
    "Sit!": offset + 181,
    "Sleep Study": offset + 182,
    "Slick": offset + 183,
    "Slip The Bars": offset + 184,
    "Slippers": offset + 185,
    "Small & Mighty": offset + 186,
    "Smells Like Updog": offset + 187,
    "Smelt It Dealt It": offset + 188,
    "Smidge": offset + 189,
    "Smooth": offset + 190,
    "Sniffers": offset + 191,
    "Snip Snip": offset + 192,
    "So Brave": offset + 193,
    "Specialist": offset + 194,
    "Spineless Cowards": offset + 195,
    "Sprinkler System": offset + 196,
    "Squint": offset + 197,
    "Squirrel!?": offset + 198,
    "Star Pupil": offset + 199,
    "Stay!": offset + 200,
    "Stinky Soap": offset + 201,
    "StoreCredit": offset + 202,
    "Storm Warning": offset + 203,
    "Straight Dog": offset + 204,
    "Strays": offset + 205,
    "Strength In Numbers": offset + 206,
    "StrictOwner": offset + 207,
    "Stylist": offset + 208,
    "Summoning Circle": offset + 209,
    "Supersonic": offset + 210,
    "Sweet Dreams": offset + 211,
    "TaxReturn": offset + 212,
    "Teamwork": offset + 213,
    "Teeny": offset + 214,
    "Tennis Ball": offset + 215,
    "The Farm": offset + 216,
    "The Gambler": offset + 217,
    "The Swindler": offset + 218,
    "The Very Best": offset + 219,
    "Thinks It's People": offset + 220,
    "Three of a Hound": offset + 221,
    "Through The World": offset + 222,
    "Timeless Echo": offset + 223,
    "Too Cool For School": offset + 224,
    "Top Dogs": offset + 225,
    "Toy Factory": offset + 226,
    "Training Montage": offset + 227,
    "Treat Bag": offset + 228,
    "Underachiever": offset + 229,
    "Reverse": offset + 230,
    "Velcro Dog": offset + 231,
    "Waft": offset + 232,
    "Well Trained": offset + 233,
    "Where'd You Get That": offset + 234,
    "Whippets": offset + 235,
    "Whistle": offset + 236,
    "Window Shopper": offset + 237,
    "Yappers": offset + 238,
    "Yard Sale": offset + 239,
    "Zoomies": offset + 240,
}

def create_tag_bundles():
    tags_bundles={}
    l=[]
    count=0
    while tags:
        random_key = random.choice(list(tags.keys()))
        tags.pop(random_key)
        l.append(random_key)
        if len(tags)==0:
            tags_bundles[offset+count-1].append(random_key)
        if len(l)==options.BundleSize: #gère la taille des bundles en fonction des options
            tags_bundles[offset+count]=l
            count+=1
            l=[]
    print(tags_bundles)


def classification():
    dict_classification={}
    for 
