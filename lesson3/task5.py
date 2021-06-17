# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array_random = [random.randint(-10, 10) for _ in range(10)]

el = -float('inf')

for i, item in enumerate(array_random):
    if el < item < 0:
        el = item
        min_idx = i

print(f'В массиве: \n{array_random} \nмаксимальный отрицательный элемент {el} \nего индекс = {min_idx}')