from spell_cards import field_spell_cards
from deck_building import spell_card_lookup



name = "Pot of Greed"
card = spell_card_lookup.get(name)

if not card:
    print(f"\nCard '{name}' not found.")

if card["Typing"] != "Field":
    print("Not a field spell")
else:
    print("Field spell")