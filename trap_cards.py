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
    # Add more cards below using the same format
]

counter_trap_cards = [
    { # Solemn Judgment
        "Name": "Solemn Judgment",
        "Category": "Trap",
        "Type": "Counter",
        "Effect": "When a monster(s) would be Summoned, OR a Spell/Trap Card is activated: "
        "Pay half your LP; negate the Summon or activation, and if you do, destroy that card."
    },
    # Add more cards below using the same format
]