from matplotlib import pyplot as plt
from load_image import ft_load
import numpy as np


def transpose(img: np.ndarray) -> np.ndarray:
    """Transpose the image

    Args:
        img (np.ndarray): The image in an np array format

    Returns:
        np.ndarray: The transposed image
    """
    img = img.reshape(img.shape[0], img.shape[1])
    transposed_img = np.array([[img[j][i]
                                for j in range(len(img))]
                              for i in range(len(img[0]))]
                              )

    print(f"New shape after Transpose: {transposed_img.shape[:2]}")
    print(f"[{np.array2string(transposed_img[0])}\n ...\n \
{np.array2string(transposed_img[-1])}]")
    return np.array(transposed_img)


def main():
    """Get the content of the image and call zoom_and_grey on it
    """
    img = ft_load("ex04/animal.jpeg")
    if img is []:
        return

    np.set_printoptions(edgeitems=3, threshold=10)
    transposed_img = transpose(img)
    if transposed_img is []:
        return
    plt.imshow(transposed_img, cmap='gray')

    plt.show()


if __name__ == "__main__":
    main()
