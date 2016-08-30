import itertools


class Board(object):

    def __init__(self):
        self.rows = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.empty_coordinates = set(itertools.product(range(3), repeat=2))

    @property
    def diagonals(self):
        return [[self.rows[0][0], self.rows[1][1], self.rows[2][2]],
                [self.rows[0][2], self.rows[1][1], self.rows[2][0]]]

    @property
    def columns(self):
        return map(list, zip(*self.rows))

    def update_empty_coordinates(self, coordinate_pair):
        '''Removes coordinate_pair from empty coordinate_pair'''
        self.empty_coordinates.remove(coordinate_pair)

    def __str__(self):
        return "  a b c\n0 {}\n1 {}\n2 {}".format(' '.join(self.rows[0]),
                                                  ' '.join(self.rows[1]),
                                                  ' '.join(self.rows[2]))

    def update(self, player_name, coordinate_pair):
        self.rows[coordinate_pair[0]][coordinate_pair[1]] = player_name
        self.update_empty_coordinates(coordinate_pair)

    @property
    def id(self):
        return ''.join(itertools.chain.from_iterable(self.rows))
