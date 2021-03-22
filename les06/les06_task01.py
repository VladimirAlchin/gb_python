"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
 Атрибут реализовать как приватный.
  В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
   Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
    третьего (зеленый) — на ваше усмотрение.
     Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
     Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep
import datetime
from itertools import cycle


class TrafficLight:
    def __init__(self):
        self.__color = ''


    def running(self):
        for self.__color in cycle(['red', 'yellow', 'green', 'yellow']):
            print(self.__color, datetime.datetime.now())
            if self.__color == 'green':
                sleep(7)
            elif self.__color == 'yellow':
                sleep(2)
            else:
                sleep(5)
    def get_color(self):
        return self.__color

a = TrafficLight()
a.running()
print(1)
