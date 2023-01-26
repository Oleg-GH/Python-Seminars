def main_menu():
    menu_list = [' Открыть журнал',  # +
                 ' Сохранить журнал',  # +
                 ' Выбрать предмет',
                 ' Добавление предмета'  # +
                 ' Выход'] #+
    
    menu_student = [' Список всех студентов',
                    ' Поиск ученика',
                    ' Добавление ученика',
                    ' Удаление ученика ', # +
                    ' Изменнение ученика '
                    ' Добавить оценку',
                    ' Удалить оценку',
                    ' Изменнить оценку',
                    ' Выход '
                    ]

    print('\n\033[33mГлавное меню:\n\033[0m')
    for i in range(len(menu_list) - 1):
        print(f'\t{i + 1}. {menu_list[i]}')
    print(f'\t{0}. {menu_list[-1]}')

    while True:
        user_input = input('\n\033[33mВведи команду >: \033[0m')
        input_valid = validate_input(user_input, menu_list)
        if input_valid is not None:
            break
        else:
            print("\n\033[31mНеверный ввод! Пожалуйста, введите число от 0 до", len(
                menu_list) - 1, "\033[0m")
    print()
    return input_valid
  
def school_read(sch_list):
    for i in range(len(sch_list)):
        print(f'{i+1} - {sch_list[i]}')  
    user_input = input('\n\033[33mВведи команду >: \033[0m')
    return int(user_input) -1


    


# Функция проверки на правильность ввода выбора пункта меню
def validate_input(user_input: str, menu_list) -> int:
    if user_input.isnumeric():
        user_input = int(user_input)
        if user_input >= 0 and user_input <= len(menu_list) - 1:
            return user_input
    return None


# Функция вывода всех учеников (успеваемость всех учеников')
def show_all_students(db: list):
    for i in range(len(db)):
        user_id = i + 1
        print(f'\t{user_id}', end='. ')
        for v in db[i].values():
            print(f'{v}', end=' ')
        print()

# Функция поиска ученика
def search_by_parameters(db: list):
    print("1. Поиск по фамилии")
    print("2. Поиск по имени")
    print("3. Поиск по фамилии и имени")
    print("4. Отменить поиск")

    keys = ['lastname', 'firstname']
    record = {}

    while record == {}:
        try:
            search_by = int(input("\nПожалуйста, введите число от 1 до 4: "))

            if search_by not in range(1, 5):
                raise ValueError

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 4: ")
            continue
        if search_by == 1:
            record[keys[0]] = input("Введите фамилию для поиска: ")
          
        elif search_by == 2:
            record[keys[1]] = input("Введите имя для поиска: ")

        elif search_by == 3:
            record[keys[0]] = input("Введите фамилию для поиска: ")
            record[keys[1]] = input("Введите имя для поиска: ")
            
            return record
          
        elif search_by == 4:
            print("Поиск отменен!")
            return None

# Функция добавления нового предмета
def add_subject():
    print('Вы уверены что хотите добавить новый предмет?\n1 - Да\n2 - Нет: \n')
    
    try:
        enter_number = int(input("\nПожалуйста, введите число 1 или 2: "))
        if enter_number not in range(1, 3):
            raise ValueError

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число 1 или 2: ")
        return
    
    if enter_number == 1:
      new_subject = dict()
      new_subject['subject'] = input('\tВведите название предмета: ')
      
      return new_subject
    
    else:
      print("Добавление нового предмета отменено!")
      return None
    
# Функция добавления нового ученика
def adding_student():
    print('Вы уверены что хотите добавить нового ученика?\n1 - Да\n2 - Нет: \n')

    while True:
        try:
            enter_number = int(input("\nПожалуйста, введите число 1 или 2: "))
            if enter_number not in range(1, 3):
                raise ValueError

        except ValueError:
            print("Неверный ввод. Пожалуйста, введите число 1 или 2: ")
            continue

        if enter_number == 1:
            new_student = dict()

            while True:
                id_input = input('\tВведите id ученика: ')
                if id_input.isnumeric():
                    new_student['id'] = id_input
                    break

                else:
                    print("Неверный ввод. ID должен быть числом. Пожалуйста, введите id еще раз: ")

            new_student['firstname'] = input('\tВведите имя ученика: ')
            new_student['lastname'] = input('\tВведите фамилию ученика: ')
            return new_student
        else:
            print("Добавление ученика отменено!")
            return None

# Функция удаления ученика
def deleting_student(db: list):
  print('Вы уверены что хотите удалить ученика?\n1 - Да\n2 - Нет: \n')
  
  try:
    enter_number = int(input("\nПожалуйста, введите число 1 или 2: "))
    if enter_number not in range(1, 3):
      raise ValueError
    
  except ValueError:
    print("Неверный ввод. Пожалуйста, введите число 1 или 2: ")
    return
    
  keys = ['lastname', 'firstname']
  record = {}
  
  if enter_number == 1:
    record[keys[0]] = input("Введите фамилию для поиска: ")
    record[keys[1]] = input("Введите имя для поиска: ")
    
    return record
  
  else:
    print("Удаление ученика отменено!")
    return None

 # Функция выхода из программы
def exit_program():
    print('Завершение работы, вы уверены что хотите выйти?\n1. Да\n2. Нет \n')
    
    try:
        enter_number = int(input("\nПожалуйста, введите число 1 или 2: "))
        if enter_number not in range(1, 3):
            raise ValueError

    except ValueError:
        print("Неверный ввод. Пожалуйста, введите число 1 или 2: ")
        return
    
    if exit == 1:
        return 1
    else:
        print('Отмена выхода из программы')
        return None

# Функция вывода сообщения о выполнении
def display_message(message: str):
    print("\033[34m[+]\033[0m", message)
    print("--"*70)

# Функция вывода сообщения об ошибке
def display_error(message: str):
    print("\033[31m[!]\033[0m", message)
    print("--"*70)