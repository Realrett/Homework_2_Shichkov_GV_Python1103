# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint
number_of_coins = int(input('Введите число монет на столе: '))
avers = 0
revers = 0
while number_of_coins <= 0:
    number_of_coins = int(input('Введите число монет на столе: '))
coins = []
for i in range (number_of_coins):
    coins.append(randint(0, 1))
for i in coins:
    if i > 0:
        avers += 1
    else:
        revers += 1
coup = min(avers, revers)
print(f"Выпало {avers} монет орлом вверх и {revers} монет решкой вверх. Необходимо перевернуть {coup} монет ")