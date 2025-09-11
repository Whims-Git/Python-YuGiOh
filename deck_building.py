# Import card database
from monster_cards import vanilla_monster_cards, effect_monster_cards
from extra_deck_monster_cards import extra_deck_monster_cards
from spell_cards import spell_cards
from trap_cards import trap_cards

from collections import Counter

# Build a lookup dictionary for fast access
main_deck_monster_card_lookup = {card["Name"]: card for card in vanilla_monster_cards + effect_monster_cards}
extra_deck_monster_card_lookup = {card["Name"]: card for card in extra_deck_monster_cards}
spell_card_lookup = {card["Name"]: card for card in spell_cards}
trap_card_lookup = {card["Name"]: card for card in trap_cards}
current_main_deck = []
current_extra_deck = []

def list_all_cards():
    print("\nAvailable Vanilla Monster Cards:")
    for card in vanilla_monster_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Main Deck Monster Cards:")
    for card in effect_monster_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Extra Deck Monster Cards:")
    for card in extra_deck_monster_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Spell Cards:")
    for card in spell_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Trap Cards:")
    for card in trap_cards:
        print(f"- {card['Name']}")

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
        print("Please enter a valid number for quantity.")
        return
    
    if qty <= 0:
        print("You must add at least 1 copy of a card to your deck.")
        return
    
    if len(current_main_deck) + qty > 60:
        print("Cannot add cards. Deck limit of 60 cards will be exceeded.")
        return
    
    if len(current_extra_deck) + qty > 15:
        print("Cannot add cards. Extra Deck limit of 15 cards will be exceeded.")
        return

    copies = current_main_deck.count(card) or current_extra_deck.count(card)
    addable = min(qty, 3 - copies)
    if card in vanilla_monster_cards or effect_monster_cards or spell_cards or trap_cards:
        current_main_deck.extend([card] * addable)
    else:
        current_extra_deck.extend([card] * addable)
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
        print("Please enter a valid number for quantity.")
        return
    
    if qty <= 0:
        print("You must input a number greater than or equal to 1.")
        return

    copies = current_main_deck.count(card)
    removable = min(qty, copies)
    if removable == 0:
        print(f"No copies of '{name}' found in your deck to remove.")
        show_deck()
        return
    
    # remove by Name
    removed = 0
    i = 0
    while i < len(current_main_deck) and removed < removable:
        if current_main_deck[i]["Name"] == name:
            current_main_deck.pop(i)
            removed += 1
            continue
        i += 1

    remaining = copies - removed
    print(f"\nRemoved {removed} copy/copies of '{name}'. Remaining: {name} x{remaining}.")
    if removed < qty:
        print(f"(Only {copies} copies were in the deck; {qty - removed} could not be removed.)")

    show_deck()

def card_type_counts():
    main_deck_monster_count = sum(1 for card in current_main_deck if card["Name"] in main_deck_monster_card_lookup)
    extra_deck_monster_count = sum(1 for card in current_main_deck if card["Name"] in extra_deck_monster_card_lookup)
    spell_count = sum(1 for card in current_main_deck if card["Name"] in spell_card_lookup)
    trap_count = sum(1 for card in current_main_deck if card["Name"] in trap_card_lookup)
    return main_deck_monster_count, extra_deck_monster_count, spell_count, trap_count

def show_deck():
    if not current_main_deck:
        print("\nYour deck is empty.")
        return

    # Get card type counts
    main_deck_monster_count, extra_deck_monster_count, spell_count, trap_count = card_type_counts()

    # build counts by Name
    main_name_counts = Counter(card["Name"] for card in current_main_deck)
    extra_name_counts = Counter(card["Name"] for card in current_extra_deck)

    print(f"\nCurrent Deck ({main_deck_monster_count} Monsters, {spell_count} Spells, {trap_count} Traps, {len(current_main_deck)} Cards Total):")
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