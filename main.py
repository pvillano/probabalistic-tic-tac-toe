from functools import cache
from itertools import chain
from random import Random

from utils.grids import transpose
from utils.std import pprint

x = 'x'
o = 'o'
blank = ' '

board_type = tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str],]
chance_type = tuple[
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]],
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]],
    tuple[tuple[float, float, float], tuple[float, float, float], tuple[float, float, float]]]


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
def expected_points(chances,
                    player_in_control: str = x,
                    board: board_type = ((blank, blank, blank),
                                         (blank, blank, blank),
                                         (blank, blank, blank),)) -> float:
    """

    :param chances: chance of success
    :param player_in_control: x or o
    :param board:
    :return: chance of winning, chance of a tie
    """
    w = winner(board)
    match w:
        case 'x':
            return 1 if player_in_control == x else -1
        case 'o':
            return 1 if player_in_control == o else -1
        case 'tie':
            return 0

    best = -1
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

            expectation = (chance_of_success * - expected_points(chances, other_player, new_board_success)
                           + (1 - chance_of_success) * (-expected_points(chances, other_player, new_board_fail)))
            best = max(best, expectation)
    return best


def random_thirds(r: Random, n=20):
    bar1 = r.randint(0, n)
    bar2 = r.randint(0, n)
    if bar1 > bar2: bar1, bar2 = bar2, bar1
    arr = [bar1 / n, (bar2 - bar1) / n, (n - bar2) / n]
    r.shuffle(arr)  # todo: prove this isn't necessary
    return tuple(arr)


def main():
    rand = Random()
    chances = tuple(tuple(random_thirds(rand) for _ in range(3)) for _ in range(3))
    pprint(chances)
    print(expected_points(chances))


if __name__ == '__main__':
    main()
