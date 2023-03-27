# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def number ():
    x = input("Введите число a: ")
    y = input("Введите число b: ")
    try:
        x = int(x)
        y = int(y)
        return x, y
    except (ZeroDivisionError, ValueError):
        print("Вы ввели некорректное число. Повторите ввод!")


def degree(x, y):
    if y == 1:
        return x
    if y == 0:
        return 1
    else:
        return (x * degree(x, y-1))


x, y = number()
print("Результат возведения в степень равен:",degree(x, y))