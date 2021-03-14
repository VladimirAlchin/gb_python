"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

# global x,y
while True:
    x = int(input('Введите действительное положительное число '))
    if x in range(1, 10, 1):
        break
while True:
    y = int(input('Введите отрицательное число '))
    if y < 0:
        break


def my_func(x, y):
    print(f'1 / {x ** abs(y)} = {x ** y}')
    new_x = x
    for i in range(1, abs(y), 1):
        new_x = x * new_x
    print(f'1 / {new_x} = {1 / new_x}')


my_func(x, y)
