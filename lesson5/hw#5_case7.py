'''
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
import json
profit_sum = 0
profit_cnt = 0
result_dict={}
result_list=[]
with open('hw#5_case7.txt','r', encoding='utf-8') as file:
    for line in file:
        lst = line.split(' ')
        result_dict[lst[0]] = float(lst[2]) - float(lst[3])
        if float(lst[2]) - float(lst[3]) > 0:
            profit_cnt += 1
            profit_sum += float(lst[2]) - float(lst[3])
    result_list.append(result_dict)
    result_list.append({'average_profit':profit_sum/profit_cnt})
print(result_list)

with open('hw#5_case7.json', 'w') as file:
    json.dump(result_list, file)


