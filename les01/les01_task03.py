number = input('Введите число для расчета суммы х+хх+ххх где х = ')
# вариант когда считаем по формуле задачи
print('вариант когда считаем по формуле задачи')
print(int(number * 3)+int(number * 2) + int(number))
ite_r = 1
summa = 0
print('вариант когда число это размерность и число n, например n=4 4+44+444+4444')
while ite_r < int(number) + 1:
    summa = summa + int(number * ite_r)
    ite_r = ite_r + 1
print(summa)