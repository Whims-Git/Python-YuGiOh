# Import monster card database
from vanilla_monster_cards import vanilla_monster_cards
from main_deck_monster_cards import main_deck_monster_cards
from spell_cards import spell_cards
from trap_cards import trap_cards
from collections import Counter

# Build a lookup dictionary for fast access
monster_card_lookup = {card["Name"]: card for card in vanilla_monster_cards + main_deck_monster_cards}
spell_card_lookup = {card["Name"]: card for card in spell_cards}
trap_card_lookup = {card["Name"]: card for card in trap_cards}
current_deck = []

def list_all_cards():
    print("\nAvailable Vanilla Monster Cards:")
    for card in vanilla_monster_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Main Deck Monster Cards:")
    for card in main_deck_monster_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Spell Cards:")
    for card in spell_cards:
        print(f"- {card['Name']}")

    print("\nAvailable Trap Cards:")
    for card in trap_cards:
        print(f"- {card['Name']}")

def search_card(name):
    card = monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
    if card:
        print(f"\nDetails for {name}:")
        for key, value in card.items():
            print(f"{key}: {value}")
    else:
        print(f"Card '{name}' not found.")

def add_card_to_deck(name, qty):
    card = monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
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
    
    if len(current_deck) + qty > 60:
        print("Cannot add cards. Deck limit of 60 cards will be exceeded.")
        return

    copies = current_deck.count(card)
    addable = min(qty, 3 - copies)
    current_deck.extend([card] * addable)
    print(f"\nAdded {addable} copy/copies of '{name}'. {name} x{copies + addable}.")
    if addable < qty:
        print(f"(Limit is 3 per card; {qty - addable} not added.)")

    show_deck()

def remove_card_from_deck(name, qty):
    card = monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)
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

    copies = current_deck.count(card)
    removable = min(qty, copies)
    if removable == 0:
        print(f"No copies of '{name}' found in your deck to remove.")
        show_deck()
        return
    
    # remove by Name
    removed = 0
    i = 0
    while i < len(current_deck) and removed < removable:
        if current_deck[i]["Name"] == name:
            current_deck.pop(i)
            removed += 1
            continue
        i += 1

    remaining = copies - removed
    print(f"\nRemoved {removed} copy/copies of '{name}'. Remaining: {name} x{remaining}.")
    if removed < qty:
        print(f"(Only {copies} copies were in the deck; {qty - removed} could not be removed.)")

    show_deck()

def card_type_counts():
    monster_count = sum(1 for card in current_deck if card["Name"] in monster_card_lookup)
    spell_count = sum(1 for card in current_deck if card["Name"] in spell_card_lookup)
    trap_count = sum(1 for card in current_deck if card["Name"] in trap_card_lookup)
    return monster_count, spell_count, trap_count

def show_deck():
    if not current_deck:
        print("\nYour deck is empty.")
        return

    # Get card type counts
    monster_count, spell_count, trap_count = card_type_counts()

    # build counts by Name
    name_counts = Counter(card["Name"] for card in current_deck)

    print(f"\nCurrent Deck ({monster_count} Monsters, {spell_count} Spells, {trap_count} Traps, {len(current_deck)} Cards Total):")
    for name, count in name_counts.items():
        print(f"- {name} x{count}")

#list_all_cards()
#search_card("Blue-Eyes White Dragon")
#add_card_to_deck("Blue-Eyes White Dragon")
#show_deck()
# Dark Magician