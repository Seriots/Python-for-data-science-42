import pandas


def check_path(func):
    """Decorator to handle path error

    Args:
        func (fn): function to be decorated
    """
    def wrapper(path):
        """Wrapper function to handle path error

        Args:
            path (str): The path to test

        Raises:
            ValueError: If the path is null or if its not a CSV file

        Returns:
            Exception: Handle all errors when opening a file
        """
        try:
            with open(path) as _:
                pass
            if not path.endswith(".csv"):
                raise ValueError("File is not a CSV")
            if not path:
                raise ValueError("File path is empty")
        except ValueError as e:
            print(e)
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        return func(path)
    return wrapper


@check_path
def load(path: str) -> pandas.DataFrame:
    """Load a CSV file

    Args:
        path (str): Path to he CSV file

    Returns:
        pandas.DataFrame: Return the dataset
    """
    dataset = pandas.read_csv(path)
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset
