'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''
my_list = [7, 5, 3, 3, 2]

print(f'Исходный рейтинг: {my_list}')

while len(my_list) < 15: #ограничение работы цикла до 15 элементов в рейтинге (можно сделать запрашиваемый размер рейтинга)
    el = int(input('Введите очередной элемент рейтинга: '))
    if my_list.count(el) >= 1: #если значение нового элемента рейтинга уже есть
        my_list.insert(my_list.index(el) + my_list.count(el), el) #то вычисляем индекс первого существующего значения и к нему прибавляем их число, чтобы на этом месте вставить новый элемент
    else:
       for i in range(len(my_list)):#если элемента нет, то пробегаем список, сравнивая значения
           if el > my_list[i]: #сравниваем новый элемент с текущим, если новый больше, то ставим его на место текущего, т.к. у нас убывающий список
               my_list.insert(i,el)
               break
           elif el < my_list[i] and i == len(my_list) - 1: #если новый меньше текущего и текущий есть последний, то добавляем в конец списка
               my_list.append(el)
               break

    print(f'Новый рейтинг: {my_list}')

'''
Вариант 2
my_list = [7, 5, 3, 3, 2]

print(f'Исходный рейтинг: {my_list}')

while len(my_list) < 15:
    el = int(input('Введите очередной элемент рейтинга: '))
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            my_list.append(el)
            break
        elif el > my_list[i]:
            my_list.insert(i,el)
            break
        elif el == my_list[i] and el > my_list[i+1]:
            my_list.insert(i+1, el)
            print(my_list[i+1])
            break

    print(f'Новый рейтинг: {my_list}')
'''