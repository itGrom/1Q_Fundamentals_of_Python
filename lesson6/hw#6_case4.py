'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('поехала')
    def stop(self):
        print('остановилась')
    def turn(self, direction):
        self.direction = direction
        print(f'повернула {direction}')
    def showspeed(self):
        print(self.speed)

class TownCar(Car):
    def showspeed(self):
        if self.speed > 60:
            print('Превышение скорости')
class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40:
            print('Превышение скорости')
class SportCar(Car):
    def afterburner(self):
        print('Форсаж включен')
        self.speed = self.speed * 2
class PoliceCar(Car):
    def siren(self):
        print('Кррр крр крр. Примите вправо!')

towncar = TownCar(61, 'black', 'Volvo')
workcar = WorkCar(48, 'gray', 'Lada')
sportcar = SportCar(90, 'yellow', 'Camaro')
police = PoliceCar(60, 'blue', 'Ford', True)

print(f'TownCar марка: {towncar.name}, скорость: {towncar.speed}, цвет:{towncar.color}, полиция:{towncar.is_police}')
print(f'WorkCar марка: {workcar.name}, скорость: {workcar.speed}, цвет:{workcar.color}, полиция:{workcar.is_police}')
print(f'SportCar марка: {sportcar.name}, скорость: {sportcar.speed}, цвет:{sportcar.color}, полиция:{sportcar.is_police}')
print(f'Police марка: {police.name}, скорость: {police.speed}, цвет:{police.color}, полиция:{police.is_police}')

towncar.go()
towncar.turn('направо')
towncar.showspeed()
towncar.stop()

sportcar.showspeed()
sportcar.afterburner()
sportcar.showspeed()

police.go()
police.turn('налево')
police.siren()

workcar.go()
workcar.showspeed()


