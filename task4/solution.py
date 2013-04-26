class TicTacToeBoard:
    BOARD_FORMAT = '\n  -------------\n' +\
                   '3 | {A3} | {B3} | {C3} |\n' +\
                   '  -------------\n' +\
                   '2 | {A2} | {B2} | {C2} |\n' +\
                   '  -------------\n' +\
                   '1 | {A1} | {B1} | {C1} |\n' +\
                   '  -------------\n' +\
                   '    A   B   C  \n'

    _WIN_LINES = (
        ('A1', 'B2', 'C3'),
        ('A1', 'B1', 'C1'),
        ('A1', 'A2', 'A3'),
        ('B1', 'B2', 'B3'),
        ('C1', 'C2', 'C3'),
        ('A2', 'B2', 'C2'),
        ('A3', 'B3', 'C3'),
        ('C1', 'B2', 'A3')
    )

    def __init__(self):
        self._game_board = {column + row: ' '
                            for row in ('1', '2', '3')
                            for column in ('A', 'B', 'C')}
        self._next_turn = None
        self._winner = None

    def __check_win(self):
        """Check if any player won the game and return X, O or None."""
        for win_line in self._WIN_LINES:
            line_values = set(self._game_board[key] for key in win_line)

            if len(line_values) == 1:
                value = line_values.pop()

                if value != ' ':
                    return value

        return None

    def __all_filled(self):
        """Check if all the fields have been filled."""
        return all(field != ' ' for field in self._game_board.values())

    def game_status(self):
        if self._winner is not None:
            return "{} wins!".format(self._winner)

        if self.__all_filled():
            return "Draw!"

        return "Game in progress."

    @staticmethod
    def _check_index(index):
        """Return tuple of positions (row, column) in numbers from 1 to 3."""

        if len(index) != 2:
            raise InvalidKey("The length of the key must be 2 symbols")

        if index[0] not in ('A', 'B', 'C') or index[1] not in ('1', '2', '3'):
            raise InvalidKey("The first symbol should be A, B or C, and the "
                             "second one should be 1, 2 or 3.")

    def __getitem__(self, index):
        """Return board data at `index`.

        `index` should be one letter A, B or C, followed by 1, 2 or 3.
        Raises InvalidKey if the format isn't valid.
        """
        TicTacToeBoard._check_index(index)

        return self._game_board[index]

    def __setitem__(self, index, value):
        if value not in ('X', 'O'):
            raise InvalidValue("The only allowed values are X and O")

        if self._next_turn is not None and self._next_turn != value:
            raise NotYourTurn("The {} player should play this turn"
                              .format(self._next_turn))

        TicTacToeBoard._check_index(index)

        if self._game_board[index] != ' ':
            raise InvalidMove("The field {} is already set.".format(index))

        self._game_board[index] = value
        self._next_turn = 'X' if value == 'O' else 'O'
        self._winner = self.__check_win()

    def __str__(self):
        return self.BOARD_FORMAT.format(**self._game_board)


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass
