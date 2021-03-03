second = int(input('Введите количество секунд для перевода в чч:мм:сс '))
hour = second // 3600
minute = (second % 3600) // 60
second = (second % 3600) % 60
if hour < 10:
    hour = "0" + str(hour)
if minute < 10:
    minute = "0" + str(minute)
if second < 10:
    second = "0" + str(second)
print(f'H M S {hour}:{minute}:{second}')
