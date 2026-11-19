from classes.card import Card
from classes.player import Player
from classes.game import Game
from menus.main_menu import print_main_menu, print_new_game_menu
from inputs.input_valid import get_number
from flow.game_flow import start_the_game
def main():
    while True:
        print_main_menu()
        chice = get_number("Enter your choice: ")
        if chice == 2:
            return
        if chice == 1:
            while True:
                start_the_game()
                print_new_game_menu()
                chice_new = get_number("Enter your choice: ")
                if chice_new == 2:
                    return
                if chice_new == 1:
                    start_the_game()
                else:
                    print("Enter your choice (1 or 2 only): ")
                
        else:
            print("Enter your choice (1 or 2 only): ")

if __name__ == "__main__":
    main()
    