import random
from classes.card import Card
from classes.player import Player

class Game:
    def __init__(self, human_player:Player):
        self.player = human_player
        self.computer = Player("Computer")
        self.cards = self.crate_cards()
        

    def start_game(self):
        self.mix_card()
        self.dealing_cards()

    def crate_cards(self):
        cards = []
        for type_ in ["H","D","S","C"]:
            for number in range(2,15):
                cards.append(Card(type_, number))
        return cards
    
    def mix_card(self):
        for _ in range(1000):
            first_index = random.randint(0,51)
            second_index = random.randint(0,51)
            self.cards[first_index] , self.cards[second_index] = self.cards[second_index], self.cards[first_index]

    def dealing_cards(self):
        for i in range(52):
            if i % 2 == 0:
                self.player.cards.append(self.cards[i])
            else:
                self.computer.cards.append(self.cards[i])
    

    def play_turn(self):
        card_nuumbers = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,'J':11,'Q':12,'K':13,'A':14}
        
        player_card = self.player.cards.pop(0)
        computer_card = self.computer.cards.pop(0)
        
        print(f'• {self.player.name}: {player_card}')
        print(f'• Computer: {computer_card}')
        if card_nuumbers[player_card.card_number] > card_nuumbers[computer_card.card_number]:
            self.player.cards.append(player_card)
            self.player.cards.append(computer_card)
            print(f'• {self.player.name} won the round!')
        elif card_nuumbers[player_card.card_number] < card_nuumbers[computer_card.card_number]:
            self.computer.cards.append(player_card)
            self.computer.cards.append(computer_card)
            print('• Computer won the round!')
        else:
            self.player.cards.append(player_card)
            self.computer.cards.append(computer_card)
            print("• It's a draw!")
        print(f'• {self.player.name} cards: {len(self.player.cards)} | Computer cards: {len(self.computer.cards)}')
       




#     def __str__(self):
#         return f'''
# player: {self.player},
# Computer: {self.computer},
# Cards: {self.cards}
# '''