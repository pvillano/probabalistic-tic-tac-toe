from main import winner, x, o


def test_undetermined():
    board = (('x', ' ', ' '), (' ', 'o', ' '), (' ', ' ', ' '))
    assert winner(board) == ' '


def test_tie():
    board = ((x, o, x),
             (x, o, o),
             (o, x, x))
    assert winner(board) == 'tie'


def test_filled():
    board = ((x, o, x),
             (o, x, o),
             (x, x, o))
    assert winner(board) == x


def test_sparse():
    board = (('x', ' ', ' '), (' ', 'x', ' '), (' ', ' ', 'x'))
    assert winner(board) == 'x'
