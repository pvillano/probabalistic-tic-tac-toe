from main import best_outcome


def test_x_win():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    assert best_outcome(chances, 'x', (('x', 'x', 'x'), (' ', ' ', ' '), (' ', ' ', ' '))) == 1


def test_x_lose():
    chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
    assert best_outcome(chances, 'x', (('o', 'o', 'o'), (' ', ' ', ' '), (' ', ' ', ' '))) == 0


def test_50_50():
    chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
    board = (('o', 'x', 'o'), ('x', ' ', 'x'), ('o', 'x', 'o'))
    assert best_outcome(chances, 'x', board) == .5


# def test_deep_50_50():
#     chances = ((.5, .5, .5), (.5, .5, .5), (.5, .5, .5))
#     board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
#     assert highest_win_chance(chances, 'x', board) == .5

# def test_regular_no_win():
#     chances = ((1, 1, 1), (1, 1, 1), (1, 1, 1))
#     board = ((' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '),)
#     assert best_outcome(chances, 'x', board) == 0
