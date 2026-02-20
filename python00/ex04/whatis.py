import sys

RED = "\033[91m"
RESET = "\033[0m"


def odd_or_even() -> int:
    try:
        assert len(sys.argv) > 1, "please enter a number"
        assert len(sys.argv) == 2, "more than one argument is provided"
        assert sys.argv[1].isdigit(), "argument is not an integer"

        arg = int(sys.argv[1])

        print("I'm Even." if arg % 2 == 0 else "I'm Odd.")
        return 0

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")
        return 1


# -------------------- FUNCTION CALL --------------------

# s'execute uniquement quand le fichier est lance directement
if __name__ == "__main__":
    odd_or_even()
