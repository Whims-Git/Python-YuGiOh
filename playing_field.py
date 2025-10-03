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
        # Turn and phase tracking (no actual logic)
        self.turn_count = 1
        self.current_player = 1  # 1 or 2
        self.phases = [
            "Draw Phase",
            "Standby Phase",
            "Main Phase 1",
            "Battle Phase",
            "Main Phase 2",
            "End Phase"
        ]
        self.phase_index = 0

    def print_turn_phase(self):
        print(f"\nTurn: {self.turn_count} | Player: {self.current_player} | Phase: {self.phases[self.phase_index]}")

    def next_phase(self):
        self.phase_index += 1
        if self.phase_index >= len(self.phases):
            self.phase_index = 0
            self.next_turn()
        self.print_turn_phase()

    def next_turn(self):
        self.turn_count += 1
        self.current_player = 2 if self.current_player == 1 else 1
        self.phase_index = 0
        print(f"\n--- New Turn ---")
        self.print_turn_phase()

    def shuffle_deck(self):
        random.shuffle(self.deck)
        print("\nThe deck has been shuffled.")

    def draw_card(self, n = 1):
        # On the very first turn, always draw 5 cards (ignoring n)
        if self.turn_count == 1 and len(self.hand) == 0:
            draw_amount = 5
        else:
            draw_amount = n
        for _ in range(draw_amount):
            if self.deck:
                card = self.deck.pop(0)
                self.hand.append(card)
                print(f"\nDrew card: {card.get('Name', 'Unknown')}, Remaining cards in deck: {len(self.deck)} cards")
            else:
                self.lost_condition("empty deck")

    def lost_condition(self, lost_reason):
        if lost_reason == "empty deck":
            print("\nDeck is empty! Cannot draw. You lose!")
        elif lost_reason == "0 Life Points":
            print("\nYour life points have reached 0! You lose!")
        elif lost_reason == "surrender":
            print("\nYou have surrendered the duel! You lose!")
        elif lost_reason == "alt win con":
            print("\nYou lost the duel via alternate win condition! You lose!")
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
    
    # Helper to determine a card's type between monster, spell, trap, and field spell
    def determine_card_type(self, card_name):
        if card_name in main_deck_monster_card_lookup or card_name in extra_deck_monster_card_lookup:
            return "monster"
        elif card_name in spell_card_lookup:
            if spell_card_lookup[card_name]["Type"] == "Field":
                return "field spell"
            return "spell"
        elif card_name in trap_card_lookup:
            return "trap"
        return None
    
    # Helper to move a card object to a destination list
    def move_card_obj(self, card_obj, dest):
        if dest == "gy":
            self.graveyard.append(card_obj)
        elif dest == "banish":
            self.banished.append(card_obj)
        elif dest == "hand":
            self.hand.append(card_obj)
        else:
            # 'field' moving requires a zone index and different handling
            return False
        return True

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
                    print(f"  {i+1}: {inner.get('Name', 'Unknown')} (LV {inner.get('Level')}, ATK: {inner.get('ATK')}/DEF: {inner.get('DEF')}, {pos})")

        if self.field_spell_zone is None:
            print(f"\nField Spell Zone: Empty")
        else:
            inner = self.field_spell_zone.get('card') if isinstance(self.field_spell_zone, dict) else self.field_spell_zone
            pos = self.field_spell_zone.get('position') if isinstance(self.field_spell_zone, dict) else None
            if pos == 'face-down':
                print(f"\nField Spell Zone: Set Card (Face-down)")
            else:
                print(f"\nField Spell Zone: {inner.get('Name', 'Unknown')} ({pos})")

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
                    print(f"  {i+1}: {inner.get('Name', 'Unknown')} ({inner.get('Category')}, {inner.get('Type')}, {pos})")

    def show_hand(self):
        # Hand counts (excluding extra deck monsters)
        hand_m, _, hand_s, hand_t = self.count_types(self.hand)
        print(f"\nHand: {len(self.hand)} cards, {hand_m} Monsters, {hand_s} Spells, {hand_t} Traps")
        for i, card in enumerate(self.hand):
            if card.get('Category') == "Monster":
                print(f"  {i+1}: {card.get('Name')} (Monster, LV {card.get('Level')}, {card.get('Attribute')}, {card.get('Type')})")
            else:
                print(f"  {i+1}: {card.get('Name')} ({card.get('Category')}, {card.get('Type')})")

    def show_grave_banish(self):
        # Graveyard counts
        grave_m, grave_e, grave_s, grave_t = self.count_types(self.graveyard)
        print(f"\nGraveyard: {len(self.graveyard)} cards, {grave_m + grave_e} Monsters, {grave_s} Spells, {grave_t} Traps")
        for i, card in enumerate(self.graveyard):
            if card.get('Category') == "Monster":
                print(f"  {i+1}: {card.get('Name')} (Monster, LV {card.get('Level')}, {card.get('Attribute')}, {card.get('Type')})")
            else:
                print(f"  {i+1}: {card.get('Name')} ({card.get('Category')}, {card.get('Type')})")

        # Banished counts
        banish_m, banish_e, banish_s, banish_t = self.count_types(self.banished)
        print(f"\nBanishment: {len(self.banished)} cards, {banish_m + banish_e} Monsters, {banish_s} Spells, {banish_t} Traps")
        for i, card in enumerate(self.banished):
            if card.get('Category') == "Monster":
                print(f"  {i+1}: {card.get('Name')} (Monster, LV {card.get('Level')}, {card.get('Attribute')}, {card.get('Type')})")
            else:
                print(f"  {i+1}: {card.get('Name')} ({card.get('Category')}, {card.get('Type')})")

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

    # Place cards from hand, graveyard, and banishment to field
    def place_card(self, name, from_location, index, face_up_down, field_zone_index = None, card_type = None):
        card = main_deck_monster_card_lookup.get(name) or extra_deck_monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)

        if not card:
            print(f"\nCard '{name}' not found. Please input the correct card or check spelling.")
            return False

        # Determine card type if not provided
        if card_type is None:
            card_type = self.determine_card_type(name)
            if card_type is None:
                print(f"\nCard '{name}' not found in any card pool.")
                return False

        try:
            index = int(index)
            field_zone_index = int(field_zone_index)
        except ValueError:
            print("\nPlease enter numeric indices for hand_index and field_zone_index.")
            return False

        # Validate index for the source zone
        if from_location == "hand":
            if not (0 <= index < len(self.hand)):
                print("\nInvalid hand index.")
                return False
            hand_card = self.hand[index].copy() if isinstance(self.hand[index], dict) else self.hand[index]
        elif from_location == "gy":
            if not (0 <= index < len(self.graveyard)):
                print("\nInvalid graveyard index.")
                return False
            hand_card = self.graveyard[index].copy() if isinstance(self.graveyard[index], dict) else self.graveyard[index]
        elif from_location == "banish":
            if not (0 <= index < len(self.banished)):
                print("\nInvalid banish index.")
                return False
            hand_card = self.banished[index].copy() if isinstance(self.banished[index], dict) else self.banished[index]
        else:
            print("Invalid location.")
            return False

        if face_up_down == "summon":
            if card_type in ("spell", "trap"):
                print("\nCannot summon a spell/trap card.")
                return False
            position = "face-up attack"
        elif face_up_down == "set":
            position = "face-down defense"
        else:
            print("\nNot a valid card position.")
            return False

        card_type = self.determine_card_type(name)
        if card_type == "monster":
            zones = self.monster_zones
            max_index = len(zones) - 1
            if not (0 <= field_zone_index <= max_index):
                print("\nInvalid monster zone.")
                return False
            if zones[field_zone_index] is not None:
                print("\nThat monster zone is already occupied.")
                return False
            field_card = self.field_monster_card_properties(hand_card, position)
            zones[field_zone_index] = field_card
            # Remove from the correct source
            if from_location == "gy":
                self.graveyard.pop(index)
            elif from_location == "banish":
                self.banished.pop(index)
            else:
                self.hand.pop(index)
            action_type = "Summoned" if face_up_down == "summon" else "Set"
            print(f"\n{action_type} {hand_card.get('Name', 'Unknown')} as a {position} monster in zone {field_zone_index + 1}")
            return True
        elif card_type in ("spell", "trap"):
            zones = self.spell_trap_zones
            max_index = len(zones) - 1
            if not (0 <= field_zone_index <= max_index):
                print("\nInvalid backrow zone.")
                return False
            if zones[field_zone_index] is not None:
                print("\nThat backrow zone is already occupied.")
                return False
            position = "face-down"
            field_card = self.field_backrow_card_properties(hand_card, position)
            zones[field_zone_index] = field_card
            # Remove from the correct source
            if from_location == "gy":
                self.graveyard.pop(index)
            elif from_location == "banish":
                self.banished.pop(index)
            else:
                self.hand.pop(index)
            print(f"\nSet the {card_type} card '{hand_card.get('Name', 'Unknown')}' in zone {field_zone_index + 1}")
            return True
        elif card_type == "field spell":
            position = "face-down"
            field_card = self.field_spell_card_properties(hand_card, position)
            # If a field spell is already present, send it to graveyard and replace
            if self.field_spell_zone is not None:
                print(f"\n{self.field_spell_zone['card'].get('Name', 'Unknown')} was sent to the graveyard and replaced by {hand_card.get('Name', 'Unknown')}.")
                self.graveyard.append(self.field_spell_zone['card'])
            self.field_spell_zone = field_card
            # Remove from the correct source
            if from_location == "gy":
                self.graveyard.pop(index)
            elif from_location == "banish":
                self.banished.pop(index)
            else:
                self.hand.pop(index)
            print(f"\nSet {hand_card.get('Name', 'Unknown')} as a {position} field spell in the field spell zone.")
            return True

    def examine_card(self, name, location, zone_index = None):
        # location: 'hand', 'field', 'gy', 'banish'
        # zone_index: required for field (0-based)
        location = location.lower()
        if location not in ("hand", "field", "gy", "banish"):
            print("\nInvalid option. Please input either hand, field, gy, or banish.")
            return

        # Find the card and its field properties if on field
        if location == "field":
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
        if location == "hand": # Examine card in hand
            for i, c in enumerate(self.hand):
                if c.get("Name") == name and i == zone_index:
                    print(f"\nHand Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in hand.")
            return
        if location == "gy": # Examine card in graveyard
            for i, c in enumerate(self.graveyard):
                if c.get("Name") == name:
                    print(f"\nGraveyard Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in graveyard.")
            return
        if location == "banish": # Examine card in banishment
            for i, c in enumerate(self.banished):
                if c.get("Name") == name:
                    print(f"\nBanished Card {i+1}:")
                    for k, v in c.items():
                        print(f"  {k}: {v}")
                    return
            print("\nCard not found in banished zone.")
            return

    def change_monster_position(self, name, zone_index, face_position):
        # Translate requested shorthand to full position string
        if face_position == "atk":
            requested_position = "face-up attack"
        elif face_position == "def":
            requested_position = "face-up defense"
        else:
            print("\nNot a valid card position. Use 'atk' or 'def'.")
            return False

        if zone_index is None:
            print("\nPlease provide the zone index for the card on the field.")
            return False

        # Ensure zone_index is within bounds
        try:
            zi = int(zone_index)
        except (ValueError, TypeError):
            print("\nZone index must be an integer.")
            return False

        if not (0 <= zi < len(self.monster_zones)):
            print("\nInvalid monster zone index.")
            return False

        field_card = self.monster_zones[zi]
        if not field_card or not isinstance(field_card, dict):
            print("\nNo monster found in that zone.")
            return False

        current_position = field_card.get("position")

        # If already in requested position
        if current_position == requested_position:
            print(f"\n{name} is already in {current_position} position.")
            return True

        # If currently in defense (face-up defense or face-down defense) and requesting atk -> flip face-up attack
        if current_position in ("face-up defense", "face-down defense") and requested_position == "face-up attack":
            # Changing defense to face-up attack
            field_card["position"] = "face-up attack"
            if current_position == "face-down defense":
                print(f"\n{name} was flipped from {current_position} to face-up attack.")
            else:
                print(f"\n{name} was changed from {current_position} to face-up attack.")
            return True

        # If currently face-up attack and requesting def -> change to face-up defense
        if current_position == "face-up attack" and requested_position == "face-up defense":
            field_card["position"] = "face-up defense"
            print(f"\n{name} was changed from face-up attack to face-up defense.")
            return True

        # Any other transitions are not allowed (e.g., changing face-up attack directly to face-down defense)
        print(f"\nCannot change {name} from {current_position} to {requested_position} directly.")
        return False

    # Move cards from field, hand, graveyard, and banishment -> hand, graveyard, and banishment but not field.
    def move_cards(self, name, from_location, index, to_location, card_type = None):
        # Normalize and validate locations
        if not isinstance(from_location, str) or not isinstance(to_location, str):
            print("\nfrom_location and to_location must be strings: 'hand','field','gy', or 'banish'.")
            return False
        from_location = from_location.lower()
        to_location = to_location.lower()
        if from_location not in ("hand", "field", "gy", "banish") or to_location not in ("hand", "field", "gy", "banish"):
            print("\nInvalid option. Please input either hand, field, gy, or banish.")
            return False

        # Determine card type if not provided
        if card_type is None:
            card_type = self.determine_card_type(name)
            if card_type is None:
                print(f"\nCard '{name}' not found in any card pool.")
                return False

        # Moving monster/spell/trap/field spell cards from field -> hand/gy/banish
        if from_location == "field" and card_type == "monster":
            if index is None:
                print("\nPlease provide the zone index for the card on the field.")
                return False
            try:
                zi = int(index)
            except (ValueError, TypeError):
                print("\nZone index must be an integer.")
                return False
            if not (0 <= zi < len(self.monster_zones)):
                print("\nInvalid monster zone index.")
                return False
            field_card = self.monster_zones[zi]
            if not field_card or not isinstance(field_card, dict) or field_card.get('card', {}).get('Name') != name:
                print("\nCard not found in the specified field zone.")
                return False
            # Remove from field (clear zone)
            card_obj = field_card['card']
            self.monster_zones[zi] = None
            if to_location in ("hand", "gy", "banish"):
                moved = self.move_card_obj(card_obj, to_location)
                if moved:
                    print(f"\n{card_obj.get('Name', 'Unknown')} was moved from field zone {zi+1} to {to_location}.")
                    return True
                else:
                    print("\nCannot move directly to field without specifying a zone.")
                    return False
        elif from_location == "field" and card_type in ("spell", "trap"):
            if index is None:
                print("\nPlease provide the zone index for the card on the field.")
                return False
            try:
                zi = int(index)
            except (ValueError, TypeError):
                print("\nZone index must be an integer.")
                return False
            if not (0 <= zi < len(self.spell_trap_zones)):
                print("\nInvalid backrow zone index.")
                return False
            field_card = self.spell_trap_zones[zi]
            if not field_card or not isinstance(field_card, dict) or field_card.get('card', {}).get('Name') != name:
                print("\nCard not found in the specified field zone.")
                return False
            # Remove from field (clear zone)
            card_obj = field_card['card']
            self.spell_trap_zones[zi] = None
            if to_location in ("hand", "gy", "banish"):
                moved = self.move_card_obj(card_obj, to_location)
                if moved:
                    print(f"\n{card_obj.get('Name', 'Unknown')} was moved from field zone {zi+1} to {to_location}.")
                    return True
                else:
                    print("\nCannot move directly to field without specifying a zone.")
                    return False
        elif from_location == "field" and card_type == "field spell":
            if self.field_spell_zone is None:
                print("\nNo field spell card found in the field spell zone.")
                return False

            field_card = self.field_spell_zone.get('card')
            if not field_card or field_card.get('Name') != name:
                print(f"\nCard '{name}' not found in field spell zone.")
                return False

            # Copy card before removing from field
            card_obj = field_card.copy()
            # Clear the field spell zone
            self.field_spell_zone = None

            if to_location in ("hand","gy", "banish"):
                moved = self.move_card_obj(card_obj, to_location)
                if moved:
                    print(f"\n{card_obj.get('Name', 'Unknown')} was moved from field spell zone to {to_location}.")
                    return True
            return False

        # Moving from hand -> gy/banish
        if from_location == "hand":
            if index is None:
                print("\nPlease provide the index in the hand.")
                return False
            try:
                hi = int(index)
            except (ValueError, TypeError):
                print("\nHand index must be an integer.")
                return False
            if not (0 <= hi < len(self.hand)):
                print("\nInvalid hand index.")
                return False
            hand_card = self.hand[hi]
            if not hand_card or hand_card.get('Name') != name:
                print("\nCard not found in the specified hand location.")
                return False
            # Remove from hand
            card_obj = self.hand.pop(hi)
            if to_location in ("gy", "banish"):
                self.move_card_obj(card_obj, to_location)
                print(f"\n{card_obj.get('Name', 'Unknown')} was moved from hand to {to_location}.")
                return True
            if to_location == "field" or to_location == "hand":
                print("\nCannot move the card to this area.")
                # Put it back into hand to avoid accidental loss
                self.hand.insert(hi, card_obj)
                return False

        # Moving from gy -> hand/banish
        if from_location == "gy":
            if index is None:
                print("\nPlease provide the index in the graveyard.")
                return False
            try:
                gi = int(index)
            except (ValueError, TypeError):
                print("\nGraveyard index must be an integer.")
                return False
            if not (0 <= gi < len(self.graveyard)):
                print("\nInvalid graveyard index.")
                return False
            gy_card = self.graveyard[gi]
            if not gy_card or gy_card.get('Name') != name:
                print("\nCard not found in the specified graveyard location.")
                return False
            card_obj = self.graveyard.pop(gi)
            if to_location in ("hand", "banish"):
                self.move_card_obj(card_obj, to_location)
                print(f"\n{card_obj.get('Name', 'Unknown')} was moved from graveyard to {to_location}.")
                return True
            if to_location == "field" or to_location == "gy":
                print("\nCannot move the card to this area.")
                # Return card to graveyard
                self.graveyard.insert(gi, card_obj)
                return False

        # Moving from banish -> hand/gy
        if from_location == "banish":
            if index is None:
                print("\nPlease provide the index in the banished zone (0-based).")
                return False
            try:
                bi = int(index)
            except (ValueError, TypeError):
                print("\nBanished index must be an integer.")
                return False
            if not (0 <= bi < len(self.banished)):
                print("\nInvalid banished index.")
                return False
            bx_card = self.banished[bi]
            if not bx_card or bx_card.get('Name') != name:
                print("\nCard not found in the specified banished location.")
                return False
            card_obj = self.banished.pop(bi)
            if to_location in ("hand", "gy"):
                self.move_card_obj(card_obj, to_location)
                print(f"\n{card_obj.get('Name', 'Unknown')} was moved from banished to {to_location}.")
                return True
            if to_location == "field" or to_location == "banish":
                print("\nCannot move the card to this area.")
                # Return card to banished
                self.banished.insert(bi, card_obj)
                return False

        print("\nUnsupported move or invalid parameters.")
        return False
    
    def activate_card(self, name, location, index, field_zone_index, card_type = None):
        card = main_deck_monster_card_lookup.get(name) or extra_deck_monster_card_lookup.get(name) or spell_card_lookup.get(name) or trap_card_lookup.get(name)

        if not card:
            print(f"\nCard '{name}' not found. Please input the correct card or check spelling.")
            return False

        if not isinstance(location, str):
            print("\nLocation must be strings: 'field', 'hand', 'gy', or 'banish'.")
            return False
        location = location.lower()
        if location not in ("hand", "field", "gy", "banish"):
            print("\nInvalid option. Please input either field, hand, gy, or banish.")
            return False
        
        if index is None:
                print("\nPlease provide the index for the card or field zone.")
                return False
        try:
            index = int(index)
            field_zone_index = int(field_zone_index)
        except (ValueError, TypeError):
            print("\nIndex must be an integer.")
            return False

        # Determine card type if not provided
        if card_type is None:
            card_type = self.determine_card_type(name)
            if card_type is None:
                print(f"\nCard '{name}' not found in any card pool.")
                return False
        
        # If spell/trap, especially field spells, is activated from the hand, place it on field in face-up position first
        if location == "hand" and card_type in ("spell", "trap"):
            if field_zone_index is None:
                print("\nPlease provide the field index for the field zone.")
                return False
            
            # Place card from hand to field in face-up position
            if not (0 <= index < len(self.hand)):
                print("\nInvalid hand index.")
                return False
            hand_card = self.hand[index].copy() if isinstance(self.hand[index], dict) else self.hand[index]
            zones = self.spell_trap_zones
            max_index = len(zones) - 1
            if not (0 <= field_zone_index <= max_index):
                print("\nInvalid backrow zone.")
                return False
            if zones[field_zone_index] is not None:
                print("\nThat backrow zone is already occupied.")
                return False
            position = "face-up"
            field_card = self.field_backrow_card_properties(hand_card, position)
            zones[field_zone_index] = field_card
            # Remove from the correct source
            self.hand.pop(index)
            print(f"\nThe {card_type} card '{hand_card.get('Name', 'Unknown')}' was activated in zone {field_zone_index + 1}")
            return True
        elif location == "hand" and card_type == "field spell":
            if not (0 <= index < len(self.hand)):
                print("\nInvalid hand index.")
                return False
            hand_card = self.hand[index].copy() if isinstance(self.hand[index], dict) else self.hand[index]
            position = "face-up"
            field_card = self.field_spell_card_properties(hand_card, position)
            # If a field spell is already present, send it to graveyard and replace
            if self.field_spell_zone is not None:
                print(f"\n{self.field_spell_zone['card'].get('Name', 'Unknown')} was sent to the graveyard and replaced by {hand_card.get('Name', 'Unknown')}.")
                self.graveyard.append(self.field_spell_zone['card'])
            self.field_spell_zone = field_card
            # Remove from the correct source
            self.hand.pop(index)
            print(f"\nThe {card_type} card '{hand_card.get('Name', 'Unknown')}' was activated as a {position} field spell in the field spell zone.")
            return True
        else: # Cards activated from the field, gy, and banishment need no extra action
            print(f"\nThe {card_type} card '{card.get('Name', 'Unknown')}' was activated from the {location}")

def start_duel():
    field = PlayingField()
    field.shuffle_deck()
    field.print_turn_phase()
    field.draw_card()
    field.show_field()
    field.show_hand()
    return field