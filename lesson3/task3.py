# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array_random = [random.randint(0, 29) for _ in range(10)]
print(f'Массив до изменения: {array_random}')

max_el = array_random[0]
min_el = array_random[0]

for i in array_random:
    if i > max_el:
        max_el = i
    elif i < min_el:
        min_el = i

index_min = array_random.index(min_el)
index_max = array_random.index(max_el)

array_random[index_min], array_random[index_max] = array_random[index_max], array_random[index_min]

print(f'Массив после того, как поменяли местами минимальный и максимальный элементы: {array_random}')