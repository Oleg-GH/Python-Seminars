# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.   aaaaabbbcccc -> 5a3b4c
# Входные и выходные данные хранятся в отдельных текстовых файлах.             5a3b4c -> aaaaabbbcccc
# user_str = 'aaaahhhhhhaaaaahhh  yyyyoooooohhhhuuuuuuuuuuu!!!'

def coding(my_str):                         # функция кодирования строки
    count = 1
    li = []
    my_str = my_str + '^'                   # немного костыль (а, может, и идея), но так решается  
                                            # проблема с подсчетом последнего элемента строки
    for i in range(len(my_str) - 1):
        if my_str[i + 1] == my_str[i]:
            count += 1
        else:
            li.append(str(count) + my_str[i])
            count = 1

    res = ''
    res = res.join(li)
    return res    
       

def decoding(coded_str):                    # функция декодирования строки
    coded_str = coded_str + '^'             # такой же костыль (или идея), как в пред. функции
    decoded_str = ''
    count1 = ''
    for i in range(len(coded_str) - 1):
        if coded_str[i].isdigit():
            count1 += coded_str[i]
        else:
            decoded_str += coded_str[i] * int(count1)
            count1 = ''
    return decoded_str        


print('Eсли надо закодировать строку из текстового файла по алгоритму RLE, введите 1.')
print('Раскодировать - введите любой другой символ.')
n = input('Ваш выбор:  ')

if n == '1':
    with open('HW5_initial_string.txt', 'r', encoding='UTF-8') as file:      
        user_str = str(file.readline())
    print('Кодируем: ')
    print(user_str, '     - исходная строка')    
    result = coding(user_str)
    print(result, '                                - результат кодирования')  
    with open('HW5_coded_string.txt', 'w', encoding='UTF-8') as file1:
        file1.write(result)  

else:
    with open('HW5_coded_string.txt', 'r', encoding='UTF-8') as file2:
        coded_str = str(file2.readline())
    #coded_str = coded_str[2:-1] 
    print(coded_str, '                              - закодированная строка')
    result = decoding(coded_str)
    print(result, '   - результат раскодирования')  
    with open('HW5_initial_string.txt', 'w', encoding='UTF-8') as file3:
        file3.write(result)    
