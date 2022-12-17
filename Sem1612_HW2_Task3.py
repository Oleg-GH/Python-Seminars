# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

from random import randint as RI

def listShuffle(yourList):
    myList1 = []
    for j in range(len(yourList)):
        k = RI(0, len(yourList) - 1)        # случайное число, ограниченое длиной списка
        myList1 += yourList[k]
        myList.remove(yourList[k])          # длина списка уменьшается с каждой итерацией
    return myList1    

myLength = int(input('Введите длину списка:  '))
myList = []
for i in range(myLength):
    myList.append(input())

print()
print('Исходный список: ')
print(myList)

ShufList1 = listShuffle(myList)

print()
print('Перемешанный список: ')
print(ShufList1)    

