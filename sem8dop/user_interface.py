from logger import *

def intrface():
    print("""'1 - записать данные, 
          2 - вывести данные'
          3 - удалить запись 
          4 - изменить запись""")
    var = (input(' введите номер варианта: '))
    while var not in ('1','2' ,'3','4' ):
        print('не верно')
        var = (input(' введите номер варианта: '))
    if var == '1':
        input_data() 
    if var == '2':
        print_data()
    if var == '3':
        name = (input('кого удаляем?: '))
        delete_line(name)
    if var == '4':
        old_name = input('кого хотим переименовать?: ')
        new_name = input('как хотим его назвать?: ')
        change_person(new_name,old_name)