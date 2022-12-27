# Создайте словарь, значения которого находятся по формуде 3n+1

# my_dict = {}

# number = int(input('Введите целое число: '))

# for n in range(1, number + 1):
#     my_dict[n] = 3 * n + 1

# print(my_dict.get(7, 'Такого ключа нет'))    



# my_string = 'Питон самый лучший язык в мире'

# # my_string = my_string.split('и')
# # print(my_string)                              # ['П', 'тон самый лучш', 'й язык в м', 'ре']


# my_string = my_string.replace('и', '$')
# print(my_string)                            # П$тон самый лучш$й язык в м$ре


# print(my_string.startwith('Пит'))
# print(my_string)                            # True   проверяет, начинается ли строка с 'Пит', но не изменяет


# print(my_string.startwith('пит'))           # False   проверяет, начинается ли строка с 'пит', но не изменяет
# print(my_string)                            


# print(my_string.lower().startwith('пит'))   # True   проверяет, начинается ли строка с 'пит', изменяя все буквы на строчные
# print(my_string)                            


# print(my_string.upper().startwith('ПИТ'))   # True   проверяет, начинается ли строка с 'ПИТ', изменяя все буквы на заклавные
# print(my_string)                            


# print(my_string.lower().endswith('ире'))   # True   проверяет, заканчивается ли строка на 'ире', изменяя все буквы на строчные
# print(my_string)  


# my_list = ['1','2','3','4','5','6','7','8']
# print(' '.join(my_list))                    # 1 2 3 4 5 6 7 8
# print(''.join(my_list))                     # 12345678

# glue = '|'
# print(glue.join(my_list))                   # 1|2|3|4|5|6|7|8


my_string = '    Питон самый лучший язык в мире\n'
print(my_string)                              #     Питон самый лучший язык в мире + пробел
print(my_string.strip())                      # Питон самый лучший язык в мире (справа и слева обрезано все лишнее)
print(my_string.rstrip())                     #     Питон самый лучший язык в мире  (справа обрезан перенос строки)
print(my_string.lstrip())                     # Питон самый лучший язык в мире (слева обрезаны пробелы, но не перенос справа)


