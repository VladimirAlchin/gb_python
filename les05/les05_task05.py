"""
Создать (программно) текстовый файл, записать
в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""

with open('for_task05', 'w', encoding='UTF-8') as numbers:
    numbers.write('1 2 3 4')

with open('for_task05', 'r', encoding='UTF-8') as numbers:
    print(sum(map(int, numbers.readline().split())))