# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)  
# многочлена и записать в файл многочлен степени k. Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def create_dict(degree: int):                       # Функция создания словаря, где ключ - степень х,
    polynom_first = {}                              # а значение - рандомный коэффициент члена многочлена
    for k in range(degree, -1, -1):                  
        polynom_first[k] = random.randint(-12, 12) 
    return polynom_first

def dictToString(polynome):                         # Функция преобразования словаря в строковое
    polynome1 = []                                  # выражение (многочлен)
    for key, value in polynome.items():
        if value != 0:
            polynome1.append(f'{value}*x**{key}')
    polynome1 = ' + '.join(polynome1) + ' = 0'
    polynome1 = polynome1.replace('+ -', '- ').replace(' 1*x', ' x').replace('*x**0', '')\
                         .replace('x**1 ', 'x ').replace('-1*x', '-x').replace('- x**0', '- 1')\
                         .replace('*+ x**0', '+ 1').replace('-1*x**', '-x**')
    return polynome1    

power = int(input('Введите наибольшую степень многочлена: '))   # Задаем макс. степень многочлена
print('Запись многочлена возможна в один из двух файлов.')
correctness = False
while correctness != True:                      # Вводим номер файла (с проверкой на корректность ввода)
    print('Введите номер файла 1 или 2:', end=' ')
    file_number = input()
    if file_number == '1' or file_number == '2':
        correctness = True      
    else:
        print('Вводить можно только 1 или 2. Попробуйте снова.')    

polynom = create_dict(power)                    # Получаем словарь
print(polynom)                                  # Распечатываем его для наглядности в консоль
polynom1 = dictToString(polynom)                # Преобразуем словарь в строковое выр-е (многочлен)
print(polynom1)                                 # Распечатываем строковое выр-е (многочлен) в консоль

if file_number == '1':                          # Если задан первый файл,
    with open('HW4_task2_1.txt', 'w') as data:  # записываем результат в файл HW4_task2_1.txt
        data.write(polynom1)                   
else:
    with open('HW4_task2_2.txt', 'w') as data:  # иначе записываем результат в файл HW4_task2_2.txt
        data.write(polynom1)                    # Запись результата в два файла сделана для получения
                                                # различных исходных данных для задачи 2.                 



