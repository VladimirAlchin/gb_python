"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.card = list(self.__card())
        self.fine = 0

    def __str__(self):
        a = f'----- Карточка {self.name} -----\n'
        for i in range(len(self.card)):
            for j in range(len(self.card[i])):
                a = a + str(self.card[i][j])
                if len(str(self.card[i][j])) == 1:
                    a = a + '  '
                else:
                    a = a + ' '
            a = a + '\n'
        a = a + '---------------------------\n'
        return str(a)

    def __card(self):
        player_card = []
        number = list(range(1, 91))
        for i in range(1, 4):
            a = []
            for j in range(5):
                del_number = random.randint(0, len(number) - 1)
                a.append(number[del_number])
                del number[del_number]
            a.sort()
            for j in range(4):
                a.insert(random.randint(0, len(a)), ' ')
            player_card.append(a)
        return player_card

    def __getitem__(self, item):
        return self.card[item]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.move = list(range(1, 91))

    def move(self):
        while len(self.move) > 75:
            print(self.p1)
            print(self.p2)
            del_number = random.randint(0, len(self.move) - 1)
            user_ans = input(f'Выпало число: {self.move[del_number]}\nЗачеркнуть цифру? y/n ')
            for i in range(0, 3):
                try:
                    del_player_number = self.p1[i].index(self.move[del_number])
                    self.p1[i][del_player_number] = '--'
                    break
                except ValueError:
                    del_player_number = -1
            del self.move[del_player_number]
            if (user_ans == 'y' and del_player_number == -1) or (user_ans == 'n' and del_player_number > -1):
                print('Вы проиграли, приходите еще!')
                exit()


player01 = Player('Vova')
player02 = Player('PC')
play = Game(player01, player02)
play.move()
