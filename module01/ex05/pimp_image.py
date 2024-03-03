import numpy as np


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    array = 255 - array
    return array


def ft_red(array) -> np.ndarray:
    """Get the red channel of the image"""
    array = (1, 0, 0) * array
    return array


def ft_green(array) -> np.ndarray:
    """Get the green channel of the image"""
    array = array - (255, 0, 255)
    return array


def ft_blue(array) -> np.ndarray:
    """Get the blue channel of the image"""
    new_array = np.zeros_like(array)
    new_array[:, :, 2] = array[:, :, 2]
    return new_array


def ft_grey(array) -> np.ndarray:
    """Convert the image to grayscale"""
    weights = np.array([0.2989, 0.5870, 0.1140])
    array = np.sum(array / (1 / weights), axis=2)
    return array
