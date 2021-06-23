# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import math
import cProfile

def no_eratosthenes(i):
    last_prime = [2]
    next_prime = 3
    while len(last_prime) < i:
        flag = True
        for j in last_prime.copy():
            if next_prime % j == 0:
                flag = False
                break
        if flag:
            last_prime.append(next_prime)
        next_prime += 1
    return last_prime[-1]

def with_eratosthenes(i):
    number_primes = 0
    i_max = 2
    while number_primes <= i:
        number_primes = i_max / math.log(i_max)
        i_max += 1

    last_prime = [_ for _ in range(2, i_max)]

    for n in last_prime:
        if last_prime.index(n) <= n - 1:
            for j in range(2, len(last_prime)):
                if n * j in last_prime[n:]:
                    last_prime.remove(n * j)
        else:
            break
    return last_prime[i - 1]

i = int(input('Введите номер по счету простого числа: '))
print(no_eratosthenes(i))
cProfile.run('no_eratosthenes(i)')

print(with_eratosthenes(i))
cProfile.run('with_eratosthenes(i)')

# /usr/local/bin/python3.9 "/Users/kholann/Desktop/NLP/Алгоритмы и структуры данных на python/python/AlgorithmsPython/lesson4/task2.py"
# Введите номер по счету простого числа: 100
# 541
#          1182 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task2.py:11(no_eratosthenes)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       540    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#       539    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
# 541
#          1417 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.010    0.010    0.011    0.011 task2.py:25(with_eratosthenes)
#         1    0.000    0.000    0.000    0.000 task2.py:32(<listcomp>)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#       118    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       647    0.000    0.000    0.000    0.000 {built-in method math.log}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       118    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}
#       529    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
#
#
#
# Process finished with exit code 0

# Скорость алгоритма без использования «Решета Эратосфена» 1182 function calls in 0.001 seconds выше,
# чем скорость алгоритма с использованием «Решета Эратосфена» 1417 function calls in 0.011 seconds

# Сложность обоих алгоритмов O(n^2), где n - номер по счету простого числа.
