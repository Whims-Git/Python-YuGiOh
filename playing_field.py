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
    show_deck,
    card_type_counts,
    main_deck_monster_card_lookup,
    extra_deck_monster_card_lookup,
    spell_card_lookup,
    trap_card_lookup,
)

import random
from collections import Counter

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

    def draw_card(self, n = 1):
        for _ in range(n):
            if self.deck:
                card = self.deck.pop(0)
                self.hand.append(card)
                print(f"\nDrew card: {card.get('Name', 'Unknown')}")
            else:
                print("\nDeck is empty! Cannot draw.")

    # Create a field card dictionary for dynamic properties
    def field_monster_card_properties(self, card, position = "face-up attack"):
        return {
            "card": card,  # Original card data
            "position": position,  # face-up attack, face-down defense
            "equipped_cards": [],  # Cards equipped to this card
            "counters": 0,  # Counter tokens on card
            "affected_by": [],  # Card effects currently affecting this card
            "attack_modifier": 0,  # Changes to original ATK
            "defense_modifier": 0,  # Changes to original DEF
            "cannot_attack": False,  # If card is prevented from attacking
            "cannot_change_position": False,  # If card cannot change battle position
        }
    
    def field_backrow_card_properties(self, card, position = "face-up"):
        return {
            "card": card,  # Original card data
            "position": position,  # face-up, face-down
            #"equipped_to": equipped_monster,  # monster this card is equipped to
            "counters": 0,  # Counter tokens on card
            "affected_by": [],  # Card effects currently affecting this card
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

    def show_field_hand(self):
        print("\nMonster Zones (Left -> Right):")
        for i, card in enumerate(self.monster_zones):
            if card is None:
                print(f"  {i+1}: Empty")
            else:
                # card on field is a dict with 'card' key
                inner = card.get('card') if isinstance(card, dict) else card
                print(f"  {i+1}: {inner.get('Name', 'Unknown')}")

        if self.field_zone is None:
            print(f"\nField Spell Zone: Empty")
        else:
            fz = self.field_zone.get('card') if isinstance(self.field_zone, dict) else self.field_zone
            print(f"\nField Spell Zone: {fz.get('Name', 'Unknown')}")

        print("\nSpell/Trap Zones (Left -> Right):")
        for i, card in enumerate(self.spell_trap_zones):
            if card is None:
                print(f"  {i+1}: Empty")
            else:
                inner = card.get('card') if isinstance(card, dict) else card
                # hide name if face-down
                pos = card.get('position') if isinstance(card, dict) else None
                if pos == 'face-down':
                    print(f"  {i+1}: Set Card (Face-down)")
                else:
                    print(f"  {i+1}: {inner.get('Name', 'Unknown')}")

        # Hand counts (excluding extra deck monsters)
        hand_m, _, hand_s, hand_t = self.count_types(self.hand)  # Exclude extra deck count
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

    def place_card_field(self, name, hand_index, face_up_down, field_zone_index):
        card = (
            main_deck_monster_card_lookup.get(name)
            or extra_deck_monster_card_lookup.get(name)
            or spell_card_lookup.get(name)
            or trap_card_lookup.get(name)
        )

        if not card:
            print(f"Card '{name}' not found.")
            return False

        try:
            hand_index = int(hand_index)
            field_zone_index = int(field_zone_index)
        except ValueError:
            print("Please enter numeric indices for hand_index and field_zone_index.")
            return False

        if not (0 <= hand_index < len(self.hand)):
            print("Invalid hand index.")
            return False

        # Determine card type by name membership
        is_monster = name in main_deck_monster_card_lookup or name in extra_deck_monster_card_lookup
        is_spell = name in spell_card_lookup
        is_trap = name in trap_card_lookup

        # Choose zone, position and create the field card wrapper
        if is_monster:
            hand_card = self.hand[hand_index]
            if face_up_down == "summon":
                position = "face-up attack"
            else:
                position = "face-down defense"
            zones = self.monster_zones
            max_index = len(zones) - 1
            field_card = self.field_monster_card_properties(hand_card, position)
        else:
            hand_card = self.hand[hand_index]
            if face_up_down == "summon":
                print("Not a valid action for a spell/trap.")
                return False
            elif face_up_down == "set":
                position = "face-down"
            else:
                position = "face-up"
            zones = self.spell_trap_zones
            max_index = len(zones) - 1
            field_card = self.field_backrow_card_properties(hand_card, position)

        if not (0 <= field_zone_index <= max_index):
            print("Invalid zone.")
            return False

        if zones[field_zone_index] is not None:
            print("That zone is already occupied.")
            return False

        # Place card and remove from hand
        zones[field_zone_index - 1] = field_card
        self.hand.pop(hand_index)

        action_type = "Summoned" if face_up_down == "summon" else "Set"
        card_type = "monster" if is_monster else "spell/trap card"
        print(f"\n{action_type} {card.get('Name', 'Unknown')} as a {position} {card_type} in zone {field_zone_index}")

        return True

    def examine_card(self):
        pass

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
    field.show_field_hand()
    return field