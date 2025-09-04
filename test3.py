def generate_spiral(n):
    matrix = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n - 1, 0, n - 1

    while left <= right and top <= bottom:
        # верхняя строка слева направо
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        #  правый столбец сверху вниз
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # нижняя строка справа налево
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        # левый столбец снизу вверх
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    # Выводим матрицу
    for row in matrix:
        print(' '.join(f'{x:2d}' for x in row))


result = int(input(f'Введите число: '))
generate_spiral(result)