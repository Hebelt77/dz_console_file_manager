import actions_folder_files
import victory_to_manager

print("Добро пожаловать в файловый менеджер")
while True:
    print(f'''Выберите необходимое действие из меню:

1. создать папку
2. удалить (файл/папку)
3. копировать (файл/папку)
4. просмотр содержимого рабочей директории
5. посмотреть только папки
6. посмотреть только файлы
7. просмотр информации об операционной системе
8. создатель программы
9. играть в викторину
10. мой банковский счет
11. смена рабочей директории (*необязательный пункт)
12 выход.''')

    point = input('>>: ')
    if point == '1':
        actions_folder_files.create_folder()

    if point == '2':
        actions_folder_files.delete_folder()

    if point == '3':
        name = input("Введите название файла или папки которую нужно скопировать: ")
        new_name = input("Введите новое название файла или папки: ")
        actions_folder_files.copy_folder_files(name, new_name)

    if point == '4':
        import os
        print(os.listdir(path=os.getcwd()))

    if point == '5':
        actions_folder_files.filter_folder_files('folder')

    if point == '6':
        actions_folder_files.filter_folder_files('file')

    if point == '7':
        import sys
        print(sys.platform)

    if point == '8':
        pass
    if point == '9':
        victory_to_manager.victory()

    if point == '10':
        pass
    if point == '11':
        pass
    if point == '12':
        break
