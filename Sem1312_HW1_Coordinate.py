# Напишите программу, которая по заданному номеру четверти показывает диапазон 
# возможных координат точек в этой четверти (x и y).

print('Please enter the quarter of the coordinate plane (1, 2, 3 or 4): ')
my_quater = int(input('quater = '))

isCorrect = False
while isCorrect == False:                                               # пока не знаю. как защищаться
    if my_quater < 1 or my_quater > 4:                                  # от ввода нецифровых символов
        print('Incorrect value. The quarter should not be less than 1 and more than 4.')
        print('Please try to enter the correct quarter again: ')
        my_quater = int(input('quater = '))        
    else:    
        if my_quater == 1:
            print(f'quater = {my_quater}, x > 0, y > 0')
            isCorrect = True
        elif my_quater == 2:
            print(f'quater = {my_quater}, x < 0, y > 0')
            isCorrect = True   
        elif my_quater == 3:
            print(f'quater = {my_quater}, x < 0, y < 0')
            isCorrect = True 
        else:    
            print(f'quater = {my_quater}, x > 0, y < 0')
            isCorrect = True      