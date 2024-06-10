from main import highest_win_chance


def test_x_win():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    assert highest_win_chance(chances, 'x', (('x', 'x', 'x'), (' ', ' ', ' '), (' ', ' ', ' '))) == 1


def test_x_lose():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    assert highest_win_chance(chances, 'x', (('o', 'o', 'o'), (' ', ' ', ' '), (' ', ' ', ' '))) == 0


def test_50_50():
    chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
    board = (('o', 'x', 'o'), ('x', ' ', 'x'), ('o', 'x', 'o'))
    assert highest_win_chance(chances, 'x', board) == .5


def test_deep_50_50():
    chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
    board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
    assert highest_win_chance(chances, 'x', board) == .5
