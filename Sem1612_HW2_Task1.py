# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:    6782 -> 23      -0,56 -> 11

def numDigitSum(number):
                        
    value = str(abs(number)).split('.')         # abs, чтобы и для отрицат.чисел работало
    result = 0

    for i in range(len(value[0])):
        result += int(value[0][i])              # сумма цифр до десятичной точки

    for j in range(len(value[1])):
        result += int(value[1][j])              # сумма цифр посое десятичной точки

    return result

num = float(input('Введите вещественное число:  '))
print(f'У числа {num} -> сумма цифр равна {numDigitSum(num)}')            


# from decimal import Decimal
# num = abs(Decimal(input('Введите вещественное число: ')))
# while num != int(num):
#     num *= 10
# my_sum = 0
# while num > 0:
#     my_sum += int(num % 10)
#     num /= 10
# print(my_sum)            # еще один вариант через Decimal