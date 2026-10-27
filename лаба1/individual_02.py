n = int(input("Введите шестизначное число: "))

d1 = n // 100000
d2 = (n // 10000) % 10
d3 = (n // 1000) % 10
d4 = (n // 100) % 10
d5 = (n // 10) % 10
d6 = n % 10

sum_first = d1 + d2 + d3
sum_last = d4 + d5 + d6


result = abs(sum_first - sum_last)


print(f"Модуль разности сумм: {result}")
