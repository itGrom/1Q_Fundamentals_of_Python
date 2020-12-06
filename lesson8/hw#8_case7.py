'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''
class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return ComplexNum(self.a * other.a - self.b *other.b, self.a * other.b + self.b * other.a)
    def __str__(self):
        return f'{self.a} + {self.b}*i'

c1 = ComplexNum(2, 4)
c2 = ComplexNum(3, 6)

c3 = c1 + c2
c4 = c1 * c2
print(c1)
print(c2)
print(c3)
print(c4)
