from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def pop_proj_graph(dt, c1, c2):
    """Displays a graph comparing two countrys population projection \
        per year from a dataframe"""
    try:
        # .T : transposition (inversion) annees et pays
        # regex : regular expression, langage pour decrire des motifs
        # dans du texte -> cherche dans la string et remplace
        # Ici : remplace les notions LMB par leur valeur correspondante
        c_dt = (
            dt.set_index("country")
            .loc[[c1, c2]]
            .T.replace({"K": "e3", "M": "e6", "B": "e9"}, regex=True)
            .astype(float)
        )

        # Annees str -> int pour pouvoir slice correctement
        c_dt.index = c_dt.index.astype(int)
        c_dt = c_dt.loc[1800:2050]

        # division pour afficher par tranche de 20 la population
        c_dt = c_dt / 1e6

        ax = c_dt.plot(
            title="Population Projections",
            xlabel="Year",
            ylabel="Population",
        )

        ax.set_xticks(range(1800, 2051, 40))
        ax.set_yticks(range(20, int(c_dt.max().max()) + 1, 20))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f"{int(y)}M"))

        plt.show()

    except KeyError:
        print(f"{RED}Error: country not found in the dataframe{RESET}")


def main():
    try:
        dataframe = load("../population_total.csv")
        pop_proj_graph(dataframe, "France", "Belgium")

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
