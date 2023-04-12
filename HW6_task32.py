# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
list_1 = [randint(-50,50) for i in range(20)]
print(list_1)
maxi = int(input('максимальное число: '))
mini = int(input('минимальное число: '))
index_list = []
if maxi >= mini:
    for i in range(len(list_1)):
        if maxi>=list_1[i] and mini<=list_1[i]:
            index_list.append(i)
    print(f'всего таких элементов {len(index_list)},'  ,index_list)        
