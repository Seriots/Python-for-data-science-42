from matplotlib import pyplot as plt
from load_image import ft_load
import numpy as np


def zoom_and_grey(img: np.ndarray) -> np.ndarray:
    """Zoom the image and transform it to greyscale

    Args:
        img (np.ndarray): The image in an np array format

    Returns:
        None
    """
    try:
        crop_img = img[100:500, 450:850]
        crop_img = np.ndarray(
            (400, 400, 1),
            buffer=np.dot(crop_img[..., :3], [0.299, 0.587, 0.144])
            )
        crop_img = crop_img.astype(int)

        print(f"New shape after slicing: {crop_img.shape} \
or {crop_img.shape[:2]}")

        print(f"[[{crop_img[0][0][:]}\n  {crop_img[0][1][:]}\n  \
{crop_img[0][2][:]}\n  ...\n  {crop_img[-1][-3][:]}\n  {crop_img[-1][-2][:]}\
\n  {crop_img[-1][-1][:]}]]")
    except Exception as e:
        print(f"An error occured: {e}")
        return []
    return crop_img


def main():
    """Get the content of the image and call zoom_and_grey on it
    """
    # np.set_printoptions(formatter=dict(float=lambda x: "%d" % x))
    img = ft_load("ex03/animal.jpeg")
    if img is []:
        return
    grey_img = zoom_and_grey(img)
    if grey_img is []:
        return
    plt.imshow(grey_img, cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()
