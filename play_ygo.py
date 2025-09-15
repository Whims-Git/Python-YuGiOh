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
            deck_building.list_all_cards()
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

def duel_actions_menu():
    while True:
        print("\nActions Menu")
        print("1. Examine Card in hand or on field")
        print("2. Summon/Set Monster or Set Spell/Trap From Hand")
        print("3. Change Monster Card Position")
        print("4. Activate Card Effect")
        print("5. Send Card to GY/Banishment")
        print("6. Quit")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            pass
            card_name, hand_field = input("\nEnter the card name and either 'hand' or 'field', separated by a comma: ").split(',')
            playing_field.examine_card(card_name, hand_field)
        elif choice == "2":
            card_name, hand_index, face_up_down, field_zone_index = input("\nEnter the card name, position in hand, either 'summon' or 'set', and field zone # (L -> R, Zone 1-5), separated by a comma: ").split(',')
            playing_field.place_card_field(card_name, hand_index, face_up_down, field_zone_index)
        elif choice == "3":
            pass
            card_name, card_position = input("\nEnter the card name and either 'atk' or 'def', separated by a comma: ").split(',')
            deck_building.change_monster_position(card_name, card_position)
        elif choice == "4":
            pass
            #pull_cards_menu()
            card_name = input("\nEnter the name of the card to activate its effect: ")
            print(f"{card_name} activated its effect.")
        elif choice == "5":
            pass
            card_name, send_card = input("\nEnter the name of the card and either 'gy' or 'banish', separated by a comma: ").split(',')
            deck_building.send_card_gy_banish(card_name, send_card)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

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
            playing_field.start_duel()
            duel_actions_menu()
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