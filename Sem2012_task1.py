# Задайте список. Напишите программу, которая определит, присутствует ли 
# в заданном списке строк некое число.

# Вариант наего зала (Дмитрий, Иван)

# text = ['BKfns', 'hjghgfjgfhgf', 'hgfdfdjhh;ljlhj', 'yutreytriytriyt', 'hjgfgf', 'hj']
# n = input('Введите искомый символ или символы: ')
# result = False

# for item in text:
#     if item.find(n) != -1:
#         print(True, item, text.index(item))
#     for i in range(len(item)):
#         if n == item[i]: 
#             result = True
#             print(result, item)            



# Int = Str.find(Str, start, end)


# Вариант решения 2

# text = ['BKfns', 'hjghgfjgfhgf', 'hgfdfdjhh;ljlhj', 'yutreytriytriyt', 'hjgfgf']
# search = 'gf'

# for i in range(len(text)):
#     if search in text[i]:
#         print(f"В элементе с индексом {i} есть '{search}'.")       # рабочий код от AlexShap

#Вариант решения 2 с новшеством из инета - печатаем список индексов элементов, где есть совпадения:

text = ['BKfns', 'hjghgfjgfhgf', 'hgfdfdjhh;ljlhj', 'yutreytriytriyt', 'hjgfgf']
search = 'gf'

indices = [i for i in range(len(text)) if search in text[i]]
if indices == 0:
    print('Совпадений нет')
else:
    print(f'Совпадения есть в следующих элементах списка: {indices}')



# Вариант решения 3

# text = ['BKfns', 'hjghgfjgfhgf', 'hgfdfdjhh;ljlhj', 'yutreytriytriyt', 'hjgfgf']
# search = 'gf'

# for item in text:
#     if item.find(str(search)) != -1:
#         print(f'В строке {item} есть подстрока {search}')