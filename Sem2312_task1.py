# 3. Создайте словарь, заданный по формуле 3*n+1, где n это ключ, а формула значение 
# Пример: - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19} 

my_dict = {}

number = int(input('Введите целое число:  '))

for n in range(1, number + 1):
    my_dict[n] = 3 * n + 1

print(my_dict.get(7, 'Такого ключа нет'))   


