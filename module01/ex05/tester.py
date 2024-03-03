from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
from matplotlib import pyplot as plt


array = ft_load("ex05/landscape.jpg")
fig = plt.figure(figsize=(7, 10))

fig.add_subplot(3, 2, 1)
plt.imshow(array)
plt.title("original")

invert = ft_invert(array)
fig.add_subplot(3, 2, 2)
plt.imshow(invert)
plt.title("Invert")

red = ft_red(array)
fig.add_subplot(3, 2, 3)
plt.imshow(red)
plt.title("Red")

green = ft_green(array)
fig.add_subplot(3, 2, 4)
plt.imshow(green)
plt.title("Green")

blue = ft_blue(array)
fig.add_subplot(3, 2, 5)
plt.imshow(blue)
plt.title("Blue")

grey = ft_grey(array)
fig.add_subplot(3, 2, 6)
plt.imshow(grey, cmap="gray")
plt.title("Grey")

print(ft_invert.__doc__)

plt.show()
