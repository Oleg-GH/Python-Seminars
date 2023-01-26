
def main_menu() -> int:   # получаем пункт меню
    print('Главное меню:')
    menu_list = ['Начать работу(считать БД)',
                'Показать все контакты',
                'Найти контакт',
                'Создать контакт',
                'Изменить контакт',
                'Удалить контакт',
                #'Сохранить изменения в БД',
                'Выход (любой символ, кроме 1-6)'
                ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    while True:
        try:    
            user_input = int(input('Введи пункт меню от 1 до 7 (иначе программа закроется) :> '))
            if user_input > 7 or user_input < 1:
                user_input = 7            
            break
        except  ValueError:
            #print('Неверный формат.')
            user_input = 7
            break
        # except Exception:
        #     print('Необходимо ввести число от 1 до 7.')
    return user_input

def show_all(db: list):  # просмотр контактов
    if db_success(db):
        #print('Телефонная книга пуста')
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}',  end=' ')
            print()

def db_success(db: list): # проверка наличия записей  
    if db:
        print('Телефонная книга открыта')  
        return True 
    else:
        print('Телефонная книга пустая или не открыта')
        return False   

def exit_program():     # выход из программы
    print('Завершение программы.')
    exit()             

def create_contact():
    print('Создание нового контакта')
    new_contact = dict()
    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = str(input('\tВведите телефон >: '))
    new_contact['comment'] = input('\tВведите комментарий >: ')
    return new_contact

def search_request():
    return input('Введите поисковый запрос, нажмите Enter: ')

def save_success():
    print('Файл сохранен')

def change_success(response):
    print(response)   

def delete_success(response):
    print(response)

def confirm_changes(changing_cont: list):
    if len(changing_cont)>0:
        for item in changing_cont:
            print(*item)
    else:
        print('Нет такого контакта в тел. книге.')
        return 'н'
    return input('Подтвердите изменение...(д/н): ')     
