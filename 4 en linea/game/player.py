from board import *

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def main():
        player1 = Player('X')
        player2 = Player('O')
        
        game_board = Board()

        players = [player1, player2]
        current_player = 0

        while True:
            game_board.print_board()
            
            try:
                col = int(input(f'Jugador {players[current_player]}, elige una columna (0-{game_board.cols - 1}): '))
                if game_board.is_valid_move(col):
                    game_board.drop_piece(players[current_player], col)
                    if game_board.check_winner():
                        game_board.print_board()
                        print(f'¡Jugador {players[current_player]} gana!')
                        break
                    elif game_board.is_full():
                        game_board.print_board()
                        print('¡Empate!')
                        break
                    else:
                        current_player = 1 - current_player  
                else:
                    print('Columna no válida. Inténtalo de nuevo.')
            except ValueError:
                print('Por favor, ingresa un número válido.')