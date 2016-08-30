import unittest

from tictactoe.player import *
from tictactoe.run import *


class RunTest(unittest.TestCase):

    def test_get_player_of_mode(self):
        player = get_player_of_mode('x', 'human')
        self.assertIsInstance(player, HumanPlayer)


    def test_parse_input_mode_correct_input(self):
        input_1 = parse_input_mode('Human  ')
        input_2 = parse_input_mode('human')
        self.assertEqual('human', input_1)
        self.assertEqual('human', input_2)

    def test_parse_input_mode_wrong_input(self):
        self.assertRaises(ValueError, parse_input_mode, '  loal')

if __name__ == '__main__':
    unittest.main()
