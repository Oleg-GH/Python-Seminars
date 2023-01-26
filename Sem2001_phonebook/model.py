# path = '/home/oleg/Desktop/Python/HelloPython/Sem2001_arch1/database.txt'

db_list = []
path = 'database.txt'

def get_db_list():
    global db_list
    return db_list

def read_db(path: str) -> list:
    global db_list
    db_list = []
    my_list = ''
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            #print(line)    
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)
    return db_list
         
def save_db(path):
    global db_list
    my_list = []
    for line in db_list:
        my_str = ''
        my_str = line['lastname'] + ';' + line['firstname'] + ';' + line['phone'] + ';' + line['comment'] + ';'
        my_list.append(''.join(my_str))
    #print(*my_list)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write('\n'.join(my_list))

def search_contact(search:str):
    global db_list
    search_results=[]
    for i in range(len(db_list)):
        for v in db_list[i].values():
            if search in v:
                search_results.append(db_list[i])
                #print(*db_list[i].values())
                break
    return search_results

def change_contact(changing_cont: list, answer: str, new_contact: list):
    if 'д' in answer.lower():
        for i in range(len(changing_cont)):
            for j in range(len(db_list)):
                if changing_cont[i] == db_list[j]:
                    db_list[j] = new_contact
                    response = 'Контакт изменен'
                    break
        return response
    else:
        response = 'Контакт не изменен'
        return response

def delete_contact(removed_cont: list, answer: str):
    global db_list
    if 'д' in answer.lower():
        for i in range(len(removed_cont)):
            for j in range(len(db_list)):
                if removed_cont[i] == db_list[j]:
                    print(*removed_cont)
                    db_list.pop(j)
                    response = 'Контакт удалён'
                    break
        return response
    else:
        response = 'Удаление отменено'
        return response