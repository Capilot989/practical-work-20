import random


class NavalBattle:
    """
    A class representing a naval battle game with a shared playing field.

    Manages a 10x10 game grid where players can take shots at coordinates.
    Tracks hits and misses, displaying the current state of the field.

    Attributes:
        playing_field (list): Class variable representing the 10x10 game grid.
        0 = empty cell, 1 = ship cell.
    """

    playing_field = None

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
        if NavalBattle.playing_field is None:
            print('игровое поле не заполнено')
            return

        x -= 1
        y -= 1

        match NavalBattle.playing_field[y][x]:
            case 1:
                print('попал')
                NavalBattle.playing_field[y][x] = self.battle_symb
            case 0:
                print('мимо')
                NavalBattle.playing_field[y][x] = 'o'
            case _:
                print('ошибка')

    @classmethod
    def can_place(cls, x: int, y: int, ship: int, position: str) -> bool:
        """
        Check if a ship can be placed at the specified coordinates.

        Verifies that the ship does not overlap with existing ships and
        maintains the required one-cell gap between ships.

        Args:
            x (int): Starting X-coordinate (0-indexed).
            y (int): Starting Y-coordinate (0-indexed).
            ship (int): Size of the ship (1-4 cells).
            position (str): Orientation of the ship ('horizontal' or 'vertical').

        Returns:
            bool: True if the ship can be placed, False otherwise.
        """
        match position:
            case 'horizontal':
                width = 1
                length = ship
            case 'vertical':
                width = ship
                length = 1

        for y_shift in range(max(0, y - 1), min(10, y + width + 1)):
            for x_shift in range(max(0, x - 1), min(10, x + length + 1)):
                if cls.playing_field[y_shift][x_shift] == 1:
                    return False
        return True

    @classmethod
    def new_game(cls):
        """
        Initialize a new naval battle game with randomly placed ships.

        Creates a fresh 10x10 playing field and randomly places ships
        according to standard naval battle rules (1x4, 2x3, 3x2, 4x1 ships).
        Ships are placed with a one-cell gap between them.
        """
        cls.playing_field = [[0 for _ in range(10)] for _ in range(10)]
        ships =[
            1, 1, 1, 1,
            2, 2, 2,
            3, 3,
            4
        ]
        positions = ['horizontal', 'vertical']

        for ship in ships:

            placed = False
            while not placed:
                position = random.choice(positions)
                match position:
                    case 'horizontal':
                        width = 1
                        length = ship
                    case 'vertical':
                        width = ship
                        length = 1

                x = random.randint(0, 9 - length + 1)
                y = random.randint(0, 9 - width + 1)

                if cls.can_place(x, y, ship, position):
                    if position == 'horizontal':
                        for shift in range(ship):
                            cls.playing_field[y][x + shift] = 1

                    if position == 'vertical':
                        for shift in range(ship):
                            cls.playing_field[y + shift][x] = 1

                    placed = True

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

