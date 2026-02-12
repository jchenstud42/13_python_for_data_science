from abc import ABC, abstractmethod

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


class Character(ABC):
    """Abstract class which can take a first_name, and\
        can toggle if it's alive or not"""

    @abstractmethod
    def is_alive(self):
        """Checks if the character is alive"""
        pass

    # Concrete method : don't have to be redefined
    def die(self):
        """Kills the character"""
        self.alive = False
        return self


class Stark(Character):
    """Class which inherits from Character"""

    def __init__(self, first_name, alive=True):
        """Constructor of Stark class"""
        self.first_name = first_name
        self.alive = alive

    def is_alive(self):
        """Checks if the character is alive"""
        return self.alive


def main():
    try:
        print(f"{BOLD}--- Valid tests{RESET}")
        Ned = Stark("Ned")
        print(Ned.__dict__)
        print(Ned.is_alive())
        Ned.die()
        print(Ned.is_alive())
        print(Ned.__doc__)
        print(Ned.__init__.__doc__)
        print(Ned.die.__doc__)
        print("---")
        Lyanna = Stark("Lyanna", False)
        print(Lyanna.__dict__)

        # Doesn't work :
        print(f"{BOLD}\n--- Invalid test{RESET}")
        hodor = Character("hodor")
        hodor.die()

    except TypeError as error:
        print(f"{RED}TypeError: {error}{RESET}")
        print(f"{RED}Can't instantiate abstract class Character{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
