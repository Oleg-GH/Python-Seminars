# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). Пример:
# x=34; y=-30 -> 4       x=2; y=4-> 1       x=-34; y=-30 -> 3

print('Please enter the coordinates (not equal 0): ')
xa = int(input('x = '))
ya = int(input('y = '))

isCorrect = False
while isCorrect == False:                               # пока не знаю. как защищаться
    if xa == 0 or ya == 0:                              # от ввода нецифровых символов
        print('Incorrect value. The coordinates should not be equal 0.')
        print('Please try to enter the correct number again: ')
        xa = int(input('x = '))
        ya = int(input('y = '))
    else:    
        if xa > 0 and ya > 0:
            print(f'х = {xa}, y = {ya} -> 1')
            isCorrect = True
        elif xa < 0 and ya > 0:
            print(f'х = {xa}, y = {ya} -> 2')
            isCorrect = True   
        elif xa < 0 and ya < 0:
            print(f'х = {xa}, y = {ya} -> 3')
            isCorrect = True 
        else:    
            print(f'х = {xa}, y = {ya} -> 4')
            isCorrect = True        