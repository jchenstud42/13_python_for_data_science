import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

RED = "\033[91m"
RESET = "\033[0m"


def prepare_img(image):
    try:
        crop = image[100:500, 450:850]
        gray = np.dot(crop[..., :3], [0.299, 0.587, 0.114])
        res = gray[:, :, None]
        print(f"The shape of image is: {res.shape} or {res.squeeze().shape}")
        print(res)

        return gray

    except Exception as error:
        raise RuntimeError(f"{RED}failed to prepare image: {error}{RESET}")


def rotate_img(image):
    try:
        gray = prepare_img(image)
        rotated = [[gray[y][x] for y in range(len(gray))] for x in range(len(gray[0]))]
        rotated = np.array(rotated)

        print(f"\nNew shape after transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap="gray", vmin=0, vmax=255)
        plt.show()

    except Exception as error:
        raise RuntimeError(f"{RED}failed to display image: {error}{RESET}")


def main():
    try:
        img = ft_load("../animal.jpeg")
        rotate_img(img)

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
