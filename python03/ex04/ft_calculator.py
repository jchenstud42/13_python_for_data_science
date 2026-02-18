RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


# decorator : fonction qui modifie le comportement d'autres ft/methodes
# en ajoutant des fonctionnalites supplementaires av ou apres leur exec


class Calculator:
    """Class used for arithmetic operations"""

    # staticmethod : permet d'indiquer une methode qui fonctionne
    # independamment des instances de classe. Ne peut pas modifier
    # l'etat d'un objet -> ft utilitaire
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Multiply each element of two vectors"""
        result = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is : {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Adds each element of two vectors"""
        result = [float(x + y) for x, y in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Substracts each element of two vectors"""
        result = [float(x - y) for x, y in zip(V1, V2)]
        print(f"Sous Vector is : {result}")


def main():
    try:
        a = [5, 10, 2]
        b = [2, 4, 3]
        Calculator.dotproduct(a, b)
        Calculator.add_vec(a, b)
        Calculator.sous_vec(a, b)

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------


if __name__ == "__main__":
    main()
