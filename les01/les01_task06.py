start_run = float(input('Сколько километров вы пробежали в первый день? '))
end_run = float(input('Сколько километров вы хотите пробегать? '))
day = 1
while start_run < end_run:
    print(f'{day}-ый день:{round(start_run,2)}')
    start_run = start_run * 1.1
    day += 1
print(f'{day}-ый день:{round(start_run,2)}')

print(f'На {day}-й день спортсмен достиг результата - не менее {end_run} км')