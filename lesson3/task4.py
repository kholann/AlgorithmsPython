# 4. Определить, какое число в массиве встречается чаще всего.

import random

array_random = [random.randint(1, 100) for _ in range(30)]
d = dict.fromkeys(array_random, 0)

for i in array_random:
    d[i] += 1

numb = 0
for key in d:
    if d[key] > numb:
        max_key = key
        numb = d[key]

print(f'В списке \n{array_random} \nчаще всего встречается число {max_key} - {numb} раз(a)')
