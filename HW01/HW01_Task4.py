#Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

#*Пример:*

#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

s = int(input("Введите общее количество журавликов: "))

pet = round(s / 6)
print(f"Петя сделал {pet} журавликов.")

ser = round(pet)
print(f"Сережа сделал {ser} журавликов.")

kat = round((pet + ser) * 2)
print(f"Катя сделала {kat} журавликов.")