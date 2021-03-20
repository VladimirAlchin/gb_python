"""Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка."""

with open('for_task01.txt', 'w') as my_file:
    while True:
        user_input = input('Что добавить в файл? ')
        if user_input:
            my_file.write(user_input + '\n')
        else:
            print('Всего доброго')
            break


