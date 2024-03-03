import matplotlib.pyplot as plt
import seaborn as sns

from load_csv import load


def main():
    """
        Load a dataset and get the life expectancy of a country
        to display it in a graph.
    """
    TARGETED_COUNTRY = "France"

    dataset = load("ex01/life_expectancy_years.csv")
    if dataset is None:
        return

    country = dataset[dataset['country'] == TARGETED_COUNTRY].squeeze()
    if country.empty:
        print(f"Country {TARGETED_COUNTRY} not found")
        return

    try:
        sns.lineplot(x=dataset.columns[1:].astype(int), y=country[1:])

    except ValueError as e:
        print(e)
        return

    plt.title(f"{TARGETED_COUNTRY} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    try:
        plt.show()
    except KeyboardInterrupt:
        print("Interrupted by the user")


if __name__ == '__main__':
    main()
