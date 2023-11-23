from game.board import *

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = ''

    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

    def __str__(self):
        return self.symbol

