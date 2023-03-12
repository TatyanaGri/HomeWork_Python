#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

#*Пример:*

#3 2 4 -> yes
#3 2 1 -> no

n = int(input("Введите количество долек n: "))
m = int(input("Введите количество долек m: "))

flag = True
while flag:
    k = int(input("Введите количество отломанных долек k: "))
    if k < m * n:
        flag = False
    else:
        print("Отломить невозможно, введенное количество долек превышает допустимую площадь.")

if k % m == 0 or k % n == 0:
    print("YES")
else:
    print("NO")