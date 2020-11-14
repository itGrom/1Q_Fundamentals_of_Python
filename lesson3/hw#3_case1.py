'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
while 1:
    try:
        a = float(input('Введите число "a": '))
        break
    except Exception as err:
        continue
while 1:
    try:
        b = float(input('Введите число "b": '))
        break
    except Exception as err:
        continue

def func(a, b):
    try:
        c = a / b
    except Exception as err:
        print (f'На ноль делить нельзя! Ошибка: {err}')
        return None
    return c

print(f'Результат деления чисел:{func(a, b)}')