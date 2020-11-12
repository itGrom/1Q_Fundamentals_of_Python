'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой.
Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''

'''Вариант 1'''

word = input('Введите строку на латинице: ')

def capital(string):
    for el in string.split():
        el=el.replace(el[0],chr(ord(el[0])-32))
        print(el, end=' ')

capital(word)

'''Вариант 2'''
string = input('Введите строку на латинице: ')

def capital(string):
    return print(string.title())

capital(string)

'''Вариант 3'''
string = input('Введите строку на латинице: ')

def capital(string):
    return ' '.join(map(lambda x: x.capitalize(), string.split()))

print(capital(string))
'''Вариант 4'''
string = input('Введите строку на латинице: ')
def capital(string):
    return ' '.join(map(lambda x: x.replace(x[0],chr(ord(x[0])-32)), string.split()))
print(capital(string))