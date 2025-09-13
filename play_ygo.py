import deck_building

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
            card_name, card_qty = input("\nEnter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name, card_qty)
        elif choice == "5":
            card_name, card_qty = input("\nEnter the card name and the amount to be removed, separated by a comma: ").split(',')
            deck_building.remove_card_from_deck(card_name, card_qty)
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

def main_menu():
    while True:
        print("\nYu-Gi-Oh! Main Menu")
        print("1. Duel (Not implemented)")
        print("2. Deck Build")
        print("3. Pull Cards (Not implemented)")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            #duel_menu()
            print("Duel mode is not implemented yet.")
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