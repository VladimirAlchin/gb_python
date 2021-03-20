"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""
with open('for_task02', 'r', encoding='UTF-8') as read_file:
    for i, str_line in enumerate(read_file.readlines(), start=1):
        print(f'Слов в {i} строке {str_line.count(" ") + 1 if int(str_line.count(" ")) > 0 else 0}')
