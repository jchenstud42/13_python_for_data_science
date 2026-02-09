import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

RED = "\033[91m"
RESET = "\033[0m"


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received"""
    try:
        # inverse tous les canaux RGB (ex: R = 255 - 120 = 135)
        inverted = 255 - array

        plt.imshow(inverted)
        plt.title("Inverted")
        plt.axis("off")
        plt.show()
        return inverted

    except Exception as error:
        raise RuntimeError(f"{RED}failed to inverts image: {error}{RESET}")


def ft_red(array) -> np.ndarray:
    """Applies a red color filter to the image received"""
    try:
        # desactive les canaux green et bleu
        red = array.copy()
        red[:, :, 1] = 0
        red[:, :, 2] = 0

        plt.imshow(red)
        plt.title("Red")
        plt.axis("off")
        plt.show()
        return red

    except Exception as error:
        raise RuntimeError(f"{RED}failed to apply red filter: {error}{RESET}")


def ft_green(array) -> np.ndarray:
    """Applies a green color filter to the image received"""
    try:
        green = array.copy()
        green[:, :, 0] = 0
        green[:, :, 2] = 0

        plt.imshow(green)
        plt.title("Green")
        plt.axis("off")
        plt.show()
        return green

    except Exception as error:
        raise RuntimeError(f"{RED}failed to apply green filter: {error}{RESET}")


def ft_blue(array) -> np.ndarray:
    """Applies a blue color filter to the image received"""
    try:
        blue = array.copy()
        blue[:, :, 0] = 0
        blue[:, :, 1] = 0

        plt.imshow(blue)
        plt.title("Blue")
        plt.axis("off")
        plt.show()
        return blue

    except Exception as error:
        raise RuntimeError(f"{RED}failed apply blue filter: {error}{RESET}")


def ft_grey(array) -> np.ndarray:
    """Applies a grey color filter to the image received"""
    try:
        arr = array.copy()
        grey = np.dot(arr[..., :3], [0.299, 0.587, 0.114])

        plt.imshow(grey, cmap="grey", vmin=0, vmax=255)
        plt.title("Grey")
        plt.axis("off")
        plt.show()
        return grey

    except Exception as error:
        raise RuntimeError(f"{RED}failed apply grey filter: {error}{RESET}")


def main():
    try:
        array = ft_load("../landscape.jpg")

        ft_invert(array)
        ft_red(array)
        ft_green(array)
        ft_blue(array)
        ft_grey(array)
        # permet d'afficher la documentation d'une fonction
        print(ft_invert.__doc__)

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
