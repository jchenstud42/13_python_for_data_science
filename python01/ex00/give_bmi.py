import numpy as np

RED = "\033[91m"
RESET = "\033[0m"


def give_bmi(h: list[int | float], w: list[int | float]) -> list[int | float]:
    """Calculate the BMI value with the height and the weight inputed"""

    assert isinstance(h, list), "please use a list for height"
    assert isinstance(w, list), "please use a list for weight"
    assert all(isinstance(x, (int, float)) for x in h + w), (
        "only int and float are accepted"
    )
    assert all(x != 0 for x in h + w), "input valid value"
    assert len(h) == len(w), "lists are not the same size"

    height = np.array(h)
    weight = np.array(w)

    return (weight / (height * height)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Checks if the BMI is below the inputed limit"""

    assert isinstance(bmi, list), "please use a list for bmi"
    assert all(isinstance(x, (int, float)) for x in bmi), (
        "only int and float are accepted"
    )
    assert isinstance(limit, int), "please use an int for limit"

    return [x > limit for x in bmi]


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")
        return 1


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
