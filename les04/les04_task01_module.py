"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
 заработной платы сотрудника. В расчете необходимо использовать формулу:
 (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
  значений необходимо запускать скрипт с параметрами.
"""
import sys
"""bonus - процент от общей суммы"""
print('передаваемые параметры часы, ставка, процент премии')
hours, price, bonus = sys.argv[1:]
cost = float(hours)*float(price)
print(cost+cost*(float(bonus)/100))



