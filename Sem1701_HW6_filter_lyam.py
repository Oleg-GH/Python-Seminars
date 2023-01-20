# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i - 1]. Найдите это число.

data = '1 2 3 4 5 6 8 9 11 12 13 14 15 17 18 19 21'
data = [int(x) for x in data.split()]     
                                                
my_func = list(filter(lambda i: not data[i] + 1 == data[i + 1], range(len(data) - 1)))  # filter() lambda

for item in my_func:
    print(data[item] + 1)