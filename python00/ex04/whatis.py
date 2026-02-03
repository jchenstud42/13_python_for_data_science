import sys

RED = "\033[91m"
RESET = "\033[0m"


def odd_or_even() -> int:
    if len(sys.argv) <= 1:
        return 1
    elif len(sys.argv) > 2:
        print(RED + "AssertionError: more than one argument is provided" + RESET)
        return 1

    try:
        arg = int(sys.argv[1])
    except ValueError:
        print(RED + "AssertionError: argument is not an interger" + RESET)
        return 1

    print("I'm Even." if arg % 2 == 0 else "I'm Odd.")
    return 0


# -------------------- FUNCTION CALL --------------------

# s'execute uniquement quand le fichier est lance directement
if __name__ == "__main__":
    odd_or_even()
