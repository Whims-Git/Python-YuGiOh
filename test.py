from spell_cards import field_spell_cards
from deck_building import (spell_card_lookup, main_deck_monster_card_lookup, extra_deck_monster_card_lookup, trap_card_lookup)


card_name = "Pot of Greed"
def determine_card_type(card_name):
        if card_name in main_deck_monster_card_lookup or card_name in extra_deck_monster_card_lookup:
            return "monster"
        elif card_name in spell_card_lookup:
            if spell_card_lookup[card_name]["Typing"] == "Field":
                return "field spell"
            return "spell"
        elif card_name in trap_card_lookup:
            return "trap"
        return None

print(determine_card_type(card_name))