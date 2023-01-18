# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

from random import randint as RI

def listShuffle(yourList):
    for j in range(len(yourList)):
        k = RI(0, len(yourList) - 1)        # случайное число, ограниченое длиной списка
        yourList.append(yourList.pop(k))    # выдергиваем случайный элемент и вставляем его в конец
        # yourList[j], yourList[k] = yourList[k], yourList[j]     # еще один способ перемешивания списка
      

myLength = int(input('Введите длину списка:  '))
myList = [i for i in range(myLength)]

print()
print('Исходный список: ')
print(*myList)

print()
print('Перемешанный список: ')
listShuffle(myList)
print(*myList)    

