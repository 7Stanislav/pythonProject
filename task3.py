"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

num = (input("Введите целое положительное число: "))
first = int(num)
second = num + num
third = num + num + num
sum_num = first + int(second) + int(third)
print(f'n + nn + nnn = {sum_num}')