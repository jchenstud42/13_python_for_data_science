import random
import string
from dataclasses import dataclass, field

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


# dataclasse : classe permettant de se concentrer sur la definition
# des attributs, sans avoir a implementer de constructeurs ni de methodes
@dataclass
class Student:
    """Example of a dataclass that takes as arguments a name and nickname"""

    name: str
    surname: str
    # field : permet de configurer le comportement de l'attribut
    # exemple : init=False > retirer l'attribut du constructeur __init__
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[:1] + self.surname
        self.id = generate_id()


def main():
    try:
        print(f"{BOLD}\n---------- Valid Test ----------{RESET}")
        student = Student(name="Edward", surname="agle")
        print(f"{student}\n")

        print(f"{BOLD}---------- Invalid Test ----------{RESET}")
        student = Student(name="Edward", surname="agle", id="toto")
        print(f"{student}\n")

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
