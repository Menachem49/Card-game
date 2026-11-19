
from classes.player import Player
from classes.game import Game
from inputs.input_valid import get_string, get_number
from menus.game_menu import print_game_menu

def start_the_game():
    name = get_string("Enter your name: ").title()
    player = Player(name)
    game = Game(player)
    game.start_game()

    while True:
        print_game_menu()
        choice = get_number("Enter your choice: ")
        if choice == 2:
            break
        if choice == 1:
            print('• ========== TURN ==========')
            game.play_turn()
            print('• ==========================')
            
        else:
            print("Enter your choice (1 or 2 only)!")
    print(f'• {name} cards: {len(game.player.cards)} | Computer cards: {len(game.computer.cards)}')
    winner = game.player.name if len(game.player.cards) > len(game.computer.cards) else "Computer" if len(game.player.cards) < len(game.computer.cards) else "It's a draw!"
    print(f'{winner} is the winner 🥳🥳🥳')
