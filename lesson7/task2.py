# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random

def merge_sort(array):
    def merge(a, b):
        i = 0
        j = 0
        len_a = len(a)
        len_b = len(b)
        result = []
        while i != len_a and j != len_b:
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                result.append(b[j])
                i += 1
                j += 1
        if i < len_a:
            result.extend(a[i:])
        if j < len_b:
            result.extend(b[j:])
        return result

    if len(array) < 2:
        return array

    id_x = len(array) // 2
    return merge(merge_sort(array[:id_x]), merge_sort(array[id_x:]))

array = [random.randint(0, 49) for _ in range(15)]
print(f'Исходный массив:\n{array}')

new_array = merge_sort(array)
print(f'Отсортированный по возрастанию массив:\n{new_array}')

# Исходный массив:
# [4, 49, 41, 48, 14, 32, 47, 31, 32, 42, 37, 8, 2, 9, 14]
# Отсортированный по возрастанию массив:
# [2, 4, 8, 9, 14, 14, 31, 32, 32, 37, 41, 42, 47, 48, 49]