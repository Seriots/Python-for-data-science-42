from matplotlib import image
import numpy as np
import PIL


def ft_load(path: str) -> np.ndarray:
    """Load the image at the given path

    Args:
        path (str): Path to the image to load

    Returns:
        list: Image in 3D List format with RGB values
    """
    try:
        img = image.imread(path)

    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: '{path}'")
        return []
    except IsADirectoryError:
        print(f"IsADirectoryError: Is a directory: '{path}'")
        return []
    except PermissionError:
        print(f"PermissionError: Permission denied: '{path}'")
        return []
    except PIL.UnidentifiedImageError:
        print(f"UnidentifiedImageError: Cannot identify image file '{path}'")
        return []
    except Exception as e:
        print(f"An error occured: {e}")
        return []

    print(f"The shape of the image is: {img.shape}")
    return img
