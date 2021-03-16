"""
3. Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
"""


def my_func(num1, num2, num3):
    if num1 == num2 == num3:
        print('вы ввели одинаковые значения')
    elif num1 > num2 and num1 > num3:
        if num2 > num3:
            return num1+num2
        else:
            return num1+num3
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            return num1+num2
        else:
            return num2+num3
    else:
        if num1 > num2:
            return num1+num3
        else:
            return num2+num3


print(my_func(10, 30, 10))
