def max_diagonals_in_polygon(n):
    try:

        if not isinstance(n, int):
            raise ValueError("Количество углов должно быть целым числом.")


        if n < 3:
            raise ValueError("Многоугольник должен иметь не менее 3 углов.")


        max_diagonals = 0.5 * n * (n - 3)

        if not max_diagonals.is_integer():
            raise ValueError("Ошибка: результат не является целым числом.")

        return int(max_diagonals)

    except ValueError as e:
        print(f"Ошибка: {e}")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None


print(max_diagonals_in_polygon(5))
print(max_diagonals_in_polygon(6))

