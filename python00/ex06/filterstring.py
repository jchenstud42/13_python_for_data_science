import sys

RED = "\033[91m"
RESET = "\033[0m"


def filterstring(S, N):
    """Function that output a list of words from S(string)
    that have a length greater than N(interger)"""
    # x : element de S.split, sur lequel on va verifier la condition lambda
    return (x for x in S.split() if (lambda y: len(y) > N)(x))


def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert all(arg.isalpha() for arg in sys.argv[1].split()), (
            "string must contain only letters and spaces"
        )
        n = int(sys.argv[2])

        print(list(filterstring(sys.argv[1], n)))

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")
    except ValueError:
        print(f"{RED}ValueError: second argument must be an interger{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
