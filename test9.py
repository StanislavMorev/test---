import random

def create_deck():
    # Масти
    suits = ["♠", "♥", "♦", "♣"]
    # Карты (от 6 до туза)
    ranks = ["6", "7", "8", "9", "10", "Валет", "Дама", "Король", "Туз"]


    deck = [f"{rank} {suit}" for suit in suits for rank in ranks]
    return deck


def main():
    deck = create_deck()
    print("Исходная колода:")
    print(deck)

    random.shuffle(deck)

    print("\nПеремешанная колода:")
    print(deck)


if __name__ == "__main__":
    main()
