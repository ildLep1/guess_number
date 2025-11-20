from random import randint

print('Угадай число от 1 до 100!')
number = randint(1, 100)

while True:
    users_try = int(input('Введите число: '))
    if number > users_try:
        print('Ваше число меньше того, что загадано.')
    elif number < users_try:
        print('Ваше число больше того, что загадано.')
    elif users_try == number:
        break

print('Отличная интуиция! Вы угадали число :)')