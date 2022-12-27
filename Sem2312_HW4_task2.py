# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов. (Прим. Файлы созданы по результату решения задачи № 1 )


def strToDict(polynom: str) -> dict:
    polynom = polynom.replace(' + ', ' ').replace(' - ', ' -').replace(' -x', ' -1*x')\
        .replace(' x', ' 1*x').replace('*x ', '*x**1 ').split()[:-2]
    my_dict = {}
    for item in polynom:                        # Функция создания словаря из исходного многочлена
        i = item.split('*x**')                  # (ключ - степень, значение - коэффициент)
        if len(i) > 1:                          
            my_dict[int(i[1])] = int(i[0])
        elif len(i) == 1:
            my_dict[0] = int(i[0])    
    return my_dict         

def sum_dict(pol1, pol2):                       # Функция получения нового словаря путем сложения
    result_dict = {}                            # коэффициентов по соответствующим ключам-степеням
    result_dict.update(pol1)
    result_dict.update(pol2)

    for key in result_dict:
        result_dict[key] = pol1.get(key, 0) + pol2.get(key, 0)   # все гениальное просто ))
    return result_dict    

def dictToString(polynome):                     # Фунция преобразования словаря (где ключи -
    polynome1 = []                              # степени х, а значения - коэффициенты)
    for key, value in polynome.items():         # в строковое выражение (многочлен)
        if value != 0:
            polynome1.append(f'{value}*x**{key}')
    polynome1 = ' + '.join(polynome1) + ' = 0'
    polynome1 = polynome1.replace('+ -', '- ').replace(' 1*x', ' x').replace('*x**0', '')\
                         .replace('x**1', 'x').replace('-1*x', '-x')
    return polynome1    

with open('HW4_task2_1.txt', 'r') as data:      # Считываем строковые выражения:
    polynom1 = data.readline()                  # из первого файла
with open('HW4_task2_2.txt', 'r') as data:      # из второго файла
    polynom2 = data.readline()

dict_poly1 = strToDict(polynom1)                # Получаем словарь (степень-коэффициент) для 1й строки
dict_poly2 = strToDict(polynom2)                # Получаем словарь (степень-коэффициент) для 2й строки
str_result = sum_dict(dict_poly1, dict_poly2)   # Получаем словарь (степень-коэффициент) для суммы 1го и го словарей

print(dictToString(dict_poly1))             # Для наглядности распечатываем в консоли первый многочлен,
print(dictToString(dict_poly2))             # второй многочлен
print(dictToString(str_result))             # и результат их сложения (вызвав функцию преобразования словаря в строку)

with open('HW4_task2_result.txt', 'w') as data:      # Записываем результат сложения в файл
    data.write(dictToString(str_result))             # HW4_task2_result.txt
