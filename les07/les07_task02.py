"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы
для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.cloth = int(size)

    @abstractmethod
    def my_method_1(self):
        pass


class Coat(Clothes):
    def my_method_1(self):
        return round(self.cloth / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def my_method_1(self):
        return self.cloth * 2 + 0.3


coat1 = Coat(10)
coat2 = Coat(20)
costum1 = Costume(10)
costum2 = Costume(20)

print(
    coat1.my_method_1(),
    coat2.my_method_1(),
    costum1.my_method_1,
    costum2.my_method_1
)
print(
    coat1.my_method_1() +
    coat2.my_method_1() +
    costum1.my_method_1 +
    costum2.my_method_1
)
