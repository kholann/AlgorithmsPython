# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for j in range(4):
        numb = int(input(f'Введите элемент ({i+1},{j+1}): '))
        sum += numb
        matrix[i].append(numb)

    matrix[i].append(sum)

for i in matrix:
    print(('{:>4d}' * 5).format(*i))

