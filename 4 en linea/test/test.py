from game.board import Board
from game.player import Player
import unittest

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initialization(self):
        self.assertEqual(self.board.rows, 6)
        self.assertEqual(self.board.cols, 7)
        self.assertEqual(len(self.board.board), 6)
        self.assertEqual(len(self.board.board[0]), 7)

    def test_is_valid_move(self):
        self.assertTrue(self.board.is_valid_move(0))
        self.assertTrue(self.board.is_valid_move(3))
        self.assertFalse(self.board.is_valid_move(-1))
        self.assertFalse(self.board.is_valid_move(7))

    def test_drop_piece(self):
        player = Player('X')
        self.board.drop_piece(player, 2)
        self.assertEqual(self.board.board[5][2], 'X')