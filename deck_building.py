# Import card database
from monster_cards import (
    vanilla_monster_cards,
    effect_monster_cards
)

from extra_deck_monster_cards import (
    extra_deck_fusions_cards
)

from spell_cards import (
    normal_spell_cards,
    field_spell_cards,
    equip_spell_cards,
    quick_spell_cards
)

from trap_cards import (
    normal_trap_cards,
    continuous_trap_cards,
    counter_trap_cards
)

from collections import Counter

# Build a lookup dictionary for fast access
main_deck_monster_card_lookup = {card["Name"]: card for card in vanilla_monster_cards + effect_monster_cards}
extra_deck_monster_card_lookup = {card["Name"]: card for card in extra_deck_fusions_cards}
spell_card_lookup = {card["Name"]: card for card in normal_spell_cards + field_spell_cards + equip_spell_cards + quick_spell_cards}
trap_card_lookup = {card["Name"]: card for card in normal_trap_cards + continuous_trap_cards + counter_trap_cards}

# Create Empty Lists for deck
current_main_deck = []
current_extra_deck = []

def list_all_vanillas():
    print("\nAvailable Vanilla Monster Cards:")
    for card in vanilla_monster_cards:
        main_type = card.get('Type', '').split(',')[0].strip()
        print(f"\n- {card['Name']}, Lv: {card['Level']}, {card['Attribute']}, {main_type}, ATK/{card['ATK']} DEF/{card['DEF']}")

def list_all_main_effects():
    print("\nAvailable Effect Monster Cards:")
    for card in effect_monster_cards:
        main_type = card.get('Type', '').split(',')[0].strip()
        print(f"\n- {card['Name']}, Lv: {card['Level']}, {card['Attribute']}, {main_type}, ATK/{card['ATK']} DEF/{card['DEF']}")

def list_all_fusions():
    print("\nAvailable Extra Deck Fusion Monster Cards:")
    for card in extra_deck_fusions_cards:
        main_type = card.get('Type', '').split(',')[0].strip()
        extra_type = card.get('Type', '').split(',')[1].strip()
        print(f"\n- {card['Name']}, Lv: {card['Level']}, {card['Attribute']}, {main_type}, {extra_type}, ATK/{card['ATK']} DEF/{card['DEF']}")

def list_all_spells():
    print("\nAvailable Spell Cards:")
    for card in normal_spell_cards + field_spell_cards + equip_spell_cards + quick_spell_cards:
        print(f"\n- {card['Name']}, {card['Typing']}")

def list_all_traps():
    print("\nAvailable Trap Cards:")
    for card in normal_trap_cards + continuous_trap_cards + counter_trap_cards:
        print(f"\n- {card['Name']}, {card['Typing']}")

def search_card(name):
    card = main_deck_monster_card_lookup.get(name) or extra_deck_monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
    if card:
        print(f"\nDetails for {name}:")
        for key, value in card.items():
            print(f"{key}: {value}")
    else:
        print(f"Card '{name}' not found.")

def add_card_to_deck(name, qty):
    card = main_deck_monster_card_lookup.get(name) or extra_deck_monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
    if not card:
        print(f"Card '{name}' not found.")
        return
    
    try:
        qty = int(qty)
    except ValueError:
        print("Please enter a number for quantity.")
        return
    
    if qty <= 0:
        print("You must add at least 1 copy of a card to your deck.")
        return
    
    # Determine which deck to add to
    if name in extra_deck_monster_card_lookup:
        if len(current_extra_deck) + qty > 15:
            print("Cannot add cards. Extra Deck limit of 15 cards will be exceeded.")
            return
        copies = sum(1 for c in current_extra_deck if c["Name"] == name)
        addable = min(qty, 3 - copies)
        current_extra_deck.extend([card] * addable)
        print(f"\nAdded {addable} copy/copies of '{name}' to Extra Deck. {name} x{copies + addable}.")
        if addable < qty:
            print(f"(Limit is 3 per card; {qty - addable} not added.)")
    else:
        if len(current_main_deck) + qty > 60:
            print("Cannot add cards. Deck limit of 60 cards will be exceeded.")
            return
        copies = sum(1 for card in current_main_deck if card["Name"] == name)
        addable = min(qty, 3 - copies)
        current_main_deck.extend([card] * addable)
        print(f"\nAdded {addable} copy/copies of '{name}'. {name} x{copies + addable}.")
        if addable < qty:
            print(f"(Limit is 3 per card; {qty - addable} not added.)")

    show_deck()

def remove_card_from_deck(name, qty):
    card = main_deck_monster_card_lookup.get(name) or extra_deck_monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
    if not card:
        print(f"Card '{name}' not found in your deck.")
        return
    
    try:
        qty = int(qty)
    except ValueError:
        print("Please enter a number for quantity.")
        return
    
    if qty <= 0:
        print("You must input an amount greater than or equal to 1 and less than or equal to 3.")
        return
    
    if name in extra_deck_monster_card_lookup:
        deck = current_extra_deck
    else:
        deck = current_main_deck

    copies = sum(1 for card in deck if card["Name"] == name)
    removable = min(qty, copies)
    if removable == 0:
        print(f"\nNo copies of '{name}' found in your deck to remove.")
        show_deck()
        return

    # Remove by Name
    removed = 0
    i = 0
    while i < len(deck) and removed < removable:
        if deck[i]["Name"] == name:
            deck.pop(i)
            removed += 1
            continue
        i += 1

    remaining = copies - removed
    print(f"\nRemoved {removed} copy/copies of '{name}'. Remaining: {name} x{remaining}.")
    if removed < qty:
        print(f"(Only {copies} copy/copies were in the deck; {qty - removed} copy/copies could not be removed.)")

    show_deck()

def card_type_counts():
    main_deck_monster_count = sum(1 for card in current_main_deck if card["Name"] in main_deck_monster_card_lookup)
    extra_deck_monster_count = sum(1 for card in current_extra_deck if card["Name"] in extra_deck_monster_card_lookup)
    spell_count = sum(1 for card in current_main_deck if card["Name"] in spell_card_lookup)
    trap_count = sum(1 for card in current_main_deck if card["Name"] in trap_card_lookup)
    return main_deck_monster_count, extra_deck_monster_count, spell_count, trap_count

def show_deck():

    if not current_main_deck and not current_extra_deck:
        print("\nYour deck is empty.")
        return
    
    # Get card type counts
    main_deck_monster_count, extra_deck_monster_count, spell_count, trap_count = card_type_counts()

    # build counts by Name
    main_name_counts = Counter(card["Name"] for card in current_main_deck)
    extra_name_counts = Counter(card["Name"] for card in current_extra_deck)

    print(f"\nCurrent Main Deck ({main_deck_monster_count} Monsters, {spell_count} Spells, {trap_count} Traps, {len(current_main_deck)} Cards Total):")
    for name, count in main_name_counts.items():
        print(f"- {name} x{count}")
    print(f"\nCurrent Extra Deck ({extra_deck_monster_count} Monsters, {len(current_extra_deck)} Cards Total):")
    for name, count in extra_name_counts.items():
        print(f"- {name} x{count}")

#list_all_cards()
#search_card("Blue-Eyes White Dragon")
#add_card_to_deck("Blue-Eyes White Dragon")
#show_deck()
# Dark Magician