"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
 Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
 Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""

people = []
mean_costs = []
with open('for_task03', 'r', encoding='UTF-8') as costs:
    for str_line in costs:
        a = str_line.replace('\n', '').split(' ')
        mean_costs.append(float(a[1]))
        if float(a[1]) > 20000:
            people.append(a[0])
print(f'Люди с зп выше 20 000: {people}')
print(f'Средняя зп: {sum(mean_costs) / len(mean_costs)}')

import numpy as np

print(f'Средняя зп: {np.mean(mean_costs)}')
