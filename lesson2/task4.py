#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
sum = 0
for i in range(n):
    sum += 1 / (-2) ** i

print(f'Сумма {sum}')
