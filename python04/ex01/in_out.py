RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def square(x: int | float) -> int | float:
    """Returns the square of argument"""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of argument by itself"""
    return x**x


def outer(x: int | float, function) -> object:
    """Takes as argument a number and a function, and returns an object\
    that when called, returns the result of the arguments calculation"""
    value = x

    def inner() -> float:
        nonlocal value
        # value : equivalent de static
        value = function(value)
        return value

    return inner


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
