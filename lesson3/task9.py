# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []

for i in range(5):
    matrix.append([])
    matrix[i].extend([random.randint(0, 99) for _ in range(5)])

min_l = []
min_l.extend(matrix[0])

for str in matrix:
    print()
    print(('{:4d} ' * len(str)).format(*str))
    i = 0
    for j in str:
        if j < min_l[i]:
            min_l[i] = j
        i += 1

print()
print('Минимальные элементы столбцов матрицы')
print(('{:4d} ' * len(min_l)).format(*min_l))
print()

min_l.sort(reverse=True)
print('Максимальный элемент среди минимальных элементов столбцов матрицы: ', min_l[0])
