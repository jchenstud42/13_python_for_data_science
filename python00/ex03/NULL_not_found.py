BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
BLUE_BOLD = BOLD + BLUE
RED_BOLD = BOLD + RED
RESET = "\033[0m"


def NULL_not_found(object: any) -> int:
    if object is None:
        print(BLUE_BOLD + "Nothing : " + RESET + "None", end=" ")
    elif type(object) is float and object != object:
        print(BLUE_BOLD + "Cheese : " + RESET + "nan", end=" ")
    elif type(object) is int and object == 0:
        print(BLUE_BOLD + "Zero : " + RESET + "0", end=" ")
    elif type(object) is str and object == "":
        print(BLUE_BOLD + "Empty :", end=" " + RESET)
    elif type(object) is bool and not object:
        print(BLUE_BOLD + "Fake : " + RESET + "False", end=" ")
    else:
        print(RED_BOLD + "Type not found" + RESET)
        return 1
    print(type(object))

    return 0


# ------------- TESTS --------------#

# from NULL_not_found import NULL_not_found

# Nothing = None
# Garlic = float("NaN")
# Zero = 0
# Empty = ""
# Fake = False

# NULL_not_found(Nothing)
# NULL_not_found(Garlic)
# NULL_not_found(Zero)
# NULL_not_found(Empty)
# NULL_not_found(Fake)
# print(NULL_not_found("Brian"))
