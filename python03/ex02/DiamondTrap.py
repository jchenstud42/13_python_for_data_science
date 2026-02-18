from S1E7 import Baratheon, Lannister

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


class King(Baratheon, Lannister):
    """Diamond class of Baratheon et Lannister"""

    def __init__(self, first_name, alive=True):
        """Constructor of the King class"""
        self.first_name = first_name
        self.alive = alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # indique la representation en str d'un objet, lisible
    def __str__(self):
        """Representiong the King for human"""
        return f"{self.first_name}, {self.eyes}, {self.hairs}"

    # indique une str qui sert a la representation d'une classe, pour debugger
    def __repr__(self):
        """Representiong the King for debugging"""
        return "Vector: ('{}', '{}', '{}')".format(
            self.family_name, self.eyes, self.hairs
        )

    def is_alive(self):
        """Checks if the character is alive"""
        return self.alive

    # property : methode deguisee en attribut, equivalent d'un set-getter
    @property
    def eyes(self):
        """Property for Eyes color getter"""
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        """Property Eyes color setter"""
        self._eyes = color

    @property
    def hairs(self):
        """Property Hair color getter"""
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        """Property Hair color setter"""
        self._hairs = color

    # Wrapper qui ne servent pas a grand chose, pour ne pas casser le main
    def get_eyes(self):
        """Eyes color getter"""
        return self.eyes

    def set_eyes(self, color):
        """Eyes color setter"""
        self.eyes = color

    def get_hairs(self):
        """Hair color getter"""
        return self.hairs

    def set_hairs(self, color):
        """Hair color setter"""
        self.hairs = color


def main():
    try:
        Joffrey = King("Joffrey")
        print(Joffrey.__dict__)

        Joffrey.set_eyes("blue")
        Joffrey.set_hairs("light")
        print(Joffrey.get_eyes())
        print(Joffrey.get_hairs())
        print(Joffrey.__dict__)

    except TypeError as error:
        print(f"{RED}TypeError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
