# Yu-Gi-Oh Trap Card Database
# Each card is represented as a dictionary with 4 characteristics.

normal_trap_cards = [
    { # Two-Pronged Attack
        "Name": "Two-Pronged Attack",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "Select and destroy 2 of your monsters and 1 of your opponent's monsters."
    },
    { # Trap Hole
        "Name": "Trap Hole",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "When your opponent Normal or Flip Summons 1 monster with 1000 or more ATK: Target that monster; destroy that target."
    },
    { # Fairy's Hand Mirror
        "Name": "Fairy's Hand Mirror",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "When your opponent activates a Spell Card that targets exactly 1 monster (and no other cards) on the field: " \
        "Target another card that would be an appropriate target; that Spell now targets the new target."
    },
    { # Eatgaboon
        "Name": "Eatgaboon",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "If the ATK of a monster summoned by your opponent (excluding Special Summon) is 500 points or less, the monster is destroyed."
    },
    { # House of Adhesive Tape
        "Name": "House of Adhesive Tape",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "If the DEF of a monster summoned by your opponent (excluding Special Summon) is 500 points or less, the monster is destroyed."
    },
    { # Snake Fang
        "Name": "Snake Fang",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "Decrease 1 selected monster's DEF by 500 points during the turn this card is activated."
    },
    { # Fake Trap
        "Name": "Fake Trap",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "Activate only when your opponent activates a Spell, Trap, or Effect Monster's effect that would destroy a Trap Card(s) you control. " \
        "Destroy this card instead. (If the cards that would have been destroyed are face-down, you can look at them to confirm.)"
    },
    { # Mirror Force
        "Name": "Mirror Force",
        "Category": "Trap",
        "Type": "Normal",
        "Effect": "When an opponent's monster declares an attack: Destroy all your opponent's Attack Position monsters."
    },
    # Add more cards below using the same format
]

continuous_trap_cards = [
    { # Dragon Capture Jar
        "Name": "Dragon Capture Jar",
        "Category": "Trap",
        "Type": "Continuous",
        "Effect": "Change all face-up Dragon-Type monsters on the field to Defense Position, "
        "also they cannot change their battle positions."
    },
    { # Spellbinding Circle
        "Name": "Spellbinding Circle",
        "Category": "Trap",
        "Type": "Continuous",
        "Effect": "Activate this card by targeting 1 monster your opponent controls; it cannot attack or change its battle position. " \
        "When that monster is destroyed, destroy this card."
    },
    { # Robbin' Goblin
        "Name": "Robbin' Goblin",
        "Category": "Trap",
        "Type": "Continuous",
        "Effect": "Each time a monster you control inflicts Battle Damage to your opponent, your opponent discards 1 random card."
    },
    # Add more cards below using the same format
]

counter_trap_cards = [
    { # Horn of Heaven
        "Name": "Horn of Heaven",
        "Category": "Trap",
        "Type": "Counter",
        "Effect": "When a monster(s) would be Summoned: Tribute 1 monster; negate the Summon, and if you do, destroy that monster(s)."
    },
    { # Magic Jammer
        "Name": "Magic Jammer",
        "Category": "Trap",
        "Type": "Counter",
        "Effect": "When a Spell Card is activated: Discard 1 card; negate the activation, and if you do, destroy it."
    },
    { # Seven Tools of the Bandit
        "Name": "Seven Tools of the Bandit",
        "Category": "Trap",
        "Type": "Counter",
        "Effect": "When a Trap Card is activated: Pay 1000 LP; negate the activation, and if you do, destroy it."
    },
    { # Solemn Judgment
        "Name": "Solemn Judgment",
        "Category": "Trap",
        "Type": "Counter",
        "Effect": "When a monster(s) would be Summoned, OR a Spell/Trap Card is activated: Pay half your LP; negate the Summon or activation, and if you do, destroy that card."
    },
    # Add more cards below using the same format
]