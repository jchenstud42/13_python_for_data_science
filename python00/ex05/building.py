import sys

BOLD = "\033[1m"
RED = "\033[91m"
RESET = "\033[0m"


def character_calculator(inp) -> int:
    """Displays the sums of its upper-case characters,
    lower-case characters, punctuation, digits, and spaces"""

    upper = sum(1 for c in inp if c.isupper())
    lower = sum(1 for c in inp if c.islower())
    punct = sum(1 for x in inp if x in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}")
    space = inp.count(" ")
    digit = sum(1 for c in inp if c.isdigit())

    print(
        f"{BOLD}The text contains {len(inp)} characters:\n{RESET}",
        f"{BOLD}{upper}{RESET} upper letters\n",
        f"{BOLD}{lower}{RESET} lower letters\n",
        f"{BOLD}{punct}{RESET} punctuation marks\n",
        f"{BOLD}{space}{RESET} spaces\n",
        f"{BOLD}{digit}{RESET} digits",
    )


def main():
    try:
        assert len(sys.argv) < 3, "Too many arguments"

        if len(sys.argv) == 1:
            print(f"{BOLD}What is the text to count?{RESET}")
            inp = input()
            print("")
        else:
            inp = sys.argv[1]

        character_calculator(inp)

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
