# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
# элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

array_random = [random.randint(0, 10) for _ in range(10)]
print(*array_random)

min_elem = array_random[0]
max_elem = array_random[1]

for i, item in enumerate(array_random):
    if item <= min_elem:
        min_elem = item
        min_index = i
    if item >= max_elem:
        max_elem = item
        max_index = i

print(f'Минимальный элемент = {min_elem}(индекс {min_index})\nМаксимальный элементам = {max_elem} (индекс {max_index})')

if max_index < min_index:
    max_index, min_index = min_index, max_index

print(f'Элементы между минимальным и максимальным: {array_random[min_index + 1:max_index]}')

sum = 0
for i in range(min_index + 1, max_index):
    sum += array_random[i]

print(f'Сумма элементов, находящихся между минимальным и максимальным элементами = {sum}')