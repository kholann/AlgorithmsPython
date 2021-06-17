# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

array_random = [random.randint(0, 99) for _ in range(10)]
print(f'Массив: {array_random}')
sort_list = []
sort_list.extend(array_random)
sort_list.sort()

print(f'Два наименьших элемента: {sort_list[0]} и {sort_list[1]}')