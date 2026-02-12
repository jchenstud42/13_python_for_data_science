from S1E9 import Character

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name, alive=True):
        """Constructor of Baratheon class"""
        self.first_name = first_name
        self.alive = alive
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    # indique la representation en str d'un objet, lisible
    def __str__(self):
        """Representiong the Baratheon family for human"""
        return f"{self.first_name}, {self.eyes}, {self.hairs}"

    # indique une str qui sert a la representation d'une classe, pour debugger
    def __repr__(self):
        """Representiong the Baratheon family for debugging"""
        return "Vector: ('{}', '{}', '{}')".format(
            self.family_name, self.eyes, self.hairs
        )

    def is_alive(self):
        """Checks if the character is alive"""
        return self.alive


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, alive=True):
        """Constructor of Lannister class"""
        self.first_name = first_name
        self.alive = alive
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    # indique la representation en str d'un objet, lisible
    def __str__(self):
        """Representiong the Lannister family for human"""
        return f"{self.first_name}, {self.eyes}, {self.hairs}"

    # indique une str qui sert a la representation d'une classe, pour debugger
    def __repr__(self):
        """Representiong the Lannister family for debbuger"""
        return "Vector: ('{}', '{}', '{}')".format(
            self.family_name, self.eyes, self.hairs
        )

    def is_alive(self):
        """Checks if the character is alive"""
        return self.alive

    # Class method : Methode qui agit sur la classe, pas seulement sur l'objet
    @classmethod
    def create_lannister(cls, first_name, alive):
        """Creates a Lannister character"""
        created = cls(first_name)
        created.alive = alive

        return created


def main():
    try:
        Robert = Baratheon("Robert")
        print(Robert.__dict__)
        print(Robert.__str__)
        print(Robert.__repr__)
        print(Robert.is_alive())
        Robert.die()
        print(Robert.is_alive())
        print(Robert.__doc__)
        print("---")
        Cersei = Lannister("Cersei")
        print(Cersei.__dict__)
        print(Cersei.__str__)
        print(Cersei.is_alive())
        print("---")
        Jaine = Lannister.create_lannister("Jaine", True)
        print(f"Name : {Jaine.first_name, type(Jaine).__name__}, ", end="")
        print(f"Alive : {Jaine.is_alive()}")

    except TypeError as error:
        print(f"{RED}TypeError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
