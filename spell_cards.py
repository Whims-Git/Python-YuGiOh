# Yu-Gi-Oh Normal Spell Card Database
# Each card is represented as a dictionary with 4 characteristics.

normal_spell_cards = [
    { # Pot of Greed
        "Name": "Pot of Greed",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Draw 2 cards."
    },
    { # Final Flame
        "Name": "Final Flame",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Inflict 600 points of damage to your opponent's Life Points."
    },
    { # Fissure
        "Name": "Fissure",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Destroy the 1 face-up monster your opponent controls that has the lowest ATK (your choice, if tied)."
    },
    { # Goblin's Secret Remedy
        "Name": "Goblin's Secret Remedy",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Increase your Life Points by 600 points."
    },
    { # Gravedigger Ghoul
        "Name": "Gravedigger Ghoul",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Select up to 2 Monster Card(s) from your opponent's Graveyard. Remove the selected card(s) from play."
    },
    { # Stop Defense
        "Name": "Stop Defense",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Select 1 Defense Position monster on your opponent's side of the field and change it to Attack Position."
    },
    { # Monster Reborn
        "Name": "Monster Reborn",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Target 1 monster in either GY; Special Summon it."
    },
    { # Dark Hole
        "Name": "Dark Hole",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Destroy all monsters on the field."
    },
    { # Polymerization
        "Name": "Polymerization",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Fusion Summon 1 Fusion Monster from your Extra Deck, using monsters from your hand or field as Fusion Material."
    },
    { # Raigeki
        "Name": "Raigeki",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Destroy all monsters your opponent controls."
    },
    { # Swords of Revealing Light
        "Name": "Swords of Revealing Light",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "After this card's activation, it remains on the field, but you must destroy it during the End Phase " \
        "of your opponent's 3rd turn. When this card is activated: If your opponent controls a face-down monster, " \
        "flip all monsters they control face-up. While this card is face-up on the field, your opponent's monsters cannot declare an attack."
    },
    # Add more cards below using the same format
]

field_spell_cards = [
    { # Forest
        "Name": "Forest",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All EARTH monsters gain 200 ATK and DEF."
    },
    # Add more cards below using the same format
]

equip_spell_cards = [
    { # Beast Fangs
        "Name": "Beast Fangs",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "A Beast-Type monster equipped with this card increases its ATK and DEF by 300 points."
    },
    # Add more cards below using the same format
]

quick_spell_cards = [
    { # Forest
        "Name": "Mystical Space Typhoon",
        "Category": "Spell",
        "Type": "Quick-Play",
        "Effect": "Target 1 Spell/Trap on the field; destroy that target."
    },
    # Add more cards below using the same format
]