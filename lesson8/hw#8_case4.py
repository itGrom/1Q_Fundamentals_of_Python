'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
'''

from abc import ABC, abstractmethod
class Store:
    __store_cnt = 0 #кол-во созданных складов
    type = 'store'
    def __init__(self, capacity, name):
        __class__.__store_cnt += 1
        self.capacity = capacity # емкость склада
        self.name = name # название склада
        self.__store_num = __class__.__store_cnt # номер склада
        self.__dev_reference = {} # справка по наличию оборудования на складе: общее кол-во и по категориям
        self.__store_eq = {} # хранящееся оборудование на складе по категориям
        self.__dep_eq = {}# выданное оборудование в определенные департаменты
        self.__dev_reference['all_device'] = 0

    def recieve(self, *devices):
        for dev in devices:
            if self.__dev_reference['all_device'] < self.capacity:
                self.__dev_reference['all_device'] += 1
                if dev not in self.__dev_reference.keys():
                    self.__dev_reference[dev.type] = 1
                else:
                    self.__dev_reference[dev.type] += 1
                if dev not in self.__store_eq.keys():
                    self.__store_eq[dev.type] = [dev]
                else:
                    self.__store_eq[dev.type].append(dev)
            else:
                raise ErrMethod(f'На складе нет места для нового оборудования')


    def send(self, dep, *devices):
        if dep not in self.__dep_eq.keys():
            self.__dep_eq[dep]=[]
        for dev in devices:
            if self.__dev_reference['all_device'] == 0:
                raise ErrMethod(f'На складе не осталось оборудования')
            else:
                if dev not in self.__store_eq[dev.type]:
                    raise ErrMethod(f'Оборудования {dev.type} {dev.brand} {dev.model} {dev.sn} нет на складе')
                else:
                    self.__dev_reference['all_device'] -= 1
                    self.__dev_reference[dev.type] -= 1
                    self.__dep_eq[dep].append(dev)
                    self.__store_eq[dev.type].remove(dev)
    @property
    def dev_reference(self):
        return self.__dev_reference
    @property
    def store_eq(self):
        return self.__store_eq
    @property
    def dep_eq(self):
        return self.__dep_eq

class OfficeEq:
    type = 'office_equipment'
    __dev_cnt = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        __class__.__dev_cnt += 1
    @abstractmethod
    def print(self, txt):
        pass
    @abstractmethod
    def scan(self, txt):
        pass
    @classmethod
    def dev_cnt(cls):
        return cls.__dev_cnt



class Printer(OfficeEq):
    type = 'printer'
    __dev_cnt = 0
    glb_type = OfficeEq.type
    def __init__(self, brand, model):
        self.__class__.__dev_cnt += 1
        self.sn = f'{__class__.type}#{__class__.__dev_cnt:05}'
        super().__init__(brand, model)
    def print(self, txt):
        print(f'Вывод на печать\n{txt}')
    def scan(self, txt):
        raise ErrMethod('Метод не поддерживается данным типом оборудования')
    @property
    def dev_cnt(cls):
        return cls.__dev_cnt



class Scaner(OfficeEq):
    type = 'scaner'
    __dev_cnt = 0
    glb_type = OfficeEq.type

    def __init__(self, brand, model):
        self.__class__.__dev_cnt += 1
        self.sn = f'{__class__.type}#{__class__.__dev_cnt:05}'
        self.scan_txt = ''
        super().__init__(brand, model)
    def print(self, txt):
        raise ErrMethod('Метод не поддерживается данным типом оборудования')
    def scan(self, txt):
        self.scan_txt = txt
        print(f'Документ отсканирован')
    @property
    def dev_cnt(cls):
        return cls.__dev_cnt


class Copier(OfficeEq):
    type = 'copier'
    __dev_cnt = 0
    glb_type = OfficeEq.type

    def __init__(self, brand, model):
        self.__class__.__dev_cnt += 1
        self.sn = f'{__class__.type}#{__class__.__dev_cnt:05}'
        self.scan_txt = ''
        self.print_txt = ''
        super().__init__(brand, model)
    def print(self, txt):
        self.print_txt = txt
    def scan(self, txt):
        self.scan_txt = txt
    def copy(self, txt):
        self.scan(txt)
        self.print(txt)
    @property
    def dev_cnt(cls):
        return cls.__dev_cnt

class ErrMethod(Exception):
    def __init__(self, txt):
        self.txt = txt

p1 = Printer('HP', 'LaserJet')
c1 = Copier('Xerox', 'X1234')
s1 = Scaner('Canon', 'CN2345')

store1 = Store(100, 'Central')
print(f'Создан склад "{store1.name}" вместимостью {store1.capacity}\n')

store1.recieve(p1,c1,s1)
print(f'На склад принято оборудование:\n{p1.type}: {p1.brand} {p1.model} {p1.sn}\n{c1.type}: {c1.brand} {c1.model} {c1.sn}\n{s1.type}: {s1.brand} {s1.model} {s1.sn}\n')

print(f'Справка по складу: {store1.dev_reference}\n')
print(f'Фактически в наличии следующее оборудование: {store1.store_eq}\n')
print(f'Оборудование выдано в подразделения: {store1.dep_eq}\n')

store1.send('it_dept', s1)
print(f'После выдачи оборудования в подразделение\n')
print(f'Справка по складу: {store1.dev_reference}\n')
print(f'Фактически в наличии следующее оборудование: {store1.store_eq}\n')
print(f'Оборудование выдано в подразделения: {store1.dep_eq}\n')

print(f'Всего создано оборудования {OfficeEq.dev_cnt()}')

p1.print('sdfasfas')