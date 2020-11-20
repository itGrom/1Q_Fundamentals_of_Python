'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
'''Вариант 1'''
content_dict = {}

with open('hw#5_case2.txt', 'r') as file:
    n = 1
    for line in file:
        content_dict[f'{n} строка']=f'{len(line.split(" "))} слов'
        n += 1

print(f'Строк в файле {len(content_dict)}')

for a, b in content_dict.items():
    print(a, b)

'''Вариант 2'''
content = []

with open('hw#5_case2.txt', 'r') as file:
    content = file.readlines()

print(f'Строк в файле {len(content)}')

for el in content:
    print(f'В {content.index(el)+1} строке {len(el.split(" "))} слов')