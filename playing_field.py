from deck_building import current_main_deck, current_extra_deck, search_card, card_type_counts
import random

class PlayingField:
    def __init__(self):
        self.monster_zones = [None] * 5
        self.spell_trap_zones = [None] * 5
        self.field_zone = None
        self.graveyard = []
        self.deck = current_main_deck.copy()
        self.extra_deck = current_extra_deck.copy()
        self.banished = []
        self.hand = []

    def shuffle_deck(self):
        random.shuffle(self.deck)