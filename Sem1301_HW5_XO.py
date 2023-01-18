# Создайте программу для игры в 'Крестики-нолики'. НЕОБЯЗАТЕЛЬНО: Добавить игру против бота с интеллектом

def paint_table():                              # отрисовка игрового поля (таблицы)
    for i in range(3):
        print(' ', my_table[0 + i * 3], '|', my_table[1 + i * 3], '|', my_table[2 + i * 3])
        if i < 2:
            print(' -----------')
    print()        

def try_input(my_char):                         # ввод Х или 0 в клетки игрового поля
    while True:
        place = input('Укажите поле, куда поставить ' + my_char + ' : ')
        print()
        if not (place in '123456789'):
            print('Ты ошибся. Введи корректное число от 1 до 9: ')
            continue 
        place = int(place)                       # с проверками на корректность введения поля
        if str(my_table[place - 1]) in 'XO':     # и его неповторяемость
            print('Это поле уже занято. Введи другое число от 1 до 9: ')   
            continue
        my_table[place - 1] = my_char
        break

def check_win_set():                             # проверка выигрышных комбинаций
    for each in win_set:
        if (my_table[each[0] - 1]) == (my_table[each[1] - 1]) == (my_table[each[2] - 1]):
            return my_table[each[1] - 1]
    else: 
        return False

my_table = list(range(1, 10))
win_set = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
print()

count = 0
while True:
    paint_table()
    if count % 2 == 0:
        try_input('X')
    else:
        try_input('O')
    if count > 3:
        winner = check_win_set()   
        if winner:
            paint_table()
            print('Победил ', winner, '! Поздравляем!')
            print()
            break  
    count += 1
    if count > 8:                       # ограничение ходов игры (принудит.завершение)
        paint_table()                   # при отсутствии победителей на предыдущ.ходах
        print('Победила Дружба! Ничья!')
        print()
        break



