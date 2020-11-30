'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
'''
class Cell:
    def __init__(self, cell_num):
        self.cell_num = cell_num
    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)
    def __sub__(self, other):
        if self.cell_num - other.cell_num  <= 0:
            print('Вычитание клеток невозможно')
        else:
            return Cell(self.cell_num - other.cell_num)
    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)
    def __truediv__(self, other):
        return Cell(self.cell_num // other.cell_num)

    def make_order(self, cnt):
        cell_str = ''
        while self.cell_num > 0:
            cell_str += f'{"".join(["*" for _ in range(cnt if self.cell_num > cnt else self.cell_num)])}\n'
            self.cell_num -= cnt
        return cell_str

cell_1 = Cell(18)
cell_2 = Cell(6)
cell_3 = cell_1 * cell_2
cell_4 = cell_1 / cell_2
cell_5 = cell_1 + cell_2

print(cell_3.make_order(5))
print(cell_4.make_order(2))
print(cell_5.make_order(5))


