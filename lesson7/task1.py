# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble_sort(array, rev=False):
    if rev:
        left = 1
        right = 0
    else:
        left = 0
        right = 1
    n = 1
    len_ar = len(array)

    while n < len_ar:
        c = True
        for i in range(n - 1, len_ar - n):
            if array[i + left] > array[i + right]:
                array[i], array[i + 1] = array[i + 1], array[i]
                c = False
        if c:
            break
        for j in range(len_ar - n, n - 1, -1):
            if array[j - left] < array[j - right]:
                array[j], array[j - 1] = array[j - 1], array[j]
        n += 1

array = [random.randint(-100, 99) for _ in range(15)]
print(f'Исходный массив:\n{array}')

bubble_sort(array, rev=True)
print(f'Отсортированный по убыванию массив:\n{array}')

# Исходный массив:
# [39, 81, 86, 19, -69, -62, 46, 69, 11, -32, 79, -49, -76, -39, -23]
# Отсортированный по убыванию массив:
# [86, 81, 79, 69, 46, 39, 19, 11, -23, -32, -39, -49, -62, -69, -76]