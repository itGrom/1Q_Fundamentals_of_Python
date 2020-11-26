'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, matrix=[]):
        self.matrix = matrix

    def __str__(self):
        string = ''
        for el in self.matrix:
            string += f'{" ".join([str(ch) for ch in el])}\n'
        return string

    def __add__(self, other):
        self_ext = self.matrix.copy()
        other_ext = other.matrix.copy()
        result = []
        delta_height = len(self_ext) - len(other_ext)
        delta_width = len(self_ext[0]) - len(other_ext[0])
        if delta_width > 0:
            for el in other_ext:
                for _ in range(delta_width):
                    el.append(0)
        elif delta_width < 0:
            for el in self_ext:
                for _ in range(abs(delta_width)):
                    el.append(0)

        if delta_height > 0:
            for _ in range(delta_height):
                other_ext.append([el*0 for el in range(len(other_ext[0]))])
        elif delta_height < 0:
            for _ in range(abs(delta_height)):
                self_ext.append([el*0 for el in range(len(self_ext[0]))])
        mtx_height = len(self_ext)
        mtx_width = len(self_ext[0])
        line = []
        for h in range(mtx_height):
            for w in range(mtx_width):
                line.append(self_ext[h][w] + other_ext[h][w])
            result.append(line.copy())
            line.clear()
        return Matrix(result)


m1 = Matrix([[2,3,4],[1,5,6],[8,4,3]])
m2 = Matrix([[2,3],[1,6],[4,3],[3,6]])

print(m1)
print(m2)

m3 = m1 + m2

print(m3)
