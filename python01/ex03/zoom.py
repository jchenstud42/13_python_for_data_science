import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

RED = "\033[91m"
RESET = "\033[0m"


def zoom_img(image):
    """Zooms in an image, and load it"""
    try:
        zoomed = image[100:500, 450:850]
        # grey : prend les 3 canaux RGB et converti en valeur grise
        grey = np.dot(zoomed[..., :3], [0.299, 0.587, 0.114])
        # res : permet de remettre le canal responsable du RGB
        res = grey[:, :, None]
        print(f"\nNew shape after slicing: {res.shape} or {res.squeeze().shape}")
        print(res)
        plt.imshow(res, cmap="grey", vmin=0, vmax=255)
        plt.show()

    except Exception as error:
        raise RuntimeError(f"{RED}failed to display image: {error}{RESET}")


def main():
    try:
        img = ft_load("../animal.jpeg")
        zoom_img(img)

    except KeyboardInterrupt:
        print(f"{RED}\nKeyboardInterrupt : signal catched{RESET}")
    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
