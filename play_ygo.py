import deck_building
import playing_field

def deck_building_menu():
    while True:
        print("\nDeck Building Menu")
        print("1. View Current Deck")
        print("2. View Card Pool")
        print("3. Search and View Card Details")
        print("4. Add Card(s) to Deck")
        print("5. Remove Card(s) from Deck")
        print("6. Return to Main Menu")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1": # View Current Deck
            deck_building.show_deck()
        elif choice == "2": # View Card Pool
            search_card_pool()
            # deck_building.list_all_cards()
        elif choice == "3": # Search and View Card Details
            card_name = input("\nEnter the name of the card to search: ")
            deck_building.search_card(card_name)
        elif choice == "4": # Add Card(s) to Deck
            #card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
            #deck_building.add_card_to_deck(card_name, card_qty)
            deck_building.add_card_to_deck("Dark Magician", "3")
            # deck_building.add_card_to_deck("Blue-Eyes White Dragon", "3")
            deck_building.add_card_to_deck("Pot of Greed", "2")
            deck_building.add_card_to_deck("Two-Pronged Attack", "2")
            deck_building.add_card_to_deck("Forest", "2")
            # deck_building.add_card_to_deck("Charubin the Fire Knight", "1")
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
        print("\nActions Menu")
        print("1. Examine card - field/hand/graveyard/banishment")
        print("2. Summon/Set card to Field")
        print("3. Change monster card position on field")
        print("4. Activate card effect")
        print("5. Move a card field/hand/gy/banishment <-> hand/gy/banishment")
        print("6. Show main/extra deck")
        print("7. Quit")
        choice = input("\nEnter your choice (1-7): ")

        if choice == "1": # Examine card - field/hand/graveyard/banishment
            field.show_hand()
            card_name, location, location_index = input("\nEnter the card name, location: 'field', 'hand', 'gy', or 'banish', " \
            "and the index of the card, separated by a comma:\n").split(',')
            location_index = int(location_index.strip()) - 1
            field.examine_card(card_name, location.strip(), location_index)
        elif choice == "2": # Summon/Set card to Field
            field.show_hand()
            field.show_grave_banish()
            card_name, from_location, hand_index, face_up_down, field_zone_index = input("\nEnter the monster card name, location: 'hand', 'gy', or 'banish', " \
            "index of card, either 'summon' or 'set', and field zone for monsters and spells/traps, separated by a comma:\n").split(',')
            hand_index = int(hand_index.strip()) - 1
            field_zone_index = int(field_zone_index.strip()) - 1
            field.place_card(card_name.strip(), from_location.strip(), hand_index, face_up_down.strip(), field_zone_index)
            field.show_field()
        elif choice == "3": # Change monster card position on field
            field.show_field()
            card_name, field_zone_index, card_position = input("\nEnter the monster card name, the zone number, "
            "and either 'atk' or 'def', separated by a comma:\n").split(',')
            field_zone_index = int(field_zone_index.strip()) - 1
            field.change_monster_position(card_name.strip(), field_zone_index, card_position.strip())
            field.show_field()
        elif choice == "4": # Activate card effect
            card_name = input("\nEnter the name of the card to activate its effect:\n")
            field.activate_card(card_name.strip())
            print(f"\n{card_name} activated its effect.")
        elif choice == "5": # Move a card field/hand/gy/banishment <-> hand/gy/banishment
            field.show_field()
            card_name, from_location, index, to_location = input("\nEnter the name of the card, from location: 'field', 'hand', 'gy', or 'banish', " \
            "the index, and to location: 'hand', 'gy', or 'banish', separated by a comma:\n").split(',')
            index = int(index.strip()) - 1
            field.move_cards(card_name.strip(), from_location.strip(), index, to_location.strip())
            field.show_grave_banish()
            field.show_field()
        elif choice == "6": # Show main/extra deck
            field.show_main_extra()
        elif choice == "7": # Quit
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

def search_card_pool():
    while True:
        print("\nSelect Category of Cards to View")
        print("1. Vanilla Monsters")
        print("2. Main Deck Effect Monsters")
        print("3. Fusion Monsters")
        print("4. Spell Cards")
        print("5. Trap Cards")
        print("6. Quit")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1": # Vanilla Monsters
            deck_building.list_all_vanillas()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "2": # Main Deck Effect Monsters
            deck_building.list_all_main_effects()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "3": # Fusion Monsters
            deck_building.list_all_fusions()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "4": # Spell Cards
            deck_building.list_all_spells()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "5": #Trap Cards
            deck_building.list_all_traps()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "6":
            print("\nReturning to deck building menu.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

def main_menu():
    while True:
        print("\nYu-Gi-Oh! Main Menu")
        print("1. Duel")
        print("2. Deck Build")
        print("3. Pull Cards (Not implemented)")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1": # Duel
            print("\nDuel!")
            field = playing_field.start_duel()
            duel_actions_menu(field)
        elif choice == "2": # Deck Build
            deck_building_menu()
        elif choice == "3": # Pull Cards
            #pull_cards_menu()
            print("Pull Cards is not implemented yet.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()