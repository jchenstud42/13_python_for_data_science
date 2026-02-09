import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

RED = "\033[91m"
RESET = "\033[0m"


def prepare_img(image):
    """Prepares an image to be displayed"""
    try:
        crop = image[100:500, 450:850]
        g = np.dot(crop[..., :3], [0.299, 0.587, 0.114])
        res = g[:, :, None]
        print(f"The shape of image is: {res.shape} or {res.squeeze().shape}")
        print(res)

        return g

    except Exception as error:
        raise RuntimeError(f"{RED}failed to prepare image: {error}{RESET}")


def rotate_img(image):
    """Rotates an image by 90° counterclockwise, and displays it"""
    try:
        g = prepare_img(image)
        # rotated : Parcours les lignes (y for len(g))
        # les colonnes (x for len(g[0])) et on les intervertis :
        # rotated[x][y] = g[y][x] -> transposition
        rotated = [[g[y][x] for y in range(len(g))] for x in range(len(g[0]))]
        rotated = np.array(rotated)

        print(f"\nNew shape after transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap="g", vmin=0, vmax=255)
        plt.show()

    except Exception as error:
        raise RuntimeError(f"{RED}failed to display image: {error}{RESET}")


def main():
    try:
        img = ft_load("../animal.jpeg")
        rotate_img(img)

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
