# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

def number ():
    n = input("Введите число: ")
    try:
        n = int(n)
        return n
    except (ZeroDivisionError, ValueError):
        print("Вы ввели некорректное число. Повторите ввод!")

def sqrt ():
    power = 1
    while power <= n:
        print(power, end = ' ')
        power *= 2

n = number()
sqrt()
