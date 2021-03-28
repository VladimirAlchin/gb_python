"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

dict_trans = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('for_task04', 'r', encoding='UTF-8') as dict_file:
    with open('for_task04_result', 'w', encoding='UTF-8') as result_file:
        for dict_line in dict_file:
            result_file.write(dict_trans.get(dict_line.split(' — ')[0]) + ' — ' + dict_line.split(' — ')[1])