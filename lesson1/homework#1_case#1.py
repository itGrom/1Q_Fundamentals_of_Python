'''
case 1
Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

number_a = int (input('Введите число a: '))
number_b = int (input('Введите число b: '))
sum = number_a + number_b
print(f'Сумма чисел "{number_a}" и "{number_b}" равна: {sum}')

user_name = input('Введите ваше имя: ')

text_count = int(input(f'{user_name.capitalize()}, сколько раз Вы хотели бы поприветствовать себя: '))

user_text = f'Привет, {user_name.capitalize()}!\n'

print(user_text * text_count)


