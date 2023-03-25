# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# Пример:
# 5    1 2 3 4 5
# 3    -> 1

from random import randint


def number_n():
    n = input("Введите длинну массива: ")
    try:
        n = abs(int(n))
        return n
    except (ZeroDivisionError, ValueError):
        print("Вы ввели неверные данные. Повторите ввод!")


def array():
    a = []
    for i in range(n):
        a.append(randint(1, n))
    return a


def number_x():
    x = input("Введите число которое нужно найти и посчитать: ")
    try:
        x = abs(int(x))
        return x
    except (ZeroDivisionError, ValueError):
        print("Вы ввели неверные данные. Повторите ввод!")


n = number_n()
arr = array()
print(*arr)
x = number_x()

i = 0
count_x = 0
while i < len(arr):
    if arr[i] == x:
        count_x = count_x + 1
    i = i + 1

print(f"Число {x} в массиве встречается {count_x} раз")
