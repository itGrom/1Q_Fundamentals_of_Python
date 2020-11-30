'''
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class ClothesAbstract(ABC):
    @property
    @abstractmethod
    def textile_volume(self):
        pass

class Clothes(ClothesAbstract):
    __cnt = 0
    name = 'одежда'
    def __init__(self):
        __class__.__cnt += 1
        self.name = self.__class__.name
    @classmethod
    def cnt(cls):
        return __class__.__cnt


class Coat(Clothes):
    name = 'пальто'
    __cnt = 0
    def __init__(self, V):
        self.__class__.__cnt += 1
        self.__item = self.__class__.__cnt
        self.V = V
        super().__init__()
    @property
    def textile_volume(self):
        return self.V/6.5 + 0.5
    @classmethod
    def cnt(cls):
        return __class__.__cnt
    @property
    def item(self):
        return self.__item

class Suit(Clothes):
    name = 'костюм'
    __cnt = 0
    def __init__(self, H):
        self.__class__.__cnt += 1
        self.__item = self.__class__.__cnt
        self.H = H
        super().__init__()
    @property
    def textile_volume(self):
        return 2 * self.H + 0.3
    @classmethod
    def cnt(cls):
        return __class__.__cnt
    @property
    def item(self):
        return self.__item

suit1 = Suit(1.8)
suit2 = Suit(1.7)
suit3 = Suit(1.6)

print(f'{suit1.name.capitalize()} №{suit1.item}, рост {suit1.H}, расход ткани {suit1.textile_volume:.2f}')
print(f'{suit2.name.capitalize()} №{suit2.item}, рост {suit2.H}, расход ткани {suit2.textile_volume:.2f}')
print(f'{suit3.name.capitalize()} №{suit3.item}, рост {suit3.H}, расход ткани {suit3.textile_volume:.2f}')

print(f'Всего выпущено экземпляров {Suit.name.capitalize()}: {Suit.cnt()}')

coat1 = Coat(48)
coat2 = Coat(50)
coat3 = Coat(52)

print(f'{coat1.name.capitalize()} №{coat1.item}, размер {coat1.V}, расход ткани {coat1.textile_volume:.2f}')
print(f'{coat2.name.capitalize()} №{coat2.item}, размер {coat2.V}, расход ткани {coat2.textile_volume:.2f}')
print(f'{coat3.name.capitalize()} №{coat3.item}, размер {coat3.V}, расход ткани {coat3.textile_volume:.2f}')

print(f'Всего выпущено экземпляров {Coat.name.capitalize()}: {Coat.cnt()}')

print(f'Всего выпущено экземпляров {Clothes.name.capitalize()}: {Clothes.cnt()}')

textile = suit1.textile_volume + suit2.textile_volume + suit3.textile_volume + coat1.textile_volume + coat2.textile_volume + coat3.textile_volume
print(f'На выпуск всей {Clothes.name.capitalize()} понадобится ткани: {textile:.2f}')
