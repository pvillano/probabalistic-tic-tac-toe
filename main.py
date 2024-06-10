"""
x goes first
approx 2 * 3**9 == 39_366 possible states
terminal states have gain of 1 or 0

the fitness of a state is ish the sum of the probabilities of the ideal state

"""
from functools import cache
from itertools import chain
from random import Random

from utils.grids import transpose
from utils.std import pprint

x = 'x'
o = 'o'
blank = ' '

board_type = tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str],]
chance_type = tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]


def wrap(player: str, board: tuple[tuple[str]]) -> int:
    pass


def unwrap(wrapped: int) -> (str, board_type):
    pass


def winner(board: board_type) -> str:
    for row in chain(board, transpose(board),
                     ((board[0][0], board[1][1], board[2][2]),
                      (board[0][2], board[1][1], board[2][0]))):
        if set(row) in ({x}, {o}):
            return row[0]
    if blank not in set(chain(*board)):
        return 'tie'
    return blank


@cache
def highest_win_chance(chances,
                       player_in_control: str = x,
                       board: board_type = ((blank, blank, blank),
                                            (blank, blank, blank),
                                            (blank, blank, blank),)):
    """

    :param chances: chance of success
    :param player_in_control: x or o
    :param board:
    :return:
    """
    if (w := winner(board)) != blank:
        return int(w == player_in_control)

    best = 0
    other_player = x if player_in_control == o else o
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val != blank:
                continue
            chance_of_success = chances[r][c]
            new_board_success = tuple(tuple(player_in_control if r == rr and c == cc else board[rr][cc]
                                            for cc in range(3)) for rr in range(3))

            new_board_fail = tuple(tuple(other_player if r == rr and c == cc else board[rr][cc]
                                         for cc in range(3)) for rr in range(3))

            expectation = chance_of_success * (1 - highest_win_chance(chances, other_player, new_board_success))
            + (1 - chance_of_success) * highest_win_chance(chances, other_player, new_board_fail)
            best = max(best, expectation)
    return best


def main():
    rand = Random()
    chances = tuple(tuple(rand.randint(0, 20) / 20 for c in range(3)) for r in range(3))
    pprint(chances)
    print(highest_win_chance(chances))


if __name__ == '__main__':
    main()
