# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для получения случайного int

from random import randint as RI

def listShuffle(yourList):
    for j in range(len(yourList)):
        k = RI(0, len(yourList) - 1)        
        yourList.append(yourList.pop(k))    

myLength = int(input('Введите длину списка:  '))
myList = [i for i in range(myLength)]               # List Comprehension

print('Исходный список: ')
print(*myList)

print('Перемешанный список: ')
listShuffle(myList)
print(*myList)    
