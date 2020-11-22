'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''

'''6.a вариант 1'''
from itertools import count

def iter(num):
    for el in count(num):
        if el > 10:
            break
        yield el

for i in iter(3):
    print(i)

'''6.а вариант 2'''

from itertools import count

def iter(start, stop=10):
    while start <= stop:
        yield start
        start += 1

for i in iter(3):
    print(i)

'''6.б вариант 1 в переменной stop указывается сколько раз элементов надо вывести'''

from itertools import cycle

def my_repeat(my_list, stop=10):
    i = 0
    for el in cycle(my_list):
        i += 1
        if i > stop:
            break
        yield el

my_list = [3, 7, 9]

for el in my_repeat(my_list, 3):
    print(el)

'''6.б вариант 2 в переменной cnt_list указывается число повторения всего списка'''
from itertools import cycle

def my_repeat(my_list, cnt_list=10):
    i = 0
    for el in cycle(my_list):
        yield el
        i += 1
        if i / len(my_list) == cnt_list:
            break

my_list = [3, 7, 9]

for el in my_repeat(my_list, 3):
    print(el)
