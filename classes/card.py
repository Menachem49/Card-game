class Card:
    card_types = {"H": "♥️", "D":"♦️", "S": "♠️", "C": "♣️"}
    card_nuumbers = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:"J",12:"Q",13:"K",14:"A"}
    def __init__(self, card_type, card_number):
        self.card_type = self.card_types[card_type]
        self.card_number = self.card_nuumbers[card_number]

    def __str__(self):
        return f'{self.card_number} {self.card_type}'