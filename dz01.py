# Задача 2. Напишите программу, которая будет на вход принимать число
#  N и выводить числа от -N до N

a = int (input("Задайте число:  "))

listA = list(range(-a, a))
print(listA)

# LIST COMPREHENSON
listA = [i for i in range(-a, a)]
print(listA)



