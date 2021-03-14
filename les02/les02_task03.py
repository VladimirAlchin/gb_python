# dict
seasons_dict = {1: 'зима',
                2: 'зима',
                3: 'весна',
                4: 'весна',
                5: 'весна',
                6: 'лето',
                7: 'лето',
                8: 'лето',
                9: 'осень',
                10: 'осень',
                11: 'осень',
                12: 'зима'}
# list
month_tuple = ('зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима')

# input and result
user_month = int(input('Введите номер месяца: '))
while 0 > user_month or user_month > 12:
    print('Такого месяца нет, введите другой')
    user_month = int(input('Введите номер месяца: '))

print(f'Месяц {user_month} через словарь отноcится к {seasons_dict.get(user_month)}')
print(f'Месяц {user_month} через лист/кортеж отноcится к {month_tuple[user_month]}')
