# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a,n,d = int(input('введите первый элемент: ')),int(input('кол-во элементов: ')), int(input('разность: '))
# list_1 = []
res = [(a + (i - 1) * d) for i in range(1, n + 1)]
print(*res)