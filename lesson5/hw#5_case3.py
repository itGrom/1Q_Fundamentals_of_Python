'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
'''Вариант 1'''
with open('hw#5_case3.txt','r') as file:
    content_dict = {}
    sum = 0
    cnt = 0

    for line in file:
        key, value = line.encode('cp1251').decode('utf-8').split(' ')
        content_dict[key] = float(value)
        sum += float(value)
        cnt += 1

    print(f'Средний доход сотрудников равен {sum / cnt}')
    print(f'Оклад менее 20 тыс. имеют сотрудники:')
    for key, value in content_dict.items():
        if value < 20000:
            print(key)
'''Вариант 2'''
with open('hw#5_case3.txt','r') as file:
    sum = 0
    cnt = 0
    print(f'Оклад менее 20 тыс. имеют сотрудники:')
    for line in file:
        key, value = line.encode('cp1251').decode('utf-8').split(' ')
        sum += float(value)
        cnt += 1
        if float(value) < 20000:
            print(key)

    print(f'Средний доход сотрудников равен {sum / cnt}')

