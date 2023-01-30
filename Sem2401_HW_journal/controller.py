from os import system


import model
import view


menu_journal_choise = [" Выберите класс: "]
menu_subject_choise = [" Выберите предмет: "]
menu_learner_choise = [" Выберите действие: "]

def main():
    # system("cls")  # Уже очищена
    menu_journal_choise.extend( model.journals_list() )
    command = view.input_command( menu_journal_choise )
    if command == 0:
         view.close(); return
    model.journal_open( menu_journal_choise[ command ] )

    system("cls")
    # Журнал выбран, список предметов загружен
    menu_subject_choise.extend( model.subjects )
    command = view.input_command( menu_subject_choise )
    if command == 0:
         view.close(); return

    model.subject_open( menu_subject_choise[ command ] )

    # Выбран предмет, список учеников загружен
    menu_learner_choise.extend([ 
        "Поставить ученику оценку", 
        "Исправить поставленную оценку",
        "Заменить или поставить новыю оценку",
        "Добавить нового ученика (вводим только 4)",
        "Удалить ученика с предмета)",
        "Изменить имя ученика" ])
    while True:
        system("cls")
        # Доступные действия
        command, learner_name = view.input_lerner_command( menu_learner_choise, model.journal[ model.subject_name ] )

        # Выход
        if command == 0:
            view.close(); return

        # Добавить оценку
        if command == 1:
            view.show_learner_and_mark( learner_name, model.journal[ model.subject_name ][ learner_name ] )
            # Запрос оценки
            mark = view.mark_input()
            model.mark_add( learner_name, mark )

        # Удалить оценку
        elif command == 2:
            view.show_learner_and_mark( learner_name, model.journal[ model.subject_name ][ learner_name ] )
            # Запрос оценки
            model.mark_del( learner_name, view.mark_input() )

        # Заменить или Добавить оценку
        elif command == 3:
            view.show_learner_and_mark( learner_name, model.journal[ model.subject_name ][ learner_name ] )
            # Запрос оценки
            model.mark_upd( learner_name, view.mark_input() )

        # Добавить ученика
        elif command == 4:
            # Запрос имени
            model.learner_add( view.learner_input() )

        # Удалить ученика
        elif command == 5:
            # Запрос имени
            model.learner_del( learner_name )

        # Изменить ученика
        elif command == 6:
            learner_edit( learner_name, view.learner_input() )



