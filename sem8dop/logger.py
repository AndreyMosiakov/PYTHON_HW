from data_create import *

def input_data():
    name = name_data()
    lastname =lastname_data()
    phone = phone_data()
    adress = adress_data()

    var = (input(f'''формат ввода данных? '
                    1 вариант:
                    {name},
                    {lastname},
                    {phone},
                    {adress}
                    2 вариант:
                    {name};{lastname};{phone};{adress}
                    введите номер варианта: '''))
    while var not in ('1','2'):
        print('не верно')
        var = (input(' введите номер варианта: '))
    if var == '1':
        with open('phonebook.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n{lastname}\n{phone}\n{adress}\n\n') 
    else:
          with open('phonebook.txt', 'a', encoding='utf-8') as file:
            file.write(f'{name} ; {lastname} ; {phone} ; {adress}\n\n')

def print_data():
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        phonebook = data.read()
        print(phonebook)
        return phonebook        

def delete_line(name):
    with open('phonebook.txt', "w", encoding="utf8" ) as file:
        persons = file.read()
        for person in persons:
            if name != person:
                file.write(person)

def change_person(new_name, old_name):
     with open('phonebook.txt', "w", encoding="utf8" ) as file:
        persons = file.read()
        for person in persons:
            if  old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")
              




input_data()
print_data()        