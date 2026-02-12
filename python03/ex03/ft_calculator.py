RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


class Calculator:
    """Class used for arithmetic operations"""

    def __init__(self, vector):
        """Constructor for Calculator"""
        self.vector = vector

    def __add__(self, operator) -> None:
        """Does an addition on each element of a vector"""
        self.vector = [x + operator for x in self.vector]
        print(self.vector)

    def __mul__(self, operator) -> None:
        """Does a multiplication on each element of a vector"""
        self.vector = [x * operator for x in self.vector]
        print(self.vector)

    def __sub__(self, operator) -> None:
        """Does a substraction on each element of a vector"""
        self.vector = [x - operator for x in self.vector]
        print(self.vector)

    def __truediv__(self, operator) -> None:
        """Does a division on each element of a vector"""
        assert operator != 0, "can't divise by 0"
        self.vector = [x / operator for x in self.vector]
        print(self.vector)


def main():
    try:
        v1 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v1 + 5
        print("---")
        v2 = Calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
        v2 * 5
        print("---")
        v3 = Calculator([10.0, 15.0, 20.0])
        v3 - 5
        v3 / 5

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")
    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
