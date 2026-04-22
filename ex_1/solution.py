class Circle:
    """
    A class representing a circle with radius and area calculations.

    Tracks all created circle instances and provides methods for calculating
    individual and total areas of all circles.

    Attributes:
        all_circles (list): Class variable storing all Circle instances.
        pi (float): Class constant representing the value of pi.
    """

    all_circles = []
    pi = 3.1415

    def __init__(self, radius: int = 1):
        """
        Initialize a new Circle instance.

        Args:
            radius (int, optional): The radius of the circle. Defaults to 1.
        """
        self._radius = radius
        Circle.all_circles.append(self)

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle (pi * radius^2).
        """
        return Circle.pi * (self._radius) ** 2

    def __repr__(self) -> str:
        """
        Return a string representation of the circle.

        Returns:
            str: The radius of the circle as a string.
        """
        return f'{self._radius}'

    @staticmethod
    def total_area() -> float:
        """
        Calculate the total area of all circles created.

        Returns:
            float: The sum of areas of all Circle instances.
        """
        total = 0
        for circle in Circle.all_circles:
            total += circle.area()
        return total
