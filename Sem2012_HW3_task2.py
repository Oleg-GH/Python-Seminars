# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д. Пример:  [2, 3, 4, 5, 6] => [12, 15, 16];  [2, 3, 5, 6] => [12, 15]

import random

my_list = []
my_length = random.randint(3, 7)

for _ in range(my_length):
    my_list.append(random.randint(0, 10))

my_result = []
index = 0

while index < ((len(my_list) - 1) // 2 + 1):
    my_result.append(my_list[index] * my_list[-index - 1])
    index += 1

print(my_list, ' => ', my_result)    