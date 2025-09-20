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

        if choice == "1":
            deck_building.show_deck()
        elif choice == "2":
            search_card_pool()
            # deck_building.list_all_cards()
        elif choice == "3":
            card_name = input("\nEnter the name of the card to search: ")
            deck_building.search_card(card_name)
        elif choice == "4":
            #card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
            #deck_building.add_card_to_deck(card_name, card_qty)
            deck_building.add_card_to_deck("Dark Magician", "3")
            deck_building.add_card_to_deck("Blue-Eyes White Dragon", "3")
            deck_building.add_card_to_deck("Pot of Greed", "3")
            deck_building.add_card_to_deck("Two-Pronged Attack", "2")
            deck_building.add_card_to_deck("Charubin the Fire Knight", "1")
        elif choice == "5":
            card_name, card_qty = input("\nEnter the card name and the amount to be removed, separated by a comma: ").split(',')
            deck_building.remove_card_from_deck(card_name, card_qty)
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def duel_actions_menu(field):
    while True:
        print("\nActions Menu")
        print("1. Examine Card in hand or on field")
        print("2. Examine field")
        print("3. Examine graveyard/banishment")
        print("4. Summon/Set Monster or Set Spell/Trap From Hand")
        print("5. Change Monster Card Position")
        print("6. Activate Card Effect")
        print("7. Send Card to GY/Banishment")
        print("8. Show main/extra deck")
        print("9. Quit")
        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            card_name, hand_field = input("\nEnter the card name and either 'hand' or 'field', separated by a comma: ").split(',')
            field.examine_card(card_name.strip(), hand_field.strip())
        elif choice == "2":
            field.show_field_hand()
        elif choice == "3":
            field.show_grave_banish()
        elif choice == "4":
            card_name, hand_index, face_up_down, field_zone_index = input("\nEnter the card name, position in hand, either 'summon' or 'set', and field zone # (L -> R, Zone 1-5), separated by a comma: ").split(',')
            field.place_card_field(card_name.strip(), hand_index.strip(), face_up_down.strip(), field_zone_index.strip())
            field.show_field_hand()
        elif choice == "5":
            card_name, card_position = input("\nEnter the card name and either 'atk' or 'def', separated by a comma: ").split(',')
            field.change_monster_position(card_name.strip(), card_position.strip())
            field.show_field_hand()
        elif choice == "6":
            card_name = input("\nEnter the name of the card to activate its effect: ")
            field.activate_card(card_name.strip())
            print(f"{card_name} activated its effect.")
        elif choice == "7":
            card_name, send_card = input("\nEnter the name of the card and either 'gy' or 'banish', separated by a comma: ").split(',')
            field.send_card_gy_banish(card_name.strip(), send_card.strip())
        elif choice == "8":
            field.show_main_extra()
        elif choice == "9":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

def search_card_pool():
    while True:
        print("\nSelect Catagory of Cards to View")
        print("1. Vanilla Monsters")
        print("2. Main Deck Effect Monsters")
        print("3. Fusion Monsters")
        print("4. Spell Cards")
        print("5. Trap Cards")
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            deck_building.list_all_vanillas()
        elif choice == "2":
            deck_building.list_all_main_effects()
        elif choice == "3":
            deck_building.list_all_fusions()
        elif choice == "4":
            deck_building.list_all_spells()
        elif choice == "5":
            deck_building.list_all_traps()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

def main_menu():
    while True:
        print("\nYu-Gi-Oh! Main Menu")
        print("1. Duel")
        print("2. Deck Build")
        print("3. Pull Cards (Not implemented)")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            print("\nDuel!")
            field = playing_field.start_duel()
            duel_actions_menu(field)
        elif choice == "2":
            deck_building_menu()
        elif choice == "3":
            #pull_cards_menu()
            print("Pull Cards is not implemented yet.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main_menu()