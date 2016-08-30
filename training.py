import sys
import itertools

from game import Game
import player


def train(n, score_win=10, score_lose=-10, score_draw=8):
    '''This lets two random players play against each other n times.
       For every turn it assigns the appropriate score depending on which board
       position resulted in a win/loss/draw.'''

    training = [{} for x in range(9)]
    for x in range(n):
        game = Game(player.RandomPlayer('X'), player.RandomPlayer('O'))
        game.play(public=False, train=True)

        players_cycle = itertools.cycle(game.players)
        for turn, (board_id, coordinates) in enumerate(zip(game.board_ids,
                                                           game.coordinates)):
            current_player = players_cycle.next()
            if not game.winner:
                score = score_draw
            elif game.winner == current_player:
                score = score_win
            else:
                score = score_lose

            try:
                training[turn][board_id]
            except KeyError:
                training[turn][board_id] = {}

            try:
                training[turn][board_id][coordinates]
            except KeyError:
                training[turn][board_id][coordinates] = [0, 0]

            training[turn][board_id][coordinates][0] += score
            training[turn][board_id][coordinates][1] += 1

    for turn in training:
        for board, moves in turn.iteritems():
            for move, (score, total) in moves.iteritems():
                moves[move] = score / float(total)

    return training

if __name__ == '__main__':
    n = int(sys.argv[1])
    print train(n)
