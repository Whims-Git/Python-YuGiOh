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
    { # Hinotama
        "Name": "Hinotama",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Inflict 500 damage to your opponent."
    },
    { # Red Medicine
        "Name": "Red Medicine",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Increase your Life Points by 500 points."
    },
    { # Remove Trap
        "Name": "Remove Trap",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Select 1 face-up Trap Card on the field and destroy it."
    },
    { # Sparks
        "Name": "Sparks",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Inflict 200 points of damage to your opponent's Life Points."
    },
    { # Curse of Fiend
        "Name": "Curse of Fiend",
        "Category": "Spell",
        "Type": "Normal",
        "Effect": "Change the battle positions of all Attack Position monsters on the field to Defense Position and vice-versa. " \
        "These positions cannot be changed during the turn this card is activated except by the effect of a Spell, Trap or Effect Monster Card. " \
        "You can only activate this card during your Standby Phase."
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
    { # Mountain
        "Name": "Mountain",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All Dragon, Winged Beast, and Thunder monsters on the field gain 200 ATK/DEF."
    },
    { # Umi
        "Name": "Umi",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All Fish, Sea Serpent, Thunder, and Aqua monsters on the field gain 200 ATK/DEF, " \
        "also all Machine and Pyro monsters on the field lose 200 ATK/DEF."
    },
    { # Wasteland
        "Name": "Wasteland",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All Dinosaur, Zombie, and Rock monsters on the field gain 200 ATK/DEF."
    },
    { # Yami
        "Name": "Yami",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All Fiend and Spellcaster monsters on the field gain 200 ATK/DEF, also all Fairy monsters " \
        "on the field lose 200 ATK/DEF."
    },
    { # Gaia Power
        "Name": "Gaia Power",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All EARTH monsters gain 500 ATK and lose 400 DEF."
    },
    { # Luminous Spark
        "Name": "Luminous Spark",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All LIGHT monsters gain 500 ATK and lose 400 DEF."
    },
    { # Molten Destruction
        "Name": "Molten Destruction",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All FIRE monsters gain 500 ATK and lose 400 DEF."
    },
    { # Rising Air Current
        "Name": "Rising Air Current",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "All WIND monsters gain 500 ATK and lose 400 DEF."
    },
    { # Umiiruka
        "Name": "Umiiruka",
        "Category": "Spell",
        "Type": "Field",
        "Effect": "Increase the ATK of all WATER monsters by 500 points and decrease their DEF by 400 points."
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
    { # Book of Secret Arts
        "Name": "Book of Secret Arts",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "A Spellcaster-Type monster equipped with this card increases its ATK and DEF by 300 points."
    },
    { # Dark Energy
        "Name": "Dark Energy",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Increase the ATK and DEF of a Fiend-Type monster equipped with this card by 300 points."
    },
    { # Dragon Treasure
        "Name": "Dragon Treasure",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "A Dragon-Type monster equipped with this card increases its ATK and DEF by 300 points."
    },
    { # Electro-Whip
        "Name": "Electro-Whip",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Increase the ATK and DEF of a Thunder-Type monster equipped with this card by 300 points."
    },
    { # Electro-Whip
        "Name": "Electro-Whip",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Increase the ATK and DEF of a Thunder-Type monster equipped with this card by 300 points."
    },
    { # Follow Wind
        "Name": "Follow Wind",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Increase the ATK and DEF of a Winged Beast-Type monster equipped with this card by 300 points."
    },
    { # Laser Cannon Armor
        "Name": "Laser Cannon Armor",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to an Insect monster. It gains 300 ATK/DEF."
    },
    { # Legendary Sword
        "Name": "Legendary Sword",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to a Warrior monster. It gains 300 ATK/DEF."
    },
    { # Machine Conversion Factory
        "Name": "Machine Conversion Factory",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to a Machine monster. It gains 300 ATK/DEF."
    },
    { # Mystical Moon
        "Name": "Mystical Moon",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to a Beast-Warrior-Type monster. It gains 300 ATK and DEF."
    },
    { # Power of Kaishin
        "Name": "Power of Kaishin",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to an Aqua monster. It gains 300 ATK/DEF."
    },
    { # Raise Body Heat
        "Name": "Raise Body Heat",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "Equip only to a Dinosaur monster. It gains 300 ATK/DEF."
    },
    { # Silver Bow and Arrow
        "Name": "Silver Bow and Arrow",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "A Fairy-Type monster equipped with this card increases its ATK and DEF by 300 points."
    },
    { # Vile Germs
        "Name": "Vile Germs",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "A Plant-Type monster equipped with this card increases its ATK and DEF by 300 points."
    },
    { # Violet Crystal
        "Name": "Violet Crystal",
        "Category": "Spell",
        "Type": "Equip",
        "Effect": "(This card is not treated as a 'Crystal' card.) Equip only to a Zombie monster. It gains 300 ATK/DEF."
    },
    # Add more cards below using the same format
]

quick_spell_cards = [
    { # Mystical Space Typhoon
        "Name": "Mystical Space Typhoon",
        "Category": "Spell",
        "Type": "Quick-Play",
        "Effect": "Target 1 Spell/Trap on the field; destroy that target."
    },
    # Add more cards below using the same format
]

continuous_spell_cards = [
    { # Gravekeeper's Servant
        "Name": "Gravekeeper's Servant",
        "Category": "Spell",
        "Type": "Continuous",
        "Effect": "Your opponent must send 1 card from the top of their Deck to the Graveyard to declare an attack."
    },
    # Add more cards below using the same format
]