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
        print("\nThe deck has been shuffled.")

    def draw_card(self, n=1):
        for _ in range(n):
            if self.deck:
                card = self.deck.pop(0)
                self.hand.append(card)
                print(f"\nDrew card: {card['Name']}")
            else:
                print("\nDeck is empty! Cannot draw.")

def start_duel():
    field = PlayingField()
    field.shuffle_deck()
    field.draw_card(5)
    return field