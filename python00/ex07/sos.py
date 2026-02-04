import sys

RED = "\033[91m"
RESET = "\033[0m"

NESTED_MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    " ": "/ ",
}


def str_to_morse(str, dictionnary):
    """Takes a string and encodes it in Morse Code"""
    cap_str = str.upper()
    # return [] : retourne une list
    # join() : transforme la liste en chaine
    return " ".join(dictionnary.get(c) for c in cap_str)


def main():
    try:
        assert len(sys.argv) == 2, "please enter one string only"
        assert all(c.isalnum() or c == " " for c in sys.argv[1]), (
            "supports space and alphanumeric characters only"
        )
        print(str_to_morse(sys.argv[1], NESTED_MORSE))

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
