# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4
def number():
    x = int(input("Введите число a: "))
    y = int(input("Введите число b: "))
    try:
        x = int(x)
        y = int(y)
        assert x >= 0 and y >= 0, "Число должно быть положительным!"
        return x, y
    except (ZeroDivisionError, ValueError):
        print("Вы ввели некорректное число. Повторите ввод!")


def sum (x, y):
   if x == 0:
        return y
   elif y == 0:
       return x
   return sum(x+1, y-1)


x, y = number()
print(sum(x, y))
