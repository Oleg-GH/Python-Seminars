# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N 
# *Примеры:* при 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 

number = int(input('Введите целое число: '))

my_list = []

for item in range(-number, number+abs(number)//number, abs(number)//number):
    my_list.append(item)


print(*my_list, sep =', ')
    



# a = []

# for i in range(-nimber, abs(number)//number, abs(number)//number)
#     a.apend(i)

# print(*a, sep=', ')    