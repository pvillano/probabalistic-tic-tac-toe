from collections import namedtuple
from collections.abc import Generator
from functools import cache
from itertools import chain
from random import Random

from utils.grids import transpose
from utils.std import pprint

x = 'x'
o = 'o'
blank = ' '

ChanceTriple = namedtuple("ChanceTriple", "pos neg meh")

Board = tuple[tuple[str, str, str], tuple[str, str, str], tuple[str, str, str],]
ChanceType = tuple[
    tuple[ChanceTriple, ChanceTriple, ChanceTriple],
    tuple[ChanceTriple, ChanceTriple, ChanceTriple],
    tuple[ChanceTriple, ChanceTriple, ChanceTriple]]


def winner(board: Board) -> str:
    for row in chain(board, transpose(board),
                     ((board[0][0], board[1][1], board[2][2]),
                      (board[0][2], board[1][1], board[2][0]))):
        if set(row) in ({x}, {o}):
            return row[0]
    if blank not in set(chain(*board)):
        return 'tie'
    return blank


def find_open_cells(board: Board) -> Generator[tuple[int, int]]:
    for r in range(3):
        for c in range(3):
            if board[r][c] == blank:
                yield r, c


def replace(board: Board, rc: tuple[int, int], player: str) -> Board:
    r, c = rc
    if board[r][c] != blank:
        raise ValueError("Tried to replace taken cell")
    return tuple(tuple(player if r == rr and c == cc else board[rr][cc]
                       for cc in range(3)) for rr in range(3))

@cache
def best_score_and_move(odds: ChanceType, me: str = x, board: Board = None) -> tuple[float, tuple[int, int] | None]:
    """

    :param odds: chance of success
    :param me: x or o
    :param board:
    :return: chance of winning, chance of a tie
    """
    if board is None:
        board = ((blank, blank, blank),
                 (blank, blank, blank),
                 (blank, blank, blank))
    w = winner(board)
    match w:
        case 'x':
            return (1, None) if me == x else (-1, None)
        case 'o':
            return (1, None) if me == o else (-1, None)
        case 'tie':
            return 0, None

    them = x if me == o else o
    open_cells = list(find_open_cells(board))

    best_strategy = open_cells[0]
    best_move_me_score = -1  # I want positive points

    for move_me in open_cells:
        odds_me: ChanceTriple = odds[move_me[0]][move_me[1]]
        their_best_move_score = 1  # they want me to get negative points
        for move_them in open_cells:
            odds_them: ChanceTriple = odds[move_them[0]][move_them[1]]
            score = (
                            odds_me.pos * -best_score_and_move(odds, them, replace(board, move_me, me))[0]
                            + odds_me.neg * -best_score_and_move(odds, them, replace(board, move_me, them))[0]
                            + odds_me.meh * (
                                    odds_them.pos * best_score_and_move(odds, me, replace(board, move_them, them))[0]
                                    + odds_them.neg * best_score_and_move(odds, me, replace(board, move_them, me))[0]
                            )
                    ) / (1 - odds_me.meh * odds_them.meh)
            their_best_move_score = min(their_best_move_score, score)
        if their_best_move_score > best_move_me_score:
            best_move_me_score = their_best_move_score
            best_strategy = move_me
    return best_move_me_score, best_strategy


def random_thirds(r: Random, n=20):
    bar1 = r.randint(0, n)
    bar2 = r.randint(0, n)
    if bar1 > bar2:
        bar1, bar2 = bar2, bar1
    arr = [bar1 / n, (bar2 - bar1) / n, (n - bar2) / n]
    r.shuffle(arr)  # todo: prove this isn't necessary
    return ChanceTriple(*arr)


def main():
    rand = Random()
    chances = tuple(tuple(random_thirds(rand) for _ in range(3)) for _ in range(3))
    pprint(chances)
    print(best_score_and_move(chances))
    pass


if __name__ == '__main__':
    main()
