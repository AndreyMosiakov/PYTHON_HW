# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n= int(input('введите число N: '))
result = 1
while result < n: 
    
    print(result, end =" ")
    result = result*2
