profit = float(input('Пожалуйста введите выручка организации '))
costs = float(input('Пожалуйста введите издержки организации '))
if profit > costs:
    print('Ваша организация работает в плюс')
    rent = (profit - costs) / profit
    print(f'Рентабельность вашей организации {rent}')
    people = input('Сколько человек работает в вашей организации? ')
    print(f'Прибыль фирмы на 1 сотрудника: {(profit - costs) / int(people)}')
else:
    print('Ваша организация работает в минус')
