number = int(input('Введите целое положительное число '))
while number < 0:
    number = int(input('Введите целое положительное число '))
max_number = number % 10
while number > 1:
    if max_number < number % 10:
        max_number = number % 10
    else:
        number = number // 10

print(f'Максимальная цифра в числе: {max_number}')
