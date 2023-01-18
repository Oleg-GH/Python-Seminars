# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции 
# с нечетным индексом. # Пример:   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

my_list = []
my_length = random.randint(3, 10)

for _ in range(my_length):
    my_list.append(random.randint(1, 10))

index = 1
sum = 0
my_list1 = []

while index < len(my_list):             # < my_length
    sum += my_list[index]
    my_list1.append(my_list[index])
    index += 2

print(f'Исходный список: {my_list} -> на нечетных позициях элементы:  {my_list1}, ответ: {sum}')
