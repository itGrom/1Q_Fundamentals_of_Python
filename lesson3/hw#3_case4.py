'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''

'''Вариант 1'''
def neg_power(x, y):
    try:
        x=float(abs(x))
    except Exception as err:
        return print(f'Неверный первый аргумент! Ожидается число. Error: {err}')
    try:
        y = int(y)
        if y > 0:
            y = -y
    except Exception as err:
        return print(f'Неверный второй аргумент! Ожидается число. Error: {err}')
    return x ** y

print(neg_power(2, -3))

'''Вариант 2'''
def neg_power(x, y):
    result = 1
    try:
        x=float(abs(x))
    except Exception as err:
        return print(f'Неверный первый аргумент! Ожидается число. Error: {err}')
    try:
        y = int(y)
        if y > 0:
            y = -y
    except Exception as err:
        return print(f'Неверный второй аргумент! Ожидается число. Error: {err}')

    for i in range (abs(y)):
        result *= 1 / x

    return result

print(neg_power(2, -10))
