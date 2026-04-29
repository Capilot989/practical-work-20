from typing import Union, Optional


class RomanNumber:
    """
    A class representing Roman numerals and providing bidirectional conversion.

    This class handles validation of Roman numeral strings and conversion between
    Roman numerals and decimal integers (1-3999) according to standard rules.
    Supports arithmetic operations between RomanNumber objects.

    Class Attributes:
        roman (dict): Mapping of Roman numeral characters to their integer values.
        int_to_roman (list): Ordered tuples for converting integers to Roman numerals.
    """

    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    int_to_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def __init__(self, value: Union[str, int]) -> None:
        """
        Initialize a RomanNumber instance from either a Roman numeral string or an integer.

        Args:
            value (Union[str, int]): Either a Roman numeral string or an integer (1-3999).
                                    Invalid values print 'ошибка' and set attributes to None.
        """
        if isinstance(value, str):
            if RomanNumber.is_roman(value):
                self.rom_value = value
                self.int_value = self.decimal_number()
            else:
                self.rom_value = None
                self.int_value = None
                print('ошибка')

        elif isinstance(value, int):
            if RomanNumber.is_int(value):
                self.int_value = value
                self.rom_value = self.roman_number()
            else:
                self.rom_value = None
                self.int_value = None
                print('ошибка')

    def decimal_number(self) -> Optional[int]:
        """
        Convert the stored Roman numeral to its decimal integer value.

        Handles standard Roman numeral subtraction rules (IV = 4, IX = 9, etc.)
        and additive notation for repeated characters.

        Returns:
            Optional[int]: The decimal integer value of the Roman numeral,
                             or None if the stored value is invalid.
        """
        value = self.rom_value
        if value is None:
            return None

        valid_substraction = [
            'IV', 'IX',
            'XL', 'XC',
            'CD', 'CM'
        ]
        current_index = 0
        int_numb = 0
        while current_index < len(value):
            char_int_value = RomanNumber.roman[value[current_index]]
            if current_index + 1 < len(value):
                next_char_int_value = RomanNumber.roman[value[current_index + 1]]

                if char_int_value == next_char_int_value:
                    int_numb += 2 * char_int_value
                    current_index += 2
                    continue

                if value[current_index:current_index + 2] in valid_substraction:
                    int_numb += next_char_int_value - char_int_value
                    current_index += 2
                    continue

            int_numb += char_int_value
            current_index += 1
        return int_numb

    def roman_number(self) -> Optional[str]:
        """
        Convert the stored integer to its Roman numeral representation.

        Uses a greedy algorithm with ordered value-symbol pairs.

        Returns:
            Union[str, None]: The Roman numeral string representation,
                             or None if the stored integer is invalid.
        """
        value = self.int_value
        if value is None:
            return None

        rom_numb = ''
        for int_value, rom_value in RomanNumber.int_to_roman:
            while value >= int_value:
                rom_numb += rom_value
                value -= int_value
        return rom_numb

    @staticmethod
    def is_roman(value: str) -> bool:
        """
        Validate whether a string is a properly formatted Roman numeral.

        Checks for:
        - Invalid repeated characters (e.g., IIII, XXXX, VV)
        - Presence of non-Roman characters

        Args:
            value (str): The string to validate as a Roman numeral.

        Returns:
            bool: True if the string is a valid Roman numeral, False otherwise.
        """
        invalid_chars = [
            'IIII', 'XXXX', 'CCCC', 'MMMM',
            'VV', 'LL', 'DD'
        ]
        if any(char in value for char in invalid_chars):
            return False
        for char in value:
            if char not in RomanNumber.roman:
                return False

        return True

    @staticmethod
    def is_int(value: int) -> bool:
        """
        Validate whether an integer can be represented as a Roman numeral.

        Standard Roman numerals can only represent numbers from 1 to 3999.

        Args:
            value (int): The integer to validate.

        Returns:
            bool: True if the integer is between 1 and 3999 inclusive, False otherwise.
        """
        if str(value).isdigit() and 1 <= value <= 3999:
            return True
        return False

    def __add__(self, other) -> 'RomanNumber':
        """
        Add two RomanNumber objects.

        Args:
            other (RomanNumber): The RomanNumber to add.

        Returns:
            RomanNumber: A new RomanNumber representing the sum,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() + other.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __sub__(self, other) -> 'RomanNumber':
        """
        Subtract one RomanNumber from another.

        Args:
            other (RomanNumber): The RomanNumber to subtract.

        Returns:
            RomanNumber: A new RomanNumber representing the difference,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() - other.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __mul__(self, other) -> 'RomanNumber':
        """
        Multiply two RomanNumber objects.

        Args:
            other (RomanNumber): The RomanNumber to multiply by.

        Returns:
            RomanNumber: A new RomanNumber representing the product,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() * other.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __truediv__(self, other) -> 'RomanNumber':
        """
        Divide one RomanNumber by another (true division).

        Args:
            other (RomanNumber): The divisor.

        Returns:
            RomanNumber: A new RomanNumber representing the quotient,
                        or an invalid RomanNumber if the result is not an integer
                        or is out of range.
        """
        result = self.decimal_number() / other.decimal_number()
        if result % 1 == 0 and 1 <= result <= 3999:
            return RomanNumber(int(result))
        else:
            return RomanNumber('invalid')

    def __floordiv__(self, other) -> 'RomanNumber':
        """
        Divide one RomanNumber by another (floor division).

        Args:
            other (RomanNumber): The divisor.

        Returns:
            RomanNumber: A new RomanNumber representing the floor quotient,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() // other.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __mod__(self, other) -> 'RomanNumber':
        """
        Compute the remainder of division between two RomanNumber objects.

        Args:
            other (RomanNumber): The divisor.

        Returns:
            RomanNumber: A new RomanNumber representing the remainder,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() % other.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __pow__(self, power, modulo=None) -> 'RomanNumber':
        """
        Raise a RomanNumber to a power.

        Args:
            power (RomanNumber): The exponent (must be a positive integer).
            modulo (Optional[int]): Not used, included for compatibility.

        Returns:
            RomanNumber: A new RomanNumber representing the result,
                        or an invalid RomanNumber if the result is out of range.
        """
        result = self.decimal_number() ** power.decimal_number()
        if RomanNumber.is_int(result):
            return RomanNumber(result)
        else:
            return RomanNumber('invalid')

    def __repr__(self) -> str:
        """
        Return a string representation of the Roman numeral.

        Returns:
            str: The stored Roman numeral string, or 'None' if rom_value is None.
        """
        return f'{self.rom_value}'
