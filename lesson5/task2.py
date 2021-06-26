# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import defaultdict
from collections import deque

def numb_dex(string):
    dex = 0
    numb = deque(string)
    numb.reverse()
    for i in range(len(numb)):
        dex += table[numb[i]] * 16 ** i
    return dex

def numb_hex(numb):
    num = deque()
    while numb > 0:
        ost = numb % 16
        for i in table:
            if table[i] == ost:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)

signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0

for k in signs:
    table[k] += counter
    counter += 1

number_1 = numb_dex(input('Введите первое число в шестнадцатиричном формате:\n ').upper())
number_2 = numb_dex(input('Введите второе число в шестнадцатиричном формате:\n ').upper())

print(f'Сумма чисел: {numb_hex(number_1 + number_2)}')
print(f'Произведение чисел: {numb_hex(number_1 * number_2)}')