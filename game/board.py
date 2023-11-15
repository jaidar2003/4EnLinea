
class Board:
    def __init__(self, cols=7, rows=6):
        self.rows = rows
        self.cols = cols
        self.board = [[''for _ in range(cols) for _ in range(rows)]]

    def print(self):
        for row  in self.board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' | ')
            print()
            print('-' * (self.cols * 4 - 1))