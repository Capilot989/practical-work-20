class RomanNumber:
    """
    A class representing Roman numerals and providing conversion to decimal numbers.

    This class handles validation of Roman numeral strings and converts them
    to their decimal integer equivalents according to standard Roman numeral rules.

    Class Attributes:
        roman (dict): Mapping of Roman numeral characters to their integer values.
    """

    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    def __init__(self, rom_value: str) -> None:
        """
        Initialize a RomanNumber instance.

        Args:
            rom_value (str): The Roman numeral string to be stored and validated.
                            If invalid, sets rom_value to None and prints an error.
        """
        if RomanNumber.is_roman(rom_value):
            self.rom_value = rom_value
        else:
            self.rom_value = None
            print('ошибка')

    def decimal_number(self) -> int:
        """
        Convert the Roman numeral to its decimal integer value.

        Handles standard Roman numeral subtraction rules (IV = 4, IX = 9, etc.)
        and additive notation for repeated characters.

        Returns:
            int | None: The decimal integer value of the Roman numeral,
                       or None if the stored value is invalid (None).
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

    def __repr__(self) -> str:
        """
        Return a string representation of the Roman numeral.

        Returns:
            str: The stored Roman numeral string, or 'None' if rom_value is None.
        """
        return f'{self.rom_value}'
