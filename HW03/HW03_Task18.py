# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# Пример:
# 5    1 2 3 4 5
# 6    -> 5

from random import randint


def number_n():
    n = input("Введите длинну массива: ")
    try:
        n = int(n)
        return n
    except (ZeroDivisionError, ValueError):
        print("Вы ввели неверные данные. Повторите ввод!")


def array():
    a = []
    for i in range(n):
        a.append(randint(1, n))
    return a


def number_x():
    x = input("Введите число для сравнения: ")
    try:
        x = int(x)
        return x
    except (ZeroDivisionError, ValueError):
        print("Вы ввели некорректное число. Повторите ввод!")


n = number_n()
arr = array()
print(*arr)
x = number_x()

count = 0
number_i = 0
flag = True
while number_i == 0:
    i = 0
    while i<n and flag:
        if abs(x-arr[i]) == count:
            number_i = arr[i]
            flag = False
        i += 1
    count += 1

print(f"Число {number_i} в массиве наиболее близко к величине {x}")
