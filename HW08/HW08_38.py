# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и
# Вы должны реализовать функционал для изменения и удаления данных

def show_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    return book


def find_data():
    with open('data.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Введите данные для поиска: ')
        for i in book:
            if temp in i:
                print(i)


def new_data():
    with open('data.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ' + '\n'))


def delete_person(name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if name != person:
                file.write(person)


def change_person(new_name, old_name):
    persons = read_data()
    with open("data.txt", "w", encoding="utf8") as file:
        for person in persons:
            if old_name != person:
                file.write(person)
            else:
                file.write(new_name + "\n")


while True:
    mode = input('Введите номер операции со справочником:' + '\n'
                 + '0-поиск, 1-чтение файла, 2-добавление в файл, 3-удаление, 4-замена, 5-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '0':
        find_data()
    elif mode == '2':
        new_data()
    elif mode == '3':
        name = input('Введите данные для удаления: ')
        delete_person(name)
    elif mode == '4':
        old_name = input('Введите старые данные: ')
        new_name = input('Введите новые данные: ')
        change_person(new_name, old_name)
    elif mode == '5':
        break
    else:
        print('Окончание работы')






