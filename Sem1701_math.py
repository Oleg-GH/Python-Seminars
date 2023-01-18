# Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. 
# приоритет операций стандартный. Пример:  2+2 => 4;   1+2*3 => 7;    1-2*3 => -5;

data_1 = '2+2'
data_2 = '1+2*3'
data_3 = '1-2*3'
data_4 = '-2*3 - 4*5'

data = data_4.replace('+', ' + ').replace('-', ' - ').replace('/', ' / ').replace('*', ' * ').replace('- ', '-')
data = data.split()
print(data)

oper = {
    '+': lambda x, y: int(x) + int(y),
    '-': lambda x, y: int(x) - int(y),
    '/': lambda x, y: int(x) / int(y),
    '*': lambda x, y: int(x) * int(y),
}

def calc(data: list) -> int:
    for i in range(len(data)-1):
        if data[i] in '*/':
            operation = data[i]
            left = data[i-1]
            right = data[i+1]
            res = oper[operation](left, right)
            print(f'Результат операциии {left} {operation} {right} = {res}') # для отладки
            print('Новый список:', data[:i-1] + [str(res)] + data[i+2:]) # для отладки
            return data[:i-1] + [str(res)] + data[i+2:]
    for j in range(len(data)-1):
        if data[j] in '+-':
            operation = data[j]
            left = data[j-1]
            right = data[j+1]
            res = oper[operation](left, right)
            print(f'Результат операциии {left} {operation} {right} = {res}') # для отладки
            print('Новый список:', data[:i-1] + [str(res)] + data[i+2:]) # для отладки
            return data[:j-1] + [str(res)] + data[j+2:]

for item in oper.keys():
    while item in data:
        data = calc(data)

print(data[0])