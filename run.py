'''Script and Functions to run the commandline version of the tictactoe'''
from player import *
from game import *


def get_player_of_mode(player_name, player_mode):
        if player_mode == 'human':
            return HumanPlayer(player_name)
        if player_mode == 'random':
            return RandomPlayer(player_name)
        if player_mode == 'ai':
            return AiPlayer(player_name)


def get_mode(player_name):
    while True:
        print ('Choose a mode for Player-{}: human, random or ai'
               .format(player_name))
        try:
            mode = parse_input_mode(raw_input())
            return mode
        except ValueError:
            print 'The mode you entered is not valid. Re-enter.'
            continue


def parse_input_mode(input_mode):
    mode = input_mode.lower().strip()
    if mode in ['human', 'random', 'ai']:
        return mode
    else:
        raise ValueError('Invalid mode')

def print_winner(winner):
    if winner:
        print 'Player-{} won!'.format(winner.name)
    else:
        print 'The Game ended in a draw'


if __name__ == '__main__':
    player_x = get_player_of_mode('X', get_mode('X'))
    player_o = get_player_of_mode('O', get_mode('O'))
    game = Game(player_x, player_o)
    game.play()
    print_winner(game.winner)
