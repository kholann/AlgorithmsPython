# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и
# разрядность вашей ОС.

# версия Python 3.8.5
# macOS Big Sur version 11.2.3 - 64bit

import sys

def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par

# 1 программа
numb = input('Введите натуральное число: ')
even = 0
odd = 0
for i in numb:
    j = int(i)
    if j % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'У числа {numb}: четных цифр - {even}, нечетных - {odd} ')

sum_1 = sys.getsizeof(numb) + sys.getsizeof(even) + sys.getsizeof(odd) + sys.getsizeof(j) + sys.getsizeof(i)

print(f'Под переменные задействованно {sum_1} байт памяти')
#/usr/local/bin/python3.9 "/Users/kholann/Desktop/NLP/Алгоритмы и структуры данных на python/python/AlgorithmsPython/lesson6/task1.py"
# Введите натуральное число: 46
# У числа 46: четных цифр - 2, нечетных - 0

# Под переменные задействованно 181 байт памяти

# Введите натуральное число: 1234
# У числа 1234: четных цифр - 2, нечетных - 2
# Под переменные задействованно 187 байт памяти

# С увеличением разрядности натурального числа увеличивается количество занимаемой памяти

# 2 программа
def sum_numb(numb):
    sum = 0
    for i in numb:
        sum += int(i)
    return sum

list_numb = [j for j in input('Введите числа и нажмите Enter').split()]

max_numb = 0
max_sum = 0
for j in list_numb:
    if sum_numb(j) > max_sum:
        max_numb = j
        max_sum = sum_numb(j)

print(f'У числа {max_numb} наибольшая сумма цифр - {max_sum}')

sum_2 = sys.getsizeof(numb) + sys.getsizeof(sum) + sys.getsizeof(i) + sys.getsizeof(list_numb) + sys.getsizeof(j) + sys.getsizeof(max_numb)+sys.getsizeof(max_sum)

print(f'Под переменные задействованно {sum_2} байт памяти')

# Введите числа и нажмите Enter456789
# У числа 456789 наибольшая сумма цифр - 39
# Под переменные задействованно 399 байт памяти

# Введите числа и нажмите Enter123456789
# У числа 123456789 наибольшая сумма цифр - 45
# Под переменные задействованно 407 байт памяти

# С увеличением разрядности числа увеличивается количество занимаемой памяти

# По полученным результатам 1 программа с наиболее эффективным использованием памяти (181, 187 байт памяти),
# чем 2 программа (399, 407 байт памяти).