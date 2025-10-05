from card_packs import (
    card_pack_1, # Legend of Blue Eyes White Dragon
    card_pack_2, # Metal Raiders
    card_pack_3 # Magic Ruler
)

from collections import Counter
import random

# List of all packs
all_packs = [card_pack_1, card_pack_2, card_pack_3]

# Build lookup: {pack_name: cards_list}
card_pack_lookup = {pack["Pack Name"]: pack["cards"] for pack in all_packs}

# The collection of cards that the player has pulled from packs (tracks quantity)
player_pulled_cards = []
card_copies = Counter()

# Helper to quantify the amount of cards per rarity in a pack
def rarity_counter(cards):
    rarity_counts = Counter(card['Rarity'] for card in cards)
    return rarity_counts

# Helper to determine the chance of pulling a certain rarity (returns dict of rarity:probability)
def pull_chance():
    # Example: Ultra Rare 5%, Rare 20%, Common 75%
    return {
        'Ultra Rare': 0.05,
        'Super Rare': 0.10,
        'Rare': 0.20,
        'Common': 0.65
    }

def pull_card_from_pack(pack_name, num_packs):
    if pack_name not in card_pack_lookup:
        print(f"\nPack '{pack_name}' not found.")
        return
    cards = card_pack_lookup[pack_name]
    if not cards:
        print(f"\nNo cards found in pack '{pack_name}'.")
        return
    if num_packs < 1:
        print("\nNumber of packs to open must be at least 1.")
        return
    elif num_packs > 10:
        print("\nYou can only open up to 10 packs at a time.")
        return
    
    rarity_probs = pull_chance()
    rarity_counts = rarity_counter(cards)
    # Build a list of available rarities in this pack
    available_rarities = [r for r in rarity_probs if rarity_counts.get(r, 0) > 0]
    # Normalize probabilities for only available rarities
    total_prob = sum(rarity_probs[r] for r in available_rarities)
    norm_probs = [rarity_probs[r]/total_prob for r in available_rarities]

    all_pulled_cards = []
    for pack_num in range(1, num_packs + 1):
        pack_pulled = []
        # 1 Rare (if available)
        rare_cards = [card for card in cards if card['Rarity'] == 'Rare']
        if rare_cards:
            rare_card = random.choice(rare_cards)
            pack_pulled.append(rare_card)
        else:
            # If no rare, fallback to any available
            pack_pulled.append(random.choice(cards))
        # 7 Commons (if available)
        common_cards = [card for card in cards if card['Rarity'] == 'Common']
        for _ in range(7):
            if common_cards:
                card = random.choice(common_cards)
            else:
                card = random.choice(cards)
            pack_pulled.append(card)
        # 1 card of any rarity (weighted)
        rarity = random.choices(available_rarities, weights=norm_probs, k=1)[0]
        rarity_cards = [card for card in cards if card['Rarity'] == rarity]
        if rarity_cards:
            card = random.choice(rarity_cards)
        else:
            card = random.choice(cards)
        pack_pulled.append(card)
        # Add to collections
        for card in pack_pulled:
            card_copies[card['Name']] += 1
            found = False
            for i, (n, q) in enumerate(player_pulled_cards):
                if n == card['Name']:
                    player_pulled_cards[i] = (n, q + 1)
                    found = True
                    break
            if not found:
                player_pulled_cards.append((card['Name'], 1))
        all_pulled_cards.append(pack_pulled)
        print(f"\nPack {pack_num} from '{pack_name}':")
        for card in pack_pulled:
            print(f"- {card['Name']} ({card['Category']}, {card['Type']}, {card['Rarity']})")
    return all_pulled_cards

def list_cards_in_pack(pack_name):
    if pack_name not in card_pack_lookup:
        print(f"\nPack '{pack_name}' not found.")
        return
    # Find the pack dictionary to get the 'Amount'
    pack = next((p for p in all_packs if p["Pack Name"] == pack_name), None)
    cards = card_pack_lookup[pack_name]
    print("\nHere are all the available cards in the selected pack")
    if pack:
        print(f"{pack_name}: {pack['Amount']} cards available")
        # Show rarity counts
        rarity_counts = rarity_counter(cards)
        for rarity, count in rarity_counts.items():
            print(f"  {rarity}: {count} card(s)")
        # Use player_pulled_cards for percentage and (xN)
        pack_card_names = {card['Name'] for card in cards}
        pulled_dict = dict(player_pulled_cards)
        if not player_pulled_cards:
            print(f"You own 0/{len(pack_card_names)} cards from this pack (0.0%)")
        else:
            owned = {name for name in pack_card_names if name in pulled_dict}
            percent_owned = (len(owned) / len(pack_card_names)) * 100 if pack_card_names else 0
            print(f"You own {len(owned)}/{len(pack_card_names)} cards from this pack ({percent_owned:.1f}%)")
    for card in cards:
        owned_qty = 0
        for n, q in player_pulled_cards:
            if n == card['Name']:
                owned_qty = q
                break
        if owned_qty > 0:
            print(f"- {card['Name']} ({card['Category']}, {card['Type']}, {card['Rarity']}) (x{owned_qty})")
        else:
            print(f"- {card['Name']} ({card['Category']}, {card['Type']}, {card['Rarity']})")

def list_player_pulled_cards():
    if not player_pulled_cards:
        print("\nYour collection is empty! You have not pulled any cards yet. Start pulling from packs to add to your collection.")
        return
    print("\nYour Pulled Cards:")
    for name, qty in player_pulled_cards:
        print(f"- {name} (x{qty})")
