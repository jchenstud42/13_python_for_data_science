BLUE = "\033[94m"
RED = "\033[91m"
BOLD = "\033[1m"
BLUE_BOLD = BOLD + BLUE
RED_BOLD = BOLD + RED
RESET = "\033[0m"


def all_thing_is_obj(object: any) -> int:
    if type(object) is list:
        print(BLUE_BOLD + "List :", end=" " + RESET)
    elif type(object) is tuple:
        print(BLUE_BOLD + "Tuple :", end=" " + RESET)
    elif type(object) is set:
        print(BLUE_BOLD + "Set :", end=" " + RESET)
    elif type(object) is dict:
        print(BLUE_BOLD + "Dict :", end=" " + RESET)
    elif type(object) is str:
        print(BLUE_BOLD + object + "is in the kitchen :", end=" " + RESET)
    else:
        print(RED_BOLD + "Type not found" + RESET)
        return 42
    print(type(object))

    return 42


# ------------- TESTS --------------#

# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello": "titi!"}

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("Brian")
# all_thing_is_obj("Totozoom")
# print(all_thing_is_obj(10))
