def fibonacci(n: int) -> list[int]:
    """Функция возвращает список из n чисел Фибоначчи"""
    if n == 0:
        return []
    elif n == 1:
        return [0]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    try:
        n = input("Введите количество чисел Фибоначчи: ").strip()
        if not n:
            raise ValueError("Пустой ввод!")
        n = int(n)
        if n < 0:
            raise ValueError("Количество чисел не может быть отрицательным!")
        if n > 10_000:
            raise ValueError("Слишком большое число, выберите ≤ 10000")

        result = fibonacci(n)
        print("Последовательность Фибоначчи: ")
        print(*result, sep=", ")

    except ValueError as ve:
        print(f"Ошибка ввода: {ve}")
    except OverflowError:
        print("Ошибка: введено слишком большое число!")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
