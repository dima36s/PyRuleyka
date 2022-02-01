from random import *

print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    if 0 < int(num) < 101:
        return True
    else:
        return False


def max_range():
    while True:
        n = input('Введите максимальное число: ')
        if not n.isdigit() or int(n) < 1:
            print('Введите целое число больше нуля!')
            continue
        return int(n)


border = max_range()
secret = randint(1, border)


def get_num():
    while True:
        n = input(f'Введите число от 1 до {border}: ')
        if not n.isdigit() or not (1 <= int(n) <= border):
            print(f'Введите число от 1 до {border}: ')
            continue
        return int(n)


def game():
    x, total = 0, 1
    while x != secret:
        x = get_num()
        if x > secret:
            print('Ваше число больше загаданного, попробуйте ещё раз')
            total += 1
        elif x < secret:
            print('Ваше число меньше загаданного, попробуйте ещё раз')
            total += 1
            continue
    print('Вы угадали, поздравляем!')
    print('Количество попыток: ' + str(total))


while True:
    game()
    print('Отличная игра, ещё разок?')
    answer = input('Да(Д) или Yes(Y), если желаете продолжить: ')
    if answer.lower() in ('д', 'да', 'yes', 'y'):
        border = max_range()
        secret = randint(1, border)
        continue
    else:
        break

print('Спасибо, что играли в числовую угадайку. Ждем вас снова!')
