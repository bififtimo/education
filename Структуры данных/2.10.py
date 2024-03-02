# a = int(input())
a = 876

count_tens = (a // 10) % 10
count_units = a % 10

print('Последняя цифра числа (единицы): ', count_units)
print('Средняя цифра числа (десятки): ', count_tens)
# print(count_units, count_tens, sep='')
