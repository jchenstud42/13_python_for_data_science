import os
import pandas as pd

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def load(path: str):
    """Writes the dimensions of the data set, and returns it"""
    if not os.path.exists(path):
        print(f"{RED}Error: file '{path}' not found{RESET}")
        return None

    ext = os.path.splitext(path)[1]
    if ext != ".csv":
        print(f"{RED}Error: only .csv files allowed{RESET}")
        return None

    try:
        dataframe = pd.read_csv(path)
        return dataframe

    except Exception as error:
        print(f"{RED}failed to load {path}: {error}{RESET}")
        return None


def main():
    try:
        print(load("../life_expectancy_years.csv"))

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
