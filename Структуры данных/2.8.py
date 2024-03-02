# a = int(input())
a = 49

count_tens = a // 10
count_units = a % 10
num = count_units * 10 + count_tens

print('Полученное число: ', num)
