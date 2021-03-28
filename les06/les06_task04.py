"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.speed

    def go(self):
        return 'Автомобиль поехал'

    def stop(self):
        return 'Автомобиль остановился'

    def turn(self, direction):
        return f'Автомобиль повернул на {direction}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость! Текущая скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self.speed < 100:
            return f'Педаль газа нажми! Текущая скорость {self.speed}'
        else:
            return f'Не предел: {self.speed}'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость! Текущая скорость {self.speed}'
        else:
            return f'Ваша скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car = Car(1001, 'green', 'vaz')
work_car = WorkCar(60, 'red', 'kamaz')
town_car = TownCar(45, 'black', 'kia')
sport_car = SportCar(50, 'blue', 'ducati')
police_car = PoliceCar(100, 'white', 'ford')

print(car.go())
print(car.stop())
print(car.turn('лево'))
print(f'Скорость вашего автомобиля {car.show_speed()}')

print(work_car.show_speed())
print(town_car.show_speed())
print(sport_car.show_speed())
print(police_car.show_speed())


