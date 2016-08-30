import random

from training import train


class Player(object):

    def __init__(self, name):
        self.name = name


class HumanPlayer(Player):

    def __init__(self, name):
        super(HumanPlayer, self).__init__(name)

    def get_move(self, board):
        print ('Player-{} please enter the coordinate_pair for your move'
               .format(self.name))

        while True:
            try:
                input_coordinate_pair = raw_input()
                coordinate_pair = parse_coordinate_pair(input_coordinate_pair,
                                                        board)
            except (ValueError, IndexError, KeyError):
                print 'The coordinates you entered are not valid. Re-enter.'
                continue
            break

        return coordinate_pair


class RandomPlayer(Player):

    def __init__(self, name):
        super(RandomPlayer, self).__init__(name)

    def get_move(self, board):
        '''Takes a board. And returns a valid and currently empty coordinate
        pair'''
        return random.choice(list(board.empty_coordinates))


class AiPlayer(Player):

    def __init__(self, name, training=None):
        super(AiPlayer, self).__init__(name)
        if not training:
            training = train(100000)

        if name == 'X':
            self.training = iter(training[::2])

        if name == 'O':
            self.training = iter(training[1::2])

    def get_move(self, board):
        '''Depending on the board position get the move which obtained the
        highest score in the training'''
        turn_dict = self.training.next()
        moves_dict = turn_dict[board.id]
        return max(moves_dict, key=lambda k: moves_dict[k])


def parse_coordinate_pair(input_coordinate_pair, board):
    letters_to_numbers = {'a': 0, 'b': 1, 'c': 2}

    try:
        coordinate_pair = (int(input_coordinate_pair[0]),
                           letters_to_numbers[input_coordinate_pair[1]])
    except (ValueError, KeyError):
        coordinate_pair = (int(input_coordinate_pair[1]),
                           letters_to_numbers[input_coordinate_pair[0]])

    if (coordinate_pair[0] > (len(board.rows) - 1)):
        raise ValueError('Out of bound coordinate_pair')

    if board.rows[coordinate_pair[0]][coordinate_pair[1]] != ' ':
        raise ValueError('Duplicate coordinate_pair')

    return coordinate_pair
