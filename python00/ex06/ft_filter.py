RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def ft_filter(function, iterable):
    """Returns an iterator where the items are filtered through
    a function to test if the item is accepted or not"""

    # List comprehension:
    # Expression compacte pour construire une nouvelle liste en appliquant
    # une fonction a chaque element d'une autre liste
    # [expression for itetm in iterable if condition]

    if function is None:
        return [x for x in iterable if bool(x)]
    else:
        return [x for x in iterable if function(x)]


def is_upper(s):
    return s.isupper()


def main():
    print(f"{BOLD}---------- filter() ----------{RESET}")
    print(list(filter(is_upper, "aBcDeF")))
    print(list(filter(None, [0, 1, "", "hi", False, True])))
    print()

    print(f"{BOLD}---------- ft_filter() ----------{RESET}")
    print(list(ft_filter(is_upper, "aBcDeF")))
    print(list(ft_filter(None, [0, 1, "", "hi", False, True])))


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
