list_tuple = list()
i = 1
# for test
# list_tuple = ((1, {'навание': '1', 'стоимость': 2.0, 'количество': 3.0, 'ед': '4'}),
#               (2, {'навание': '2', 'стоимость': 4.0, 'количество': 5.0, 'ед': '4'}))
while True:
    name = input('Введите наименование товара: ')
    if name == '':
        break
    price = float(input('Введите стоимость товара: '))
    count = float(input('Введите количестово товара: '))
    unit = input('Введите единицу измерения товара: ')
    my_dict = tuple([i, {'навание': name, 'стоимость': price, 'количество': count, 'ед': unit}])
    list_tuple.append(my_dict)
    i += 1
for i in list_tuple:
    print(i)

name_list = list()
price_list = list()
count_list = list()
unit_list = set()

for i in list_tuple:
    list_values = list(i[1].values())
    name_list.append(list_values[0])
    price_list.append(list_values[1])
    count_list.append(list_values[2])
    unit_list.add(list_values[3])
result_list = {'навание': name_list, 'стоимость': price_list, 'количество': count_list, 'ед': unit_list}

for i in result_list.items():
    print(i)
