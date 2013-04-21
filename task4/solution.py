class TicTacToeBoard:
    BOARD_FORMAT = '\n  -------------\n' +\
                   '3 | {A3} | {B3} | {C3} |\n' +\
                   '  -------------\n' +\
                   '2 | {A2} | {B2} | {C2} |\n' +\
                   '  -------------\n' +\
                   '1 | {A1} | {B1} | {C1} |\n' +\
                   '  -------------\n' +\
                   '    A   B   C  \n'

    __WIN_LINES = (
        ((1, 1), (1, 0)),
        ((1, 1), (0, 1)),
        ((1, 1), (1, 1)),
        ((3, 1), (-1, 1)),
        ((3, 1), (0, 1)),
        ((3, 3), (-1, 0)),
        ((2, 1), (0, 1)),
        ((3, 2), (-1, 0)),
    )

    def __init__(self):
        self.__game_board = {(row, column): ' '
                             for row in [1, 2, 3]
                             for column in [1, 2, 3]}
        self._next_turn = None
        self._winner = None

    def __check_line(self, start_index, delta):
        """Check if the line is complete
        and return the player to whom it belongs, else return None.
        """

        position = start_index
        player = None

        while 1 <= position[0] <= 3 and 1 <= position[1] <= 3:
            if player is not None and self.__game_board[position] != player:
                return None

            player = self.__game_board[position]
            position = position[0] + delta[0], position[1] + delta[1]

        return player if player is not ' ' else None

    def __check_win(self):
        """Check if any player won the game and return X, O or None."""
        for win_line in self.__WIN_LINES:
            check_result = self.__check_line(*win_line)
            if check_result is not None:
                return check_result

        return None

    def __all_filled(self):
        """Check if all the fields have been filled."""
        return all(field != ' ' for field in self.__game_board.values())

    def game_status(self):
        if self._winner is not None:
            return "{} wins!".format(self._winner)

        if self.__all_filled():
            return "Draw!"

        return "Game in progress."

    @staticmethod
    def _parse_index(index):
        """Return tuple of positions (row, column) in numbers from 1 to 3."""

        if len(index) != 2:
            raise InvalidKey("The length of the key must be 2 symbols")

        column = ord(index[0]) - ord('A') + 1
        row = int(index[1])

        if not 1 <= column <= 3 or not 1 <= row <= 3:
            raise InvalidKey("The first symbol should be A, B or C, and the "
                             "second one should be 1, 2 or 3.")

        return (row, column)

    def __getitem__(self, index):
        """Return board data at `index`.

        `index` should be one letter A, B or C, followed by 1, 2 or 3.
        Raises InvalidKey if the format isn't valid.
        """
        index_tuple = TicTacToeBoard._parse_index(index)

        return self.__game_board[index_tuple]

    def __setitem__(self, index, value):
        if value not in ('X', 'O'):
            raise InvalidValue("The only allowed values are X and O")

        if self._next_turn is not None and self._next_turn != value:
            raise NotYourTurn("The {} player should play this turn"
                              .format(self._next_turn))

        index_tuple = TicTacToeBoard._parse_index(index)

        if self.__game_board[index_tuple] != ' ':
            raise InvalidMove("The field {} is already set.".format(index))

        self.__game_board[index_tuple] = value
        self._next_turn = 'X' if value == 'O' else 'O'
        self._winner = self.__check_win()

    def __str__(self):
        board_data = {chr(column + ord('A') - 1) + str(row): value
                      for (row, column), value in self.__game_board.items()}
        return self.BOARD_FORMAT.format(**board_data)


class InvalidKey(Exception):
    pass


class InvalidMove(Exception):
    pass


class InvalidValue(Exception):
    pass


class NotYourTurn(Exception):
    pass
