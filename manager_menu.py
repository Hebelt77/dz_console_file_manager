import actions_folder_files
import my_bank_account
import victory_to_manager

print("Добро пожаловать в файловый менеджер")
while True:
    print(f'''
Выберите необходимое действие из меню:

1. создать папку
2. удалить (файл/папку)
3. копировать (файл/папку)
4. переименовать (файл/папку)
5. просмотр содержимого рабочей директории
6. посмотреть только папки
7. посмотреть только файлы
8. просмотр информации об операционной системе
9. создатель программы
10. играть в викторину
11. мой банковский счет
12. смена рабочей директории
13 выход.''')

    point = input('>>: ')
    if point == '1':
        actions_folder_files.create_folder()

    if point == '2':
        actions_folder_files.delete_folder_files()

    if point == '3':
        name = input("Введите название файла или папки которую нужно скопировать: ")
        new_name = input("Введите новое название файла или папки: ")
        actions_folder_files.copy_folder_files(name, new_name)

    if point == '4':
        actions_folder_files.rename_folder_files()

    if point == '5':
        actions_folder_files.content_directory()

    if point == '6':
        actions_folder_files.filter_folder_files('folder')

    if point == '7':
        actions_folder_files.filter_folder_files('file')

    if point == '8':
        import sys
        print(sys.platform)

    if point == '9':
        print(f'''Создатель программы: Dziuba Nikolai Sergeevich
email: hebelt@mail.ru
''')
    if point == '10':
        victory_to_manager.victory()

    if point == '11':
        my_bank_account.bank_account()

    if point == '12':
        actions_folder_files.directory_change()

    if point == '13':
        break
