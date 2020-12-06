'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''
class Data:
    __date_char = ''
    def __init__(self, date_char):
        self.date_char = date_char
        __class__.__date_char = self.date_char

    @classmethod
    def to_int(cls):# здесь можно сделать необязательную переменную
        day, month, year = __date_char.split('-')
        return int(day), int(month), int(year)
    @staticmethod
    def validation(): # здесь можно сделать необязательную переменную
        day, month, year =__class__.__date_char.split('-')
        if int(year) <= 0:
            print('Вы ввели недопустимое значение года')
        elif not (int(month) in range(1, 13)):
            print('Вы ввели недопустимое значение месяца')
        elif not (int(day) in range(1, 32)):
            print('Вы ввели недопустимое значение дня')
        elif (int(day) == 31 and int(month) not in [1, 3, 5, 7, 8, 10, 12]) or (
                int(day) == 29 and int(month) == 2 and int(year) % 4 != 0) or (int(day) == 30 and int(month) == 2):
            print('Вы ввели недопустимое значение дня для данного месяца')
        else:
            print('Введена допустимая дата')

data = Data('12-11-2020')
print(data.to_int())
data.validation()

data = Data('29-02-2018')
print(data.to_int())
data.validation()