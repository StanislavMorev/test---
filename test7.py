import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def __str__(self):
        return f"Прямоугольник (длина: {self.length}, ширина: {self.width})"


class Square:
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return f"Квадрат (сторона: {self.side})"


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Окружность (радиус: {self.radius})"


class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self):
        return f"Треугольник (стороны: {self.side1}, {self.side2}, {self.side3})"

# Пример списка фигур
figures = [
    Rectangle(5, 3),
    Square(4),
    Circle(2),
    Triangle(3, 4, 5),
    Rectangle(10, 2),
    Square(7),
    Circle(5),
    Triangle(6, 8, 10),
]

# Перебор и вывод периметров
for figure in figures:
    print(f"{figure}: Периметр = {figure.perimeter():.2f}")
