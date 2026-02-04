RED = "\033[91m"
RESET = "\033[0m"

# Iterator : objet qui te donne ses valeurs une par une,
# peut etre parcouru avec for, mais ne peux pas revenir en arriere
# pas d'index, une fois consomme, fini


def ft_filter(function, iterable):
    """Returns an iterator where the items are filtered through
    a function to test if the item is accepted or not"""
    if function is None:
        # Utilisation d'un generator (type d'iterator)
        return (x for x in iterable if bool(x))
    else:
        return (x for x in iterable if function(x))


# -------------------- TESTS --------------------


# def is_upper(s):
#     return s.isupper()


# print(f"{BOLD}---------- filter() ----------{RESET}")
# print(list(filter(is_upper, "aBcDeF")))
# print(list(filter(None, [0, 1, "", "hi", False, True])))
# print()

# print(f"{BOLD}---------- ft_filter() ----------{RESET}")
# print(list(ft_filter(is_upper, "aBcDeF")))
# print(list(ft_filter(None, [0, 1, "", "hi", False, True])))
