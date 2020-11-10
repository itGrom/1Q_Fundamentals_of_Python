'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''
'''Вариант 1'''
def my_func(a, b, c):
    num_list = [a, b, c]
    num_list.sort()
    max_1, max_2 = num_list[1:]
    return max_1 + max_2

print(f"Сумма двух наибольших аргументов равна: {my_func(32, 18, 25)}")

'''Вариант 2'''
def my_func(a, b, c):
    num_list = [a, b, c]
    max_1 = num_list.pop(num_list.index(max(num_list)))
    max_2 = num_list.pop(num_list.index(max(num_list)))
    return max_1 + max_2

print(f"Сумма двух наибольших аргументов равна: {my_func('c', 'A', 'z')}")