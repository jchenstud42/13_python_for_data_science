from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def life_vs_income_graph(income_dt, life_dt):
    """Displays the projection life expectancy in relation\
        to the gross national product of 1900 for each country"""
    try:
        i_1900 = income_dt[["country", "1900"]].rename(
            columns={"1900": "gross_national_product"}
        )
        life_1900 = life_dt[["country", "1900"]].rename(
            columns={"1900": "life_expectancy"}
        )

        # merge et garde seulement les pays en commun
        merged = pd.merge(i_1900, life_1900, on="country")

        ax = merged.plot(
            kind="scatter",
            x="gross_national_product",
            y="life_expectancy",
            title="1900",
            xlabel="Gross domestic product",
            ylabel="Life Expectancy",
        )

        # scale : affichage logarithmique
        ax.set_xscale("log")
        ax.set_xticks([300, 1000, 10000])
        ax.set_xticklabels(["300", "1k", "10k"])

        plt.show()

    except KeyError as error:
        print(f"{RED}Error: {error}{RESET}")


def main():
    try:
        dt = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        dt2 = load("../life_expectancy_years.csv")
        life_vs_income_graph(dt, dt2)

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
