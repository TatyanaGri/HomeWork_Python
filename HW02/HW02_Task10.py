# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# нужно перевернуть.

import random

flag = True
while flag:
    n = int(input("Введите количество монеток: "))
    if n >= 1:
        flag = False
    else:
        print("Вы ввели не верные данные. Повторите ввод")

zero = 0
one = 0
for i in range(n):

    coin = random.randint(0, 1)
    print(coin)

    if coin == 0:
        zero += 1
    else:
        one += 1
if zero < one:
    print("Перевернуть нужно", zero, 'монет')
else:
    print("Перевернуть нужно", one, 'монет')