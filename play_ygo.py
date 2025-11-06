import deck_building
import playing_field
import card_pulling

def deck_building_menu():
    while True:
        print("\nDeck Building Menu\n" \
        "1. View Current Deck\n" \
        "2. View Card Pool\n" \
        "3. Search and View Card Details\n" \
        "4. Add Card(s) to Deck\n" \
        "5. Remove Card(s) from Deck\n" \
        "6. Return to Main Menu\n")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1": # View Current Deck
            deck_building.show_deck()
        elif choice == "2": # View Card Pool
            search_card_pool()
        elif choice == "3": # Search and View Card Details
            card_name = input("\nEnter the name of the card to search: ")
            deck_building.search_card(card_name)
        elif choice == "4": # Add Card(s) to Deck
            card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name, card_qty)
        elif choice == "5": # Remove Card(s) from Deck
            card_name, card_qty = input("\nEnter the card name and the amount to be removed, separated by a comma: ").split(',')
            deck_building.remove_card_from_deck(card_name, card_qty)
        elif choice == "6": # Return to Main Menu
            print("\nReturning to Main Menu...")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

def duel_actions_menu(field):
    while True:
        print("\nActions Menu\n" \
        "1. Examine card - field/hand/graveyard/banishment\n" \
        "2. Summon/Set card to Field\n" \
        "3. Declare Attack\n" \
        "4. Change monster card position on field\n" \
        "5. Activate card effect\n" \
        "6. Move a card field/hand/gy/banishment <-> hand/gy/banishment\n" \
        "7. Show main/extra deck\n" \
        "8. Continue to next phase\n" \
        "9. Quit\n")
        choice = input("\nEnter your choice (1-9): ")

        if choice == "1": # Examine card - field/hand/graveyard/banishment
            field.show_hand()
            card_name, location = input("\nEnter the card name and the location: 'field', 'hand', 'gy', or 'banish', separated by a comma:\n").split(',')
            card_type = field.determine_card_type(card_name)
            if card_type != "field spell":
                location_index = int(input("\nEnter the index of the card:\n").strip()) - 1
            else:
                location_index = 0
            field.examine_card(card_name, location.strip(), location_index)
        elif choice == "2": # Summon/Set card to Field
            field.show_field()
            field.show_hand()
            field.show_grave_banish()
            card_name, from_location, hand_index, face_up_down = input("\nEnter the card name, location: 'hand', 'gy', or 'banish', " \
            "index of card, and either 'summon' or 'set', separated by a comma:\n").split(',')
            card_type = field.determine_card_type(card_name)
            if card_type != "field spell":
                field_zone_index = int(input("\nEnter the field zone:\n").strip()) - 1
            else:
                field_zone_index = 0
            hand_index = int(hand_index.strip()) - 1
            field.place_card(card_name.strip(), from_location.strip(), hand_index, face_up_down.strip(), field_zone_index)
            if from_location == "hand":
                field.show_hand()
                field.show_field()
            else:
                field.show_grave_banish()
                field.show_field()
        elif choice == "3": # Declare Attack
            field.show_field()
            # Opponent's field not implamented
            attacker_name, attacker_zone_index, target = input("\nEnter the attacking monster name, its zone number, and " \
            "the attack target: 'monster' or 'player'\n").split(',')
            attacker_zone_index = int(attacker_zone_index.strip()) - 1
            if target == "monster":
                pass
                # defender_name, defender_zone_index = input("\nthe attack target's name, and its zone number, separated by a comma:\n").split(',')
                # field.declare_attack(attacker_name.strip(), attacker_zone_index) # defender_name.strip(), defender_zone_index
            else:
                print(f"\n{attacker_name} attacked the opponenet directly.")
            # defender_zone_index = int(defender_zone_index.strip()) - 1
            field.show_field()
        elif choice == "4": # Change monster card position on field
            field.show_field()
            card_name, field_zone_index, card_position = input("\nEnter the monster card name, the zone number, "
            "and either 'atk' or 'def', separated by a comma:\n").split(',')
            field_zone_index = int(field_zone_index.strip()) - 1
            field.change_monster_position(card_name.strip(), field_zone_index, card_position.strip())
            field.show_field()
        elif choice == "5": # Activate card effect
            field.show_hand()
            field.show_field()
            field.show_grave_banish()
            card_name, from_location, index = input("\nEnter the card name, the location: 'field', 'hand', 'gy', or 'banish' and " \
            "index of card, separated by a comma:\n").split(',')
            card_type = field.determine_card_type(card_name)
            if from_location.strip() == "hand" and card_type != "field spell":
                field_zone_index = int(input("\nEnter the field zone for cards only from the hand:\n").strip()) - 1
            else:
                field_zone_index = 0
            index = int(index.strip()) - 1
            field.activate_card(card_name.strip(), from_location.strip(), index, field_zone_index)
            if from_location.strip() == "hand":
                field.show_hand()
                field.show_field()
        elif choice == "6": # Move a card field/hand/gy/banishment <-> hand/gy/banishment
            field.show_hand()
            field.show_field()
            field.show_grave_banish()
            card_name, from_location, index = input("\nEnter the name of the card, the from location: 'field', 'hand', 'gy', or 'banish', " \
            "and the index, separated by a comma:\n").split(',')
            to_location = input("\nEnter the to location: 'hand', 'gy', or 'banish' (From location and to location cannot be the same):\n")
            index = int(index.strip()) - 1
            field.move_cards(card_name.strip(), from_location.strip(), index, to_location.strip())
            if from_location == "field" and to_location == "hand":
                field.show_field()
                field.show_hand()
            elif from_location == "field" and to_location in ["gy", "banish"]:
                field.show_field()
                field.show_grave_banish()
            elif from_location == "hand" and to_location in ["gy", "banish"]:
                field.show_hand()
                field.show_grave_banish()
            elif from_location in ["gy", "banish"] and to_location == "hand":
                field.show_grave_banish()
                field.show_hand()
            else:
                field.show_grave_banish()
        elif choice == "7": # Show main/extra deck
            field.show_main_extra()
        elif choice == "8": # Continue to next phase
            field.next_phase()
        elif choice == "9": # Quit
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

