import view
import model


def start():
    path = 'database.txt'                                # /str/
    user_input = 0
    while user_input < 9:
        user_input = view.main_menu()       # вводится номер требуемого пункта меню /int/
        match user_input:
            # ниже перечень функционала для учителя
            case 1:
                # считать файл с БД (открыть файл)
                # model.read_school_db(path)              # inp. /str/    ex. /list/
                # school_db = model.get_school_db()       # inp.          ex. /list/
                # view.db_success(school_db)              # inp. /list/   ex. /bool/                
                school = ['5a', '5b']
                ind = view.school_read(school)
                clas = model.open_jurnal(f'{school[ind]}')
                print(list(clas.keys())[0])
                subj_index = view.school_read(list(clas.keys()))
                view.school_read(clas[list(clas.keys())[0]]['students'])
                subj_index = view.school_read(clas[list(clas.keys())[0]]['students'][0]["grades"])
                print(subj_index)
                

            case 2:
                # открыть БД по определенному классу и конкретному предмету
                view.show_pupils(klass, subject)        # inp. /str, str/    ex. /dict - ?/

            case 3:
                # найти (вызвать) ученика
                search = view.search_request()          #               ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
                view.show_pupil(result)                 # inp. /str/    ex. /list - ?/

            case 4:
                # поставить ученику оценку
                search = view.search_request()          #               ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /dict - ?/
                model.mark_put(result, mark)            # inp. /dict, str/  ex.
                view.mark_success()                     # inp.          ex. /str/ 'Оценка внесена в журнал'

            case 5:
                # добавить ученика
                new_pupil = view.create_pupil()         # inp.          ex. /dict -?/
                model.school_db.append(new_pupil)       # inp. /dict/   ex. /list/

            case 6:
                # изменить ученика
                search = view.search_request()          # inp.          ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /list/
                confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/   y/n
                if 'n' not in confirm:
                    new_pupil = view.create_pupil()     # inp.          ex. /dict/          
                response = model.change_pupil(result,confirm,new_pupil) # inp. /list, str, list/    ex. /str/
                view.change_success(response)           # inp. /str/

            case 7:
                # удалить ученика
                search = view.search_request()          # inp.          ex. /str/
                result = model.search_pupil(search)     # inp. /str/    ex. /list/
                confirm = view.confirm_changes(result)  # inp. /list/   ex. /str/  y/n
                response = model.delete_contact(result,confirm) # inp. /list, str/ ex. /str/
                view.delete_success(response)           # inp. /str/    ex. /str/ 'Ученик удален'

            case 8:
                # сохранить класс в файл с БД
                model.save_db(path)                     # inp. /str/    ex. updated file
                view.save_success()                     # inp.          ex. /str/ 'Файл сохранен'

    else:
        view.close()                                    # inp.          ex. /str/ 'Завершение программы'