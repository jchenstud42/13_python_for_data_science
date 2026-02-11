from load_csv import load
import matplotlib.pyplot as plt

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"


def life_expec_graph(dt, country):
    """Displays a graph of a country's life expectancy projection \
        from a dataframe"""
    try:
        country_data = dt.set_index("country").loc[country].astype(float)
        country_data.index = country_data.index.astype(int)

        # Appelle matplotlib en utilisant Pandas
        ax = country_data.plot(
            title=f"{country} Life expectancy Projections",
            xlabel="Year",
            ylabel="Life expectancy",
        )
        ax.set_xticks(range(1800, 2101, 40))

        plt.show()

    except KeyError:
        print(
            f"{RED}Error: country '{country}' not found in \
              the dataframe{RESET}"
        )


def main():
    try:
        dataframe = load("../life_expectancy_years.csv")
        life_expec_graph(dataframe, "France")

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
