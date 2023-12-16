import math

# Базовый класс для геометрических фигур
class Figure:
    def calculateArea(self):
        pass

    def calculatePerimeter(self):
        pass

# Класс Круг
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculateArea(self):
        return math.pi * self.radius**2

    def calculatePerimeter(self):
        return 2 * math.pi * self.radius

# Класс Прямоугольник
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculateArea(self):
        return self.length * self.width

    def calculatePerimeter(self):
        return 2 * (self.length + self.width)

# Класс Квадрат
class Square(Rectangle):
    def __init__(self, side):
        # Квадрат является подклассом прямоугольника
        super().__init__(side, side)

    # Переопределение методов calculateArea и calculatePerimeter
    def calculateArea(self):
        return self.length**2

    def calculatePerimeter(self):
        return 4 * self.length


circle = Circle(6)
print(f"Площадь круга: {circle.calculateArea()}")
print(f"Периметр круга: {circle.calculatePerimeter()}")

rectangle = Rectangle(4, 2)
print(f"Площадь прямоугольника: {rectangle.calculateArea()}")
print(f"Периметр прямоугольника: {rectangle.calculatePerimeter()}")

square = Square(4)
print(f"Площадь квадрата: {square.calculateArea()}")
print(f"Периметр квадрата: {square.calculatePerimeter()}")
