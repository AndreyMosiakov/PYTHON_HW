# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = int(input("введите трехзначное число:" ))

if a < 100 or a > 999:
    print('введите ТРЁХзначное число! ')
else:    
    
   
    a3= a%10
    temp = a//10
    a2=temp%10
    a1=temp//10

    print('сумма цифр в числе ',a, ' = ', a1 + a2 + a3)