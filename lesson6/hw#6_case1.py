'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
'''Вариант 1'''
from time import sleep

class TrafficLight():
    __color=''

    def running(self):
        __color='красный'
        for i in range(7):
            print(__color)
            sleep(1)
        __color='желтый'

        for i in range(2):
            print(__color)
            sleep(1)
        __color='зеленый'

        for i in range(4):
            print(__color)
            sleep(1)

svetofor = TrafficLight()
print(svetofor.running())

'''Вариант 2'''
from time import sleep
from itertools import cycle, count
class TrafficLight():
    __color=['красный', 'желтый', 'зеленый']

    def running(self, count_cycle):
        color_duration = {'красный':7, 'желтый':2, 'зеленый':5}
        cnt_cycl = 0
        current_light=TrafficLight.__color[0]
        cnt = count(1)
        while cnt_cycl < count_cycle:
            for light in cycle(current_light):
                i=next(cnt)
                if i == (color_duration[TrafficLight.__color[0]] + 1):
                    current_light=TrafficLight.__color[1]
                elif i == color_duration[TrafficLight.__color[0]] + color_duration[TrafficLight.__color[1]] + 1:
                    current_light =TrafficLight.__color[2]
                elif i > color_duration[TrafficLight.__color[0]] + color_duration[TrafficLight.__color[1]] + color_duration[TrafficLight.__color[2]]:
                    cnt = count(1)
                    cnt_cycl += 1
                    current_light = TrafficLight.__color[0]
                    break
                print(current_light)
                sleep(1)

svetofor = TrafficLight()
svetofor.running(2)