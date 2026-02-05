import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

RED = "\033[91m"
RESET = "\033[0m"


def zoom_img(image):
    try:
        zoomed = image[100:500, 450:850]
        # gray : prend les 3 canaux RGB et converti en valeur grise
        gray = np.dot(zoomed[..., :3], [0.299, 0.587, 0.114])
        # res : permet de remettre le canal responsable du RGB
        res = gray[:, :, None]
        print(f"New shape after slicing: {res.shape} or {res.squeeze().shape}")
        print(res)
        plt.imshow(res, cmap="gray", vmin=0, vmax=255)
        plt.show()

    except Exception as error:
        raise RuntimeError(f"{RED}failed to display image: {error}{RESET}")


def main():
    try:
        img = ft_load("../animal.jpeg")
        zoom_img(img)

    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
