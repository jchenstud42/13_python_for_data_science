import os
import imageio.v2 as iio

RED = "\033[91m"
RESET = "\033[0m"


def ft_load(path: str):
    """Loads img, prints its format, and its pixels content in RGB format"""
    assert os.path.exists(path), "file not found"
    # split l'extension du nom du fichier, et check l'extension ([1])
    ext = os.path.splitext(path)[1]
    assert ext in (".jpg", ".jpeg"), "only .jpg and .jpeg format allowed"

    try:
        img = iio.imread(path)

        # img : class 'numpy.ndarray', img[y, x] -> [R,G,B]
        print(f"The shape of image is: {img.shape}")
        print(img)

        return img

    except Exception as error:
        raise RuntimeError(f"{RED}failed to read image: {error}{RESET}")


def main():
    try:
        print(ft_load("../landscape.jpg"))

    except RuntimeError as error:
        print(f"{RED}Error: {error}{RESET}")
    except AssertionError as error:
        print(f"{RED}AssertionError: {error}{RESET}")


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
