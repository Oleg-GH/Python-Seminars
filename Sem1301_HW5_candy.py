# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет. Играют два игрока, делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота;    b) Подумайте как наделить бота 'интеллектом'

from random import randint

def invite(name):
    take = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while take < 1 or take > 28:
        take = int(input(f"{name}, не шалите, введите корректное количество конфет: "))
    return take

def notice(name, quantity, total_player, remains):
    print(f"    {name} взял {quantity} конфет, у него их уже {total_player}. На столе осталось {remains} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
turn = randint(0, 2)            # очередность первого хода
if turn:
    print(f"Первым ходит {player1}")
else:
    print(f"Первым ходит {player2}")

counter1 = 0
counter2 = 0

while value > 28:
    if turn:
        number = invite(player1)
        counter1 += number
        value -= number
        notice(player1, number, counter1, value)
        turn = False
    else:
        number = invite(player2)
        counter2 += number
        value -= number
        notice(player2, number, counter2, value)
        turn = True

if turn:
    print(f"Все конфеты забирает {player1}")
else:
    print(f"Все конфеты забирает {player2}")