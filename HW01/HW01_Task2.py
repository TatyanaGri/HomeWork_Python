#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

flag = True
while flag:
    x = int(input("Введите трехзначное число: "))
    if 100 < x < 1000:
        flag = False
    else:
        print("Вы ввели не трехзначное число")

sum = 0

while (x != 0):
    dig = x % 10
    sum = sum + dig
    x = x // 10
print(f"Сумма цифр числа равна: {sum}")