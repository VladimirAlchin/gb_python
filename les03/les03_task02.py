"""
2. Реализовать функцию, принимающую несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
  Реализовать вывод данных о пользователе одной строкой.
"""


def user_data(**kwargs):
    print(list(kwargs.keys()))
    print(kwargs.items())
    print(list(kwargs.values()))
    print(f'{kwargs.get("name")} {kwargs.get("lastname")} {kwargs.get("birthday")}'
          f'{kwargs.get("town")} {kwargs.get("email")} {kwargs.get("mobile")}')


user_data(
    name=input('Введите имя пользователя: '),
    lastname=input('Введите имя фамилию: '),
    birthday=input('Введите дату рождения: '),
    town=input('Введите город проживания: '),
    email=input('Введите email: '),
    mobile=input('Введите контактный телефон: ')
          )
