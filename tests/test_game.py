import unittest

from tictactoe.game import *


class GameTest(unittest.TestCase):

    def test_check_column_win(self):
        board = Board()
        board.rows = [['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]
        self.assertTrue(check_win(board))

    def test_check_row_win(self):
        board = Board()
        board.rows = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(check_win(board))

    def test_check_first_diagonal_win(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]
        self.assertTrue(check_win(board))

    def test_check_second_diagonal_win(self):
        board = Board()
        board.rows = [[' ', ' ', 'X'], [' ', 'X', ' '], ['X', ' ', ' ']]
        self.assertTrue(check_win(board))


if __name__ == '__main__':
    unittest.main()