def pull_cards_menu():
    while True:
        print("\nPull Packs!\n" \
        "1. View all the cards in a pack\n" \
        "2. Pull from a pack\n" \
        "3. View your card collection\n" \
        "4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1": # View all the cards in a pack
            print("\nAvaliable Card Packs!\n" \
            "1. Legend of Blue Eyes White Dragon ('Blue-Eyes' for input)\n" \
            "2. Metal Raiders\n" \
            "3. Magic Ruler")
            pack_name = input("\nPlease input which pack you wish to view:\n")
            if pack_name.strip() == "Blue-Eyes":
                pack_name = "Legend of Blue Eyes White Dragon"
            card_pulling.list_cards_in_pack(pack_name.strip())
        elif choice == "2": # Pull from a pack
            print("\nChoose an avaliable card pack to pull from\n" \
            "1. Legend of Blue Eyes White Dragon ('Blue-Eyes' for input)\n" \
            "2. Metal Raiders\n" \
            "3. Magic Ruler")
            pack_name, pack_qty = input("\nPlease input which pack you wish to pull from and the number of packs (max 10), separated by a comma:\n").split(',')
            if pack_name.strip() == "Blue-Eyes":
                pack_name = "Legend of Blue Eyes White Dragon"
            try:
                pack_qty = int(pack_qty.strip())
            except ValueError:
                print("\nInvalid number of packs. Please enter a valid integer.")
                continue
            card_pulling.pull_card_from_pack(pack_name.strip(), pack_qty)
        elif choice == "3": # View your card collection
            card_pulling.list_player_pulled_cards()
        elif choice == "4": # Quit
            print("\nReturning to main menu.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 4.")

def search_card_pool():
    while True:
        print("\nSelect Category of Cards to View\n" \
        "1. Vanilla Monsters\n" \
        "2. Main Deck Effect Monsters\n" \
        "3. Fusion Monsters\n" \
        "4. Spell Cards\n" \
        "5. Trap Cards\n" \
        "6. Quit")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1": # Vanilla Monsters
            deck_building.list_all_vanillas()
            add_card = input("\nWould you like to add a card to your deck? (y/n)\n")
            if add_card == "y":
                card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
                deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "2": # Main Deck Effect Monsters
            deck_building.list_all_main_effects()
            add_card = input("\nWould you like to add a card to your deck? (y/n)\n")
            if add_card == "y":
                card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
                deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "3": # Fusion Monsters
            deck_building.list_all_fusions()
            add_card = input("\nWould you like to add a card to your deck? (y/n)\n")
            if add_card == "y":
                card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
                deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "4": # Spell Cards
            deck_building.list_all_spells()
            add_card = input("\nWould you like to add a card to your deck? (y/n)\n")
            if add_card == "y":
                card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
                deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "5": #Trap Cards
            deck_building.list_all_traps()
            add_card = input("\nWould you like to add a card to your deck? (y/n)\n")
            if add_card == "y":
                card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma:\n").split(',')
                deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "6":
            print("\nReturning to deck building menu.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

def main_menu():
    while True:
        print("\nYu-Gi-Oh! Main Menu\n" \
        "1. Duel\n" \
        "2. Deck Build\n" \
        "3. Pull Cards\n" \
        "4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1": # Duel
            print("\nDuel!")
            field = playing_field.start_duel()
            duel_actions_menu(field)
        elif choice == "2": # Deck Build
            deck_building_menu()
        elif choice == "3": # Pull Cards
            pull_cards_menu()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()