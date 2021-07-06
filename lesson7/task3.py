# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

import random

def median(array, i):
    if len(array) == 1:
        return array[0]

    p = random.choice(array)

    left = [el for el in array if el < p]
    right = [el for el in array if el > p]
    p_el = [el for el in array if el == p]

    if i < len(left):
        return median(left, i)
    elif i < len(left) + len(p_el):
        return p_el[0]
    else:
        return median(right, i - len(left) - len(p_el))

m = int(input('Введите натуральное число: '))
array = [random.randint(0, 49) for _ in range(2 * m + 1)]

print(f'Исходный массив:\n{array}')
print(f'Медиана исходного массива:\n{median(array, len(array) / 2)}')

#Проверка
array.sort()
print(f'Массив после сортировки:\n{array}')
print(f'Медиана массива:\n{array[len(array) // 2]}')

# Введите натуральное число: 3
# Исходный массив:
# [23, 41, 43, 19, 5, 28, 26]
# Медиана исходного массива:
# 26
# Массив после сортировки:
# [5, 19, 23, 26, 28, 41, 43]
# Медиана массива:
# 26