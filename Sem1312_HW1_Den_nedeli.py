# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
# проверяет, является ли этот день выходным. Пример:  - 6 -> да   - 7 -> да  - 1 -> нет


print('Please enter the day number: ')
day = int(input())

isCorrect = False
while isCorrect == False:                               # пока не знаю. как защищаться
    if day < 1 or day > 7:                              # от ввода нецифровых символов
        print('Incorrect value.')
        print('Please try to enter the day number again: ')
        day = int(input())
    else:    
        if day == 6 or day == 7:
            print('This day is a weekend')
            isCorrect = True
        else:    
            print('This day is not a weekend')
            isCorrect = True        