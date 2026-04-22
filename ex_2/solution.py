class NavalBattle:
    """
    A class representing a naval battle game with a shared playing field.

    Manages a 10x10 game grid where players can take shots at coordinates.
    Tracks hits and misses, displaying the current state of the field.

    Attributes:
        playing_field (list): Class variable representing the 10x10 game grid.
        0 = empty cell, 1 = ship cell.
    """

    playing_field = [[0 for _ in range(10)] for _ in range(10)]

    def __init__(self, symb: str) -> None:
        """
        Initialize a new player in the naval battle.

        Args:
            symb (str): The symbol to mark hits on the playing field.
        """
        self.battle_symb = symb

    def shot(self, x: int, y: int) -> None:
        """
        Make a shot at the specified coordinates.

        Args:
            x (int): X-coordinate (column) from 1 to 10.
            y (int): Y-coordinate (row) from 1 to 10.
        """
        if NavalBattle.playing_field[y - 1][x - 1]:
            print('попал')
            NavalBattle.playing_field[y - 1][x - 1] = self.battle_symb
        else:
            print('мимо')
            NavalBattle.playing_field[y - 1][x - 1] = 'o'

    @staticmethod
    def show() -> None:
        """
        Display the current state of the playing field.

        Shows:
            '~' for unknown cells
            'o' for missed shots
            Player's symbol for successful hits
        """
        for row in NavalBattle.playing_field:
            current_field = ''
            for value in row:
                match value:
                    case 'o':
                        current_field += 'o'
                    case 1 | 0:
                        current_field += '~'
                    case _:
                        current_field += str(value)
            print(current_field)
