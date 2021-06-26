# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

Company = collections.namedtuple('Company', ['p1', 'p2', 'p3', 'p4'])

companies = {}

n = int(input("Введите количество предприятий: "))

for i in range(n):
    name = input('Наименование предприятия: ')
    profit1 = int(input('Прибыль за 1-й квартал: '))
    profit2 = int(input('Прибыль за 2-й квартал: '))
    profit3 = int(input('Прибыль за 3-й квартал: '))
    profit4 = int(input('Прибыль за 4-й квартал: '))
    companies[name] = Company(
        p1=profit1,
        p2=profit2,
        p3=profit3,
        p4=profit4
    )

total_profit = ()

for name, profit in companies.items():
    total_profit += profit

avg_total_profit = sum(total_profit) / len(companies)
print(f'Средняя прибыль за год для всех предприятий {avg_total_profit}')

print('Предприятия, у которых прибыль выше среднего:')

for name, profit in companies.items():
    if sum(profit) > avg_total_profit:
        print(f'{name} - {sum(profit)}')

print('Предприятия, у которых прибыль ниже среднего:')
for name, profit in companies.items():
    if sum(profit) < avg_total_profit:
        print(f'{name} - {sum(profit)}')