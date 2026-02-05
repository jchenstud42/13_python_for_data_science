import numpy as np

RED = "\033[91m"
RESET = "\033[0m"


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """Calculate the BMI value with the height and the weight inputed"""
    height = np.array(h)
    weight = np.array(w)

    return (weight / (height * height)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if the BMI is below the inputed limit"""
    return [x > limit for x in bmi]


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        assert isinstance(height, list), "please use a list for height"
        assert isinstance(weight, list), "please use a list for weight"
        assert all(isinstance(x, (int, float)) for x in height + weight), (
            "only int and float in the lists"
        )
        assert all(x != 0 for x in height + weight), "input valid value"
        assert len(height) == len(weight), "lists are not the same size"

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
