# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


def exponent(a, b):
    if b == 0:
        return 1
    return a * exponent(a, b - 1)


num1 = int(input('введите число: '))
num2 = int(input('введите степень: '))
print(exponent(num1, num2))
