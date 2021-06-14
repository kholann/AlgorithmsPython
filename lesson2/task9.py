# 9.Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

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