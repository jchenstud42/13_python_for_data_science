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
        i_1900 = income_dt[["country", "1900"]].rename(columns={"1900": "inc"})
        life_1900 = life_dt[["country", "1900"]].rename(
            columns={"1900": "life_expectancy"}
        )

        merged = pd.merge(i_1900, life_1900, on="country")

        merged.plot(
            kind="scatter",
            x="income",
            y="life_expectancy",
            title="title",
        )
        plt.xlabel("Income per Person (GDP per capita, inflation adjusted)")
        plt.ylabel("Life Expectancy (years)")
        plt.show()

    except KeyError as error:
        print(f"{RED}Error: country not found in the dataframe: {error}{RESET}")

    # def life_vs_income_graph(income_dt, life_dt):
    # """Displays life expectancy vs income per person in 1900"""
    # try:
    #     income_1900 = income_dt[["country", "1900"]].rename(columns={"1900": "income"})
    #     life_1900   = life_dt[["country", "1900"]].rename(columns={"1900": "life_expectancy"})

    #     merged = pd.merge(income_1900, life_1900, on="country")

    #     # Scatter plot avec Pandas
    #     merged.plot(
    #         kind="scatter",
    #         x="income",
    #         y="life_expectancy",
    #         color="teal",
    #         edgecolor="black",
    #         figsize=(10, 6)
    #     )

    #     plt.title("Life Expectancy vs Income per Person in 1900")
    #     plt.xlabel("Income per Person (GDP per capita, inflation adjusted)")
    #     plt.ylabel("Life Expectancy (years)")
    #     plt.grid(True)
    #     plt.show()

    # except KeyError as error:
    #     print(f"{RED}Error: country not found in the dataframe: {error}{RESET}")


# //////////////////////////////////////////////////////////////////////////////////

# try:
#     # .T : transposition (inversion) annees et pays
#     # regex : regular expression, langage pour decrire des motifs
#     # dans du texte -> cherche dans la string et remplace
#     # Ici : remplace les notions LMB par leur valeur correspondante
#     c_dt = (
#         dt.set_index("country")
#         .loc[[c1, c2]]
#         .T.replace({"K": "e3", "M": "e6", "B": "e9"}, regex=True)
#         .astype(float)
#     )

#     # Annees str -> int pour pouvoir slice correctement
#     c_dt.index = c_dt.index.astype(int)
#     c_dt = c_dt.loc[1800:2050]

#     # division pour afficher par tranche de 20 la population
#     c_dt = c_dt / 1e6

#     ax = c_dt.plot(
#         title="Population Projections",
#         xlabel="Year",
#         ylabel="Population",
#     )

#     ax.set_xticks(range(1800, 2051, 40))
#     ax.set_yticks(range(20, int(c_dt.max().max()) + 1, 20))
#     ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{int(y)}M"))

#     plt.show()

# except KeyError:
#     print(f"{RED}Error: country not found in the dataframe{RESET}")


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
