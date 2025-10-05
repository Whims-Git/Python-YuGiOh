from spell_cards import field_spell_cards
from deck_building import (spell_card_lookup, main_deck_monster_card_lookup, extra_deck_monster_card_lookup, trap_card_lookup)
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

pack_name = "Legend of Blue Eyes White Dragon"
cards = card_pack_lookup[pack_name]

rarity_probs = pull_chance()
rarity_counts = rarity_counter(cards)

available_rarities = [r for r in rarity_probs if rarity_counts.get(r, 0) > 0]
total_prob = sum(rarity_probs[r] for r in available_rarities)

print(total_prob)