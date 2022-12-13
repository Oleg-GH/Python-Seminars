# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них. 
# Примеры: - 1, 4, 8, 7, 5 -> 8 - 78, 55, 36, 90, 2 -> 90 

my_list = []

for i in range(5):
    number = int(input(f'Введите {i+1} число: '))
    my_list.append(number)

my_max = my_list[0]

for i in range(1, len(my_list)):
    if my_max < my_list[i]:
        my_max = my_list[i]

print(my_list, '->', 'max = ', my_max)        