# Дан список чисел. Создайте список, в который попадают числа, образующие возрастающую последовательность.
# Порядок элементов менять нельзя. Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 2, 3, 4] и т.д.


data = [1, 5, 2, 3, 4, 6, 1, 7]
result = []
count = 0
num1 = 1
while count < len(data):
    for i in range(len(data) - 1):
        temp = []
        temp.append(data[i])
        cur_max = data[i]
        for j in range(num1, len(data)):
            if data[j] > cur_max:
                temp.append(data[j])
                cur_max = data[j]
        if len(temp) > 1 and temp not in result:
            result.append(temp)
    count += 1
    num1 += 1    

print(result)                