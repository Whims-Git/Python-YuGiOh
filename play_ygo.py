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
            # deck_building.add_card_to_deck("Blue-Eyes White Dragon", "3")
            deck_building.add_card_to_deck("Pot of Greed", "2")
            deck_building.add_card_to_deck("Two-Pronged Attack", "2")
            deck_building.add_card_to_deck("Forest", "2")
            # deck_building.add_card_to_deck("Charubin the Fire Knight", "1")
        elif choice == "5":
            card_name, card_qty = input("\nEnter the card name and the amount to be removed, separated by a comma: ").split(',')
            deck_building.remove_card_from_deck(card_name, card_qty)
        elif choice == "6":
            print("\nReturning to Main Menu...")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

def duel_actions_menu(field):
    while True:
        print("\nActions Menu")
        print("1. Examine hand/card in hand")
        print("2. Examine field/card on field")
        print("3. Examine graveyard/banishment and a card there")
        print("4. Summon/Set card to Field")
        print("5. Change monster card position on field")
        print("6. Activate card effect")
        print("7. Move cards gy/banishment <-> hand/field")
        print("8. Show main/extra deck")
        print("9. Quit")
        choice = input("\nEnter your choice (1-9): ")

        if choice == "1":
            field.show_hand()
            card_name, hand_zone_index = input("\nEnter the card name and hand position(L -> R, 1-5), separated by a comma: ").split(',')
            hand_zone_index = int(hand_zone_index.strip()) - 1
            field.examine_card(card_name, "hand", hand_zone_index)
        elif choice == "2":
            field.show_field()
            card_name, field_zone_index = input("\nEnter the card name and the zone number(L -> R, 1-5, any for field spell), " \
            "separated by a comma: ").split(',')
            field_zone_index = int(field_zone_index.strip()) - 1
            field.examine_card(card_name.strip(), "field", field_zone_index)
        elif choice == "3":
            field.show_grave_banish()
            card_name, gy_banish, gy_banish_zone_index = input("\nEnter the card name, either 'gy' or 'banish', "
            "and the location number, separated by a comma: ").split(',')
            gy_banish_zone_index = int(gy_banish_zone_index.strip()) - 1
            field.examine_card(card_name.strip(), gy_banish.strip(), gy_banish_zone_index)
        elif choice == "4":
            summon_set_menu(field)
        elif choice == "5":
            field.show_field()
            card_name, field_zone_index, card_position = input("\nEnter the monster card name, the zone number, "
            "and either 'atk' or 'def', separated by a comma: ").split(',')
            field_zone_index = int(field_zone_index.strip()) - 1
            field.change_monster_position(card_name.strip(), field_zone_index, card_position.strip())
            field.show_field()
        elif choice == "6":
            card_name = input("\nEnter the name of the card to activate its effect: ")
            field.activate_card(card_name.strip())
            print(f"\n{card_name} activated its effect.")
        elif choice == "7":
            move_cards_menu(field)
        elif choice == "8":
            field.show_main_extra()
        elif choice == "9":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")

def summon_set_menu(field):
    while True:
        print("\nSummon or set a card menu")
        print("1. Summon or set a monster card")
        print("2. Set a spell or trap card")
        print("3. Set a field spell")
        print("4. Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            field.show_hand()
            card_name, hand_index, face_up_down, field_zone_index = input("\nEnter the monster card name, position in hand, " \
            "either 'summon' or 'set', and field zone # (L -> R, Zone 1-5), separated by a comma: ").split(',')
            hand_index = int(hand_index.strip()) - 1
            field_zone_index = int(field_zone_index.strip()) - 1
            field.place_monster_card(card_name.strip(), hand_index, face_up_down.strip(), field_zone_index)
            field.show_field()
        elif choice == "2":
            field.show_hand()
            card_name, hand_index, field_zone_index = input("\nEnter the spell/trap card name, position in hand, "
            "and field zone # (L -> R, Zone 1-5), separated by a comma: ").split(',')
            hand_index = int(hand_index.strip()) - 1
            field_zone_index = int(field_zone_index.strip()) - 1
            field.place_spell_trap_card(card_name.strip(), hand_index, field_zone_index)
            field.show_field()
        elif choice == "3":
            field.show_hand()
            card_name, hand_index = input("\nEnter the field spell card name and position in hand, separated by a comma: ").split(',')
            hand_index = int(hand_index.strip()) - 1
            field.place_field_spell(card_name.strip(), hand_index)
            field.show_field()
        elif choice == "4":
            print("Returning to Duel menu.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

def move_cards_menu(field):
    while True:
        print("\nMove cards from gy/banishment <-> hand/field")
        print("1. Send a card from field to gy/banishment")
        print("2. Send a card from hand/gy/banishment to hand/gy/banishment")
        print("3. Send a field spell card from field to gy/banishment")
        print("4. Return card from gy/banishment to field")
        print("5. Return card from gy/banishment to the hand")
        print("6. Quit")
        choice = input("\nEnter your choice (1-6): ")

        if choice == "1": # Send a card from field to gy/banishment
            field.show_field()
            card_name, field_index, gy_banish = input("\nEnter the name of the card, the field index, and either 'gy' or 'banish', separated by a comma: ").split(',')
            field_index = int(field_index.strip()) - 1
            field_location = "field"
            field.move_cards_gy_banish(card_name.strip(), field_location.strip(), field_index, gy_banish.strip())
            field.show_grave_banish()
            field.show_field()
        elif choice == "2": # Send a card from hand/gy/banishment to hand/gy/banishment
            field.show_hand()
            field.show_grave_banish()
            card_name, from_location, index, to_location = input("\nEnter the name of the card, the 'from' 'hand', 'gy', or 'banish', the index, "
            "and the 'to' location 'hand', 'gy', or 'banish', separated by a comma: ").split(',')
            index = int(index.strip()) - 1
            field.move_cards_gy_banish(card_name.strip(), from_location.strip(), index, to_location.strip())
            field.show_grave_banish()
            field.show_hand()
        elif choice == "3": # Send a field spell card from field to gy/banishment
            field.show_field()
            field.show_hand()
            card_name, hand_field_location, gy_banish = input("\nEnter the name of the card and either 'gy' or 'banish', separated by a comma: ").split(',')
            hand_field_location = "field"
            hand_field_index = None
            field.move_cards_gy_banish(card_name.strip(), hand_field_location.strip(), hand_field_index, gy_banish.strip())
            field.show_grave_banish()
            field.show_field()
        elif choice == "4":
            field.show_hand()
            card_name, hand_index = input("\nEnter the field spell card name and position in hand, separated by a comma: ").split(',')
            hand_index = int(hand_index.strip()) - 1
            field.place_field_spell(card_name.strip(), hand_index)
            field.show_field()
        elif choice == "5":
            pass
        elif choice == "6":
            print("Returning to Duel menu.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

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

        if choice == "1":
            deck_building.list_all_vanillas()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "2":
            deck_building.list_all_main_effects()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "3":
            deck_building.list_all_fusions()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "4":
            deck_building.list_all_spells()
            card_name, card_qty = input("\n Would you like to add a card to your deck? " \
            "Enter the card name and the amount to add, separated by a comma: ").split(',')
            deck_building.add_card_to_deck(card_name.strip(), card_qty.strip())
        elif choice == "5":
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