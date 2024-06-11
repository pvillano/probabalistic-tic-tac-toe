from main import best_score_and_move, ChanceTriple

def test_x_win():
    chances = ((ChanceTriple(1, 0, 0),) * 3,) * 3
    board = (('x', 'x', 'x'), (' ', ' ', ' '), (' ', ' ', ' '))
    assert best_score_and_move(chances, 'x', board)[0] == 1


def test_x_lose():
    chances = ((ChanceTriple(1, 0, 0),) * 3,) * 3
    board = (('o', 'o', 'o'), (' ', ' ', ' '), (' ', ' ', ' '))
    assert best_score_and_move(chances, 'x', board)[0] == -1


def test_50_50():
    chances = ((ChanceTriple(.5, .5, 0),) * 3,) * 3
    board = (('o', 'x', 'o'), ('x', ' ', 'x'), ('o', 'x', 'o'))
    assert best_score_and_move(chances, 'x', board)[0] == 0


def test_deep_50_50():
    chances = ((ChanceTriple(.5, .5, 0),) * 3,) * 3
    board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
    assert best_score_and_move(chances, 'x', board)[0] > 0


def test_regular_no_win():
    chances = ((ChanceTriple(1, 0, 0),) * 3,) * 3
    board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
    assert best_score_and_move(chances, 'x', board)[0] == 0
