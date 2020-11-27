'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''

class Worker():
    _income = {'wage': 20000, 'bonus': 40}
    def __init__(self, name, surname, position):
        self.name=name
        self.surname=surname
        self.position=position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self._income = super()._income

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['wage'] * self._income['bonus'] / 100

ivanov = Position('Сергей', 'Иванов', 'Менеджер')
print(ivanov.name)
print(ivanov.surname)
print(ivanov.position)

print(ivanov.get_full_name())
print(ivanov.get_total_income())