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

from deck_building import (
    current_main_deck,
    current_extra_deck,
    search_card,
    card_type_counts,
    main_deck_monster_card_lookup,
    extra_deck_monster_card_lookup,
    spell_card_lookup,
    trap_card_lookup,
)

from play_ygo import main_menu

import random
from collections import Counter

class PlayingField:
    def __init__(self):
        self.monster_zones = [None] * 5
        self.spell_trap_zones = [None] * 5
        self.field_spell_zone = None
        self.graveyard = []
        self.deck = current_main_deck.copy()
        self.extra_deck = current_extra_deck.copy()
        self.banished = []
        self.hand = []

    def shuffle_deck(self):
        random.shuffle(self.deck)
        print("\nThe deck has been shuffled.")

    def draw_card(self, n = 1):
        for _ in range(n):
            if self.deck:
                card = self.deck.pop(0)
                self.hand.append(card)
                print(f"\nDrew card: {card.get('Name', 'Unknown')}, Remaining cards in deck: {len(self.deck)} cards")
            else:
                print("\nDeck is empty! Cannot draw. You lose!")
                # Reset the entire duel so that players won't have to rebuild their decks to replay.
                self.monster_zones = [None] * 5
                self.spell_trap_zones = [None] * 5
                self.field_zone = None
                self.graveyard = []
                self.deck = current_main_deck.copy()
                self.extra_deck = current_extra_deck.copy()
                self.banished = []
                self.hand = []
                main_menu()
    # Create a field card dictionary for dynamic properties
    def field_monster_card_properties(self, card, position = "face-up attack", equipped_monster = None):
        return {
            "card": card,  # Original card data
            "position": position,  # face-up attack, face-down defense
            "equipped_cards": [],  # Cards equipped to this card
            "equipped_to": equipped_monster, # monster this card is equipped to
            "counters": 0,  # Counter tokens on card
            "affected_by": [],  # Card effects currently affecting this card
            "attack_modifier": 0,  # Changes to original ATK
            "defense_modifier": 0,  # Changes to original DEF
            "cannot_attack": False,  # If card is prevented from attacking
            "cannot_change_position": False,  # If card cannot change battle position
            "negated": False
        }
    
    def field_backrow_card_properties(self, card, position = "face-up", equipped_monster = None):
        return {
            "card": card,  # Original card data
            "position": position,  # face-up, face-down
            "equipped_to": equipped_monster,  # monster this card is equipped to
            "counters": 0,  # Counter tokens on card
            "affected_by": [],  # Card effects currently affecting this card
            "negated": False
        }
    
    def field_spell_card_properties(self, card, position = "face-up"):
        return {
            "card": card,  # Original card data
            "position": position,  # face-up, face-down
            "counters": 0,  # Counter tokens on card
            "affected_by": [],  # Card effects currently affecting this card
            "negated": False
        }
    
    # Return monster count, extra monster count, spell count, and trap count for a given list of cards.
    def count_types(self, collection):
        m = e = s = t = 0
        for card in collection:
            if not card:
                continue
            name = card.get("Name")
            if name in main_deck_monster_card_lookup:
                m += 1
            elif name in extra_deck_monster_card_lookup:
                e += 1
            elif name in spell_card_lookup:
                s += 1
            elif name in trap_card_lookup:
                t += 1
        return m, e, s, t

    def show_field(self):
        print("\nMonster Zones (Left -> Right):")
        for i, card in enumerate(self.monster_zones):
            if card is None:
                print(f"  {i+1}: Empty")
            else:
                inner = card.get('card') if isinstance(card, dict) else card
                pos = card.get('position') if isinstance(card, dict) else None
                if pos == 'face-down defense':
                    print(f"  {i+1}: Set Card (Face-down)")
                else:
                    print(f"  {i+1}: {inner.get('Name', 'Unknown')}")

        if self.field_spell_zone is None:
            print(f"\nField Spell Zone: Empty")
        else:
            inner = self.field_spell_zone.get('card') if isinstance(self.field_spell_zone, dict) else self.field_spell_zone
            pos = self.field_spell_zone.get('position') if isinstance(self.field_spell_zone, dict) else None
            if pos == 'face-down':
                print(f"\nField Spell Zone: Set Card (Face-down)")
            else:
                print(f"\nField Spell Zone: {inner.get('Name', 'Unknown')}")

        print("\nSpell/Trap Zones (Left -> Right):")
        for i, card in enumerate(self.spell_trap_zones):
            if card is None:
                print(f"  {i+1}: Empty")
            else:
                inner = card.get('card') if isinstance(card, dict) else card
                pos = card.get('position') if isinstance(card, dict) else None
                if pos == 'face-down':
                    print(f"  {i+1}: Set Card (Face-down)")
                else:
                    print(f"  {i+1}: {inner.get('Name', 'Unknown')}")

    def show_hand(self):
        # Hand counts (excluding extra deck monsters)
        hand_m, _, hand_s, hand_t = self.count_types(self.hand)
        print(f"\nHand: {len(self.hand)} cards, {hand_m} Monsters, {hand_s} Spells, {hand_t} Traps")
        for i, card in enumerate(self.hand):
            print(f"  {i+1}: {card.get('Name') if card else 'Empty'}")

    def show_grave_banish(self):
        # Graveyard counts
        grave_m, grave_e, grave_s, grave_t = self.count_types(self.graveyard)
        print(f"\nGraveyard: {len(self.graveyard)} cards, {grave_m + grave_e} Monsters, {grave_s} Spells, {grave_t} Traps")
        for i, card in enumerate(self.graveyard):
            print(f"  {i+1}: {card.get('Name') if card else 'Empty'}")

        # Banished counts
        banish_m, banish_e, banish_s, banish_t = self.count_types(self.banished)
        print(f"\nBanishment: {len(self.banished)} cards, {banish_m + banish_e} Monsters, {banish_s} Spells, {banish_t} Traps")
        for i, card in enumerate(self.banished):
            print(f"  {i+1}: {card.get('Name') if card else 'Empty'}")

    def show_main_extra(self):
        # Main and Extra deck counts
        print(f"\nCards left in deck: {len(self.deck)} cards")

        main_mon_count, extra_mon_count, spell_count, trap_count = card_type_counts()
        print(f"\nMain Deck: {len(current_main_deck)} cards, {main_mon_count} Monsters, {spell_count} Spells, {trap_count} Traps")
        main_name_counts = Counter(card["Name"] for card in current_main_deck)
        i = 0
        for name, count in main_name_counts.items():
            print(f"  {i+1}: {name} x{count}")
            i += 1

        print(f"\nExtra Deck: {len(self.extra_deck)} cards, {extra_mon_count} Monsters")
        for i, card in enumerate(self.extra_deck):
            print(f"  {i+1}: {card.get('Name') if card else 'Empty'}")

    def place_monster_card(self, name, hand_index, face_up_down, field_zone_index = None):
        card = main_deck_monster_card_lookup.get(name)
        
        if not card:
            print(f"\nCard '{name}' not found. Please input the correct card or check spelling.")
            return False

        try:
            hand_index = int(hand_index)
            field_zone_index = int(field_zone_index)
        except ValueError:
            print("\nPlease enter numeric indices for hand_index and field_zone_index.")
            return False

        if not (0 <= hand_index < len(self.hand)):
            print("\nInvalid hand index.")
            return False

        zones = self.monster_zones
        max_index = len(zones) - 1
        if not (0 <= field_zone_index <= max_index):
            print("\nInvalid monster zone.")
            return False
        if zones[field_zone_index] is not None:
            print("\nThat monster zone is already occupied.")
            return False

        # Copy card from hand before popping
        hand_card = self.hand[hand_index].copy() if isinstance(self.hand[hand_index], dict) else self.hand[hand_index]
        if face_up_down == "summon":
            position = "face-up attack"
        elif face_up_down == "set":
            position = "face-down defense"
        else:
            print("\nNot a valid card position.")
            return False

        field_card = self.field_monster_card_properties(hand_card, position)
        zones[field_zone_index] = field_card
        self.hand.pop(hand_index)
        action_type = "Summoned" if face_up_down == "summon" else "Set"
        print(f"\n{action_type} {hand_card.get('Name', 'Unknown')} as a {position} monster in zone {field_zone_index + 1}")
        return True

    def place_spell_trap_card(self, name, hand_index, field_zone_index = None):
        card = spell_card_lookup.get(name) or trap_card_lookup.get(name)
        
        if not card:
            print(f"\nCard '{name}' not found. Please input the correct card or check spelling.")
            return False
        
        if card["Name"] in spell_card_lookup:
            card_type = "spell"
        else:
            card_type = "trap"

        try:
            hand_index = int(hand_index)
            field_zone_index = int(field_zone_index)
        except ValueError:
            print("\nPlease enter numeric indices for hand_index and field_zone_index.")
            return False

        if not (0 <= hand_index < len(self.hand)):
            print("\nInvalid hand index.")
            return False

        zones = self.spell_trap_zones
        max_index = len(zones) - 1
        if not (0 <= field_zone_index <= max_index):
            print("\nInvalid backrow zone.")
            return False
        if zones[field_zone_index] is not None:
            print("\nThat backrow zone is already occupied.")
            return False

        # Copy card from hand before popping
        hand_card = self.hand[hand_index].copy() if isinstance(self.hand[hand_index], dict) else self.hand[hand_index]
        position = "face-down"

        field_card = self.field_backrow_card_properties(hand_card, position)
        zones[field_zone_index] = field_card
        self.hand.pop(hand_index)
        print(f"\nSet the {card_type} card '{hand_card.get('Name', 'Unknown')}' in zone {field_zone_index + 1}")
        return True

    def place_field_spell(self, name, hand_index):
        card = spell_card_lookup.get(name)
        
        if not card:
            print(f"\nCard '{name}' not found. Please input the correct card or check spelling.")
            return False
        
        if card["Typing"] != "Field":
            print("\nThis card is not a field spell card.")
            return False

        try:
            hand_index = int(hand_index)
        except ValueError:
            print("\nPlease enter numeric indices for hand_index.")
            return False

        if not (0 <= hand_index < len(self.hand)):
            print("\nInvalid hand index.")
            return False

        # Copy card from hand before popping
        hand_card = self.hand[hand_index].copy() if isinstance(self.hand[hand_index], dict) else self.hand[hand_index]
        position = "face-down"
        
        field_card = self.field_spell_card_properties(hand_card, position)
        # If a field spell is already present, send it to graveyard and replace
        if self.field_spell_zone is not None:
            print(f"\n{self.field_spell_zone['card'].get('Name', 'Unknown')} was sent to the graveyard and replaced by {hand_card.get('Name', 'Unknown')}.")
            self.graveyard.append(self.field_spell_zone['card'])
        self.field_spell_zone = field_card
        self.hand.pop(hand_index)
        print(f"\nSet {hand_card.get('Name', 'Unknown')} as a {position} field spell in the field spell zone.")
        return True

    def examine_card(self, name, hand_field, zone_index = None):
        # hand_field: 'hand', 'field', 'gy', 'banish'
        # zone_index: required for field (0-based)
        hand_field = hand_field.lower()
        if hand_field not in ("hand", "field", "gy", "banish"):
            print("\nInvalid option. Please input either hand, field, gy, or banish.")
            return

        # Find the card and its field properties if on field
        if hand_field == "field":
            if zone_index is None:
                print("\nPlease provide the zone index for the card on the field.")
                return
            # Search all zones for the card
            found = False
            # Monster zones
            for i, field_card in enumerate(self.monster_zones):
                if field_card and field_card["card"].get("Name") == name and i == zone_index:
                    print(f"\nMonster Zone {i+1}:")
                    print("\nField Properties:")
                    for k, v in field_card.items():
                        if k == "card": continue
                        print(f"  {k}: {v}")
                    print("\nCard Data:")
                    for k, v in field_card["card"].items():
                        print(f"  {k}: {v}")
                    found = True
                    break
            # Spell/trap zones
            if not found:
                for i, field_card in enumerate(self.spell_trap_zones):
                    if field_card and field_card["card"].get("Name") == name and i == zone_index:
                        print(f"\nSpell/Trap Zone {i+1}:")
                        print("\nField Properties:")
                        for k, v in field_card.items():
                            if k == "card": continue
                            print(f"  {k}: {v}")
                        print("\nCard Data:")
                        for k, v in field_card["card"].items():
                            print(f"  {k}: {v}")
                        found = True
                        break
            # Field spell zone
            if not found and self.field_spell_zone and self.field_spell_zone["card"].get("Name") == name:
                print(f"\nField Spell Zone:")
                print("\nField Properties:")
                for k, v in self.field_spell_zone.items():
                    if k == "card": continue
                    print(f"  {k}: {v}")
                print("\nCard Data:")
                for k, v in self.field_spell_zone["card"].items():
                    print(f"  {k}: {v}")
                found = True
            if not found:
                print("\nCard not found in the specified field zone.")
            return

        # Otherwise, print card data from hand, gy, or banish
        if hand_field == "hand":
            for i, c in enumerate(self.hand):
                if c.get("Name") == name and i == zone_index:
                    print(f"\nHand Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in hand.")
            return
        if hand_field == "gy":
            for i, c in enumerate(self.graveyard):
                if c.get("Name") == name:
                    print(f"\nGraveyard Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in graveyard.")
            return
        if hand_field == "banish":
            for i, c in enumerate(self.banished):
                if c.get("Name") == name:
                    print(f"\nBanished Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in banished zone.")
            return
    def change_monster_position(self):
        pass

    def send_card_gy_banish(self):
        pass

    def activate_card(self):
        pass

def start_duel():
    field = PlayingField()
    field.shuffle_deck()
    field.draw_card(5)
    field.show_field()
    field.show_hand()
    return field