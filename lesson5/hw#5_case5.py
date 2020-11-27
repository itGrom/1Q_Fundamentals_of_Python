'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import random
from functools import reduce

with open('hw#5_case5.txt', 'w+') as file:
    #для генерации значений float можно использовать что-то типа el/random()*100
    file.write(' '.join([str(el) for el in range(int(random()*(10-1)+1),int(random()*(5000-500)+500), int(random()*(50-10)+10))]))

with open('hw#5_case5.txt', 'r') as file:
    file_sum = reduce(lambda x,y:float(x) + float(y), file.readline().split(' '))
print(f'Сумма чисел в файле = {file_sum:.2f}')


