import model
import view

def start():
    path = 'database.txt'
    user_input = 0
    while user_input < 7:
        user_input = view.main_menu()
        match user_input:
            case 1:
                # открыть файл
                model.read_db(path) 
                view.db_success(model.db_list)                

            case 2:   
                # показать все контакты
                view.show_all(model.db_list)

            case 3:
                # найти контакт
                search = view.search_request()
                result = model.search_contact(search)
                view.show_all(result)                

            case 4:
                # создать контакт
                model.db_list.append(view.create_contact())  
                # сохранить изм-я в БД
                model.save_db(path)
                view.save_success() 

            case 5:
                # изменить контакт
                search = view.search_request()
                result = model.search_contact(search)
                confirm = view.confirm_changes(result)
                if 'н' not in confirm:
                    new_contact = view.create_contact()
                response = model.change_contact(result,confirm,new_contact)
                view.change_success(response)
                # сохранить изм-я в БД
                model.save_db(path)
                view.save_success() 

            case 6:
                # удалить контакт
                search = view.search_request()
                result = model.search_contact(search)
                confirm = view.confirm_changes(result)
                response = model.delete_contact(result,confirm)
                view.delete_success(response)
                # сохранить изм-я в БД
                model.save_db(path)
                view.save_success() 

            # case 7:                       # это меню удалено как излишнее,
            #     # сохранить изм-я в БД    # функционал перенесен в пункты
            #     model.save_db(path)       # меню 4 (создать конт.), 5 (изменить конт.),
            #     view.save_success()       # 6 (удалить контакт) для немедленного
                                            # исполнения этих пунктов. Иначе можно 
                                            # просто забыть сохранить изменения
    else:
        # выход
        view.exit_program()    

          