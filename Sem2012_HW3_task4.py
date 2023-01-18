Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:  45 -> 101101     3 -> 11       2 -> 10

def DoBinary(num):
    my_list = []
    while num >= 1:
        my_list.append(str(round(num % 2)))
        num = (num - num % 2) / 2
        
    result = []

    for _ in range(len(my_list) - 1, -1, -1):
        result.append(my_list[_])
    
    result = ''.join(result)
    return result

number = int(input('Введите десятичное число, которое необходимо перевести в двоичную систему: '))
print(number, ' => ', DoBinary(number))   


# number = int(input('Введите десятичное число, которое необходимо перевести в двоичную систему: '))

# bi_num = ''
# while number > 0:
#     bi_num = str(number%2) + bi_num
#     number //= 2

# print(bi_num)    