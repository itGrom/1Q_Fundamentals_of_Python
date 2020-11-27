'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
src_list=[]
map_dict={1:'Один', 2:'Два', 3:'Три', 4:'Четыре'}

with open('hw#5_case4_src.txt', 'r') as file:
    for line in file:
        src_list.append(line.split(' '))

with open('hw#5_case4_dest.txt', 'w') as file:
    for el in src_list:
        el[0]=map_dict[int(el[2])]
        file.write(' '.join(el))


