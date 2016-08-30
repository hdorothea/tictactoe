import itertools
import random

from board import Board


def check_win(board):
    lines = board.rows + board.columns + board.diagonals

    for line in lines:
        if (all(board_position == 'X' for board_position in line) or
           all(board_position == 'O' for board_position in line)):
            return True


class Game(object):

    def __init__(self, player_x, player_o):
        self.board = Board()
        self.players = (player_x, player_o)
        self.winner = None

    def play(self, public=True, train=False):
        if train:
            self.coordinates = []
            self.board_ids = []

        players_cycle = itertools.cycle(self.players)

        for x in range(9):
            current_player = players_cycle.next()

            if public:
                print self.board

            coordinate_pair = current_player.get_move(self.board)

            if train:
                self.board_ids.append(self.board.id)
                self.coordinates.append(coordinate_pair)

            self.board.update(current_player.name, coordinate_pair)

            if check_win(self.board):
                self.winner = current_player
                return current_player

        return None
