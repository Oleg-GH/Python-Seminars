# Удалить из текста все слова, содержащие символы "абв"

from string import punctuation

my_str = 'АБВ! ылоажы фыыдлх абв? Эщьшф вабвв ффлжв абВ'

# new_str = ' '.join(list(filter(lambda elem: 'абв' not in elem.lower(), my_str.split())))

res = []
# chars = ['.', ',', ', ', '!', '?']
x = 'абв'

for c in punctuation:
    my_str = my_str.replace(c, ' ' + c + ' ')

data = my_str.split()
print(data)

for item in data:
    if not x.lower() in item.lower():
        res.append(item)
res = ' '.join(res)
for c in punctuation:
    res = res.replace(' ' + c, c)        

print(res)