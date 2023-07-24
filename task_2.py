class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exists_triangle(self):
        return self.a + self.b > self.c and self.b + self.c > self.a and self.c + self.a > self.b

    def get_triangle_type(self):
        if not self.exists_triangle():
            return "Треугольник с такими сторонами не существует."

        if self.a == self.b == self.c:
            return "Равносторонний треугольник."
        elif self.a == self.b or self.b == self.c or self.c == self.a:
            return "Равнобедренный треугольник."
        else:
            return "Разносторонний треугольник."

triangle1 = TriangleChecker(3, 4, 5)
print(triangle1.exists_triangle())
print(triangle1.get_triangle_type())  # Разносторонний треугольник

triangle2 = TriangleChecker(5, 5, 5)
print(triangle2.exists_triangle())
print(triangle2.get_triangle_type())  # Равносторонний треугольник

triangle3 = TriangleChecker(2, 3, 10)
print(triangle3.exists_triangle())  
print(triangle3.get_triangle_type())  # Треугольник с такими сторонами не существует.
