# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

from random import randint

n = int(input("Введите количесвто элементов массива: "))

list_start = [randint(-20, 20) for _ in range(n)]
print(*list_start)

min = int(input("Введите минимум диапазона для поиска: "))
max = int(input("Введите максимум диапазона для поиска: "))

for i in range(len(list_start)):
    if min <= list_start[i] <= max:
        print(i, end=' ')

