# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру 
# дробной части числа. *Примеры:* - 6,78 -> 7 - 5 -> нет - 0,34 -> 3 

number = float(input('Введите вещественное число:  '))

if number != int(number):                 
    print(f'Первая цифра дробной части числа {number} -> '
            f'{int(abs(number)*10)%10}')
else:
    print(f'У числа {int(number)} нет дробной части.')


# number = number.split('.')    # другой способ, через разделение по точке на список списков
# print(number)                # для проверки

# if len(number) > 1:
#     print(number[1][0])
# else:
#     print ('Число целое')   
# 

# Вариант 3
# 
# num = input("Введите число: ")
# if '.' in num:
#   index_num = num.find('.')
#   print(num[index_num])
# elif ',' in num:
#   index_num = num.find('.')
#   print(num[index_num])
# else:
#   print('No')


# Вариант 4 (не работает с отрицат.числами)

# num = input("Введите число: ")
# if num.isdigit():
#     print('Нет')
# else:
#     num = int(float(num) * 10 % 10)
#     print(num)