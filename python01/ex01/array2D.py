RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


# slice : avec slice() ou avec la syntaxe [start:end:step]
# permet d'extraire une portion specifique d'un tableau
def slice_me(family: list, start: int, end: int) -> list:
    """Takes a 2D array, prints its shape, and returns a truncated version
    of the array based on the provided start and end arguments"""

    assert family, "list to slice cannot be empty"
    assert isinstance(family, list), "please use a 2D list"
    assert all(isinstance(x, list) for x in family), "please use only lists"
    assert family and all(len(x) == len(family[0]) for x in family), (
        "list are not the same size"
    )
    assert isinstance(start, int) and isinstance(end, int), (
        "start and end must be intergers"
    )

    sliced = family[start:end]
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")

    return sliced


def main():
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

        print(f"{BOLD}{slice_me(family, 0, 2)}{RESET}\n")
        print(f"{BOLD}{slice_me(family, 1, -2)}{RESET}")

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")
    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
