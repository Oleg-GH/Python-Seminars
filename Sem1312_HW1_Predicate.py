#Напишите прог-му для. проверки истинности утвер-ния ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех зн-й предикат

print('¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z    -   истинно или ложно?')
predicate = ["X", "Y", "Z"]
new_set = []
for i in range(3):
    new_set.append(input(f'Введите значение {predicate[i]}: '))

left_side = not (new_set[0] or new_set[1] or new_set[2])
right_side = not new_set[0] and not new_set[1] and not new_set[2]

if left_side == right_side:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')    