import matplotlib.pyplot as plt
import seaborn as sns

from load_csv import load


def main():
    """Load a dataset and get the population of multiple country
        to display all of them in a graph.
    """

    YEAR = '1900'

    dataset_life = load("ex03/life_expectancy_years.csv")
    if dataset_life is None:
        return

    dataset_income =\
        load("ex03/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if dataset_income is None:
        return

    life = dataset_life[YEAR]
    income = dataset_income[YEAR]

    sns.scatterplot(x=income, y=life)

    plt.title(f"{YEAR}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
    try:
        plt.show()
    except KeyboardInterrupt:
        print("Interrupted by the user")


if __name__ == '__main__':
    main()
