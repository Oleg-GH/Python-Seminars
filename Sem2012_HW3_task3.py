# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значениями отличных от 0 дробных частей элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

my_list = []

for _ in range(random.randint(2, 10)):
    index = random.randint(0, 5)
    my_list.append(round(random.uniform(0, 10), index))

fractional_parts = []

for _ in range(len(my_list)):
    if my_list[_] % 1 != 0:
        fractional_parts.append(round((my_list[_] % 1), 3))

max = fractional_parts[0]
min = fractional_parts[0]

for i in range(len(fractional_parts)):
    if max < fractional_parts[i]:
        max = fractional_parts[i]
    if min > fractional_parts[i]:
        min = fractional_parts[i]    

result = round((max - min), 3)

print(my_list, ' => ', result)
print(fractional_parts, '  -   это дробные части, кроме равных 0')
print(f'max = {max},  min = {min}')
