# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

from random import randint

n = int(input('Сколько монеток лежит на столе?: '))
orel = 0
reshka = 0
for i in range(n):
    coin = randint(0, 1)
    print(coin, end=',')
    if coin == 0:
        orel += 1
    else:
        reshka += 1
if orel < reshka or orel == reshka:
    print(f'надо перевернуть {orel} монет с орла на решку ')
else:
    print(f'надо перевернуть {reshka} монет с решки на орла ')
