RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


# *args : arbitrary arg, permet un nb d'arg inconnu en les stockant ds un tuple
# **kwargs : arbitrary keyword arg, meme chose, mais recoit un dictionnaire
def ft_statistics(*args: any, **kwargs: any) -> None:
    """Takes any number of arguments and keyword arguments,\
        and makes the Mean, Mediam, Quartile (Q1&q3), Standard Deviation\
        and Variance according to the **kwargs asked"""
    try:
        assert len(args) > 0 and len(kwargs) > 0, "missing arguments"

        for value in kwargs.values():
            if value == "mean":
                mean = sum(args) / len(args)
                print(f"mean : {mean}")

            elif value == "med":
                median = sorted(args)
                # // : division entiere, ne garde pas le restant
                mid = len(median) // 2
                # ~ : operateur bitwise NOT : -(mid + 1)
                print(f"median : {int((median[mid] + median[~mid]) / 2)}")

            elif value == "qs":
                slist = sorted(args)
                mid = len(args) // 2
                low_h = slist[: mid + 1]
                up_h = slist[mid:]

                len_lower = len(low_h)
                mid_lower = len_lower // 2
                if len_lower % 2 == 1:
                    q1 = float(low_h[mid_lower])
                else:
                    q1 = float((low_h[mid_lower] + low_h[mid_lower - 1]) / 2)

                len_upper = len(up_h)
                mid_upper = len_upper // 2
                if len_upper % 2 == 1:
                    q3 = float(up_h[mid_upper])
                else:
                    q3 = float((up_h[mid_upper] + up_h[mid_upper - 1]) / 2)
                print(f"quartile : [{q1}, {q3}]")

            elif value == "std":
                len_std = len(args)
                mean_std = sum(args) / len_std
                squared_diffs = [(x - mean_std) ** 2 for x in args]
                var_std = sum(squared_diffs) / len_std

                print(f"std : {var_std**0.5}")

            elif value == "var":
                len_var = len(args)
                mean_var = sum(args) / len_var
                squared_diffs = [(x - mean_var) ** 2 for x in args]
                var = sum(squared_diffs) / len_var

                print(f"var : {var}")

    except Exception:
        print("ERROR")


def main():
    try:
        ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="med", tata="qs")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hlo="std", wrld="var")
        print("-----")
        ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejf="hehe", ejd="kde")
        print("-----")
        ft_statistics(toto="mean", tutu="med", tata="qs")

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
