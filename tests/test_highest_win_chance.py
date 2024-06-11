from main import expected_points


def test_x_win():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    board = (('x', 'x', 'x'), (' ', ' ', ' '), (' ', ' ', ' '))
    assert expected_points(chances, 'x', board) == 1


def test_x_lose():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    board = (('o', 'o', 'o'), (' ', ' ', ' '), (' ', ' ', ' '))
    assert expected_points(chances, 'x', board) == -1


def test_50_50():
    chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
    board = (('o', 'x', 'o'), ('x', ' ', 'x'), ('o', 'x', 'o'))
    assert expected_points(chances, 'x', board) == 0


def test_deep_50_50():
    chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
    board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
    assert expected_points(chances, 'x', board) > 0


def test_regular_no_win():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
    assert expected_points(chances, 'x', board) == 0
