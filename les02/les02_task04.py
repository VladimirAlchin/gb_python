user_input = input('Введите слова через пробел : ').split()
for s in user_input:
    print(s) if len(s) < 10 else print(s[0:10])
