import matplotlib.pyplot as plt
import seaborn as sns

from load_csv import load


def update_data(value: str) -> str:
    """Update

    Args:
        value (str): The value to update

    Returns:
        str: The updated value
    """
    try:
        if value.find("k") != -1:
            value = value.replace("k", "")
            value = int(float(value) * 1000)
        elif value.find("M") != -1:
            value = value.replace("M", "")
            value = int(float(value) * 1000000)
        elif value.find("B") != -1:
            value = value.replace("B", "")
            value = int(float(value) * 1000000000)
    except ValueError:
        raise ValueError(f"Invalid value: {value}")

    return str(value)


def main():
    """Load a dataset and get the population of multiple country
        to display all of them in a graph.
    """

    dataset = load("ex02/population_total.csv")
    if dataset is None:
        return

    countries = ['France', 'Belgium']

    country = [dataset[dataset['country'] == c].squeeze() for c in countries]
    for i, c in enumerate(country):
        if c.empty:
            print(f"Country {countries[i]} not found")
            return
    try:
        country = [c[1:].apply(update_data) for c in country]
    except ValueError as e:
        print(e)
        return

    for i, c in enumerate(country):
        sns.lineplot(
            x=dataset.columns[1:252].astype(int),
            y=c[:251].astype(int),
            legend='full',
            label=countries[i]
            )

    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")

    plt.xticks([i for i in range(1800, 2060, 40)])
    plt.yticks([20000000, 40000000, 60000000], ["20M", "40M", "60M"])

    plt.legend(loc='lower right')
    try:
        plt.show()
    except KeyboardInterrupt:
        print("Interrupted by the user")


if __name__ == '__main__':
    main()
