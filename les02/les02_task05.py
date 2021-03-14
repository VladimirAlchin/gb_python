my_list = [7, 5, 3, 3, 2]

# user_number = int(input('Введите целое число для добавления в рейтинг,'
#                         ' если захотите выйти отправьте пустое значение: '))

while True:
    user_number = input('Введите целое число для добавления в рейтинг,'
                            ' если захотите выйти отправьте пустое значение: ')
    if str(user_number) != '':
        user_number = int(user_number)
        if user_number in my_list:
            my_list.insert(my_list.index(user_number)+my_list.count(user_number), user_number)
        else:
            if min(my_list) > user_number:
                my_list.append(user_number)
            elif max(my_list) < user_number:
                my_list.insert(0, user_number)
            elif max(my_list) > user_number:
                for i in reversed(my_list):
                    if user_number < int(i):
                        my_list.insert(my_list.index(i) + my_list.count(i), user_number)
                        break
    else:
        break
print('Всего доброго')
print(my_list)


