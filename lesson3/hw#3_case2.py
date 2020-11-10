'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
'''

def person(first_name, last_name, year_of_birth, city, email, phone):
    return print(f'{first_name.capitalize()} {last_name.capitalize()}, {year_of_birth} года рождения, проживающий: г.{city.capitalize()}, email: {email}, телефон: {phone}')

person (first_name='иван', last_name='васильев', year_of_birth='1987', city='москва', email='vas@mail.ru', phone='+79161745689')
