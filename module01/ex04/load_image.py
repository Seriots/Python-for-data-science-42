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

    try:
        crop_img = img[100:500, 450:850]
        crop_img = np.ndarray(
            (400, 400, 1),
            buffer=np.dot(crop_img[..., :3], [0.299, 0.587, 0.144])
            )
        crop_img = crop_img.astype(int)

        print(f"The shape of image is: {crop_img.shape} \
or {crop_img.shape[:2]}")

        print(f"[[{crop_img[0][0][:]}\n  {crop_img[0][1][:]}\n  \
{crop_img[0][2][:]}\n  ...\n  {crop_img[-1][-3][:]}\n  {crop_img[-1][-2][:]}\
\n  {crop_img[-1][-1][:]}]]")
    except Exception as e:
        print(f"An error occured: {e}")
        return []
    return crop_img
