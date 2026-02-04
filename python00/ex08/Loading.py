import os
from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """Creates our own progress bar"""
    total = len(lst)
    terminal_width = os.get_terminal_size().columns
    bar_width = terminal_width - 40

    for i, item in enumerate(lst, start=1):
        percent = int(i / total * 100)
        filled = int(bar_width * i / total)
        bar = "█" * filled + " " * (bar_width - filled)

        if i % 20 == 0 or i == total:
            print(f"\r{percent}%|{bar}| {i}/{total}", end="")
        # yield : cree un generateur, il ne renvoie pas un resultat final
        # mais un iterateur qu'on peut parcourir progressivement.
        # Chaque appel renvoie un elem, et met la fonction en pause
        yield item


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


# -------------------- FUNCTION CALL --------------------

if __name__ == "__main__":
    main()
