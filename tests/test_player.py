import unittest

from tictactoe.player import *
from tictactoe.board import Board


class PlayerTest(unittest.TestCase):

    def test_parse_coordina_pair(self):
        board = Board()
        input_coordinates_1 = '1b'
        input_coordinates_2 = 'b1'
        expected_parsed_coordinates = (1, 1)
        self.assertEqual(expected_parsed_coordinates,
                         parse_coordinate_pair(input_coordinates_1, board))
        self.assertEqual(expected_parsed_coordinates,
                         parse_coordinate_pair(input_coordinates_2, board))

    def test_parse_duplicate_coordinates(self):
        board = Board()
        board.rows = [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertRaises(ValueError, parse_coordinate_pair, '0a', board)

    def test_parse_outofbound_coordinates(self):
        board = Board()
        self.assertRaises(ValueError, parse_coordinate_pair, '0d', board)

    def test_get_random_coordinates(self):
        player = RandomPlayer('X')
        board = Board()
        board.empty_coordinates = set([(1,1)])
        coordinates = player.get_move(board)
        expected_coordinates = (1,1)
        self.assertEqual(expected_coordinates, coordinates)

    def test_get_ai_coordinates(self):
        board = Board()
        training = [{'         ':{(2,2):4.2, (1,0):0.1, (1.1):-1}}]
        player = AiPlayer('X', training=training)
        self.assertEqual((2,2), player.get_move(board))


if __name__ == '__main__':
    unittest.main()
