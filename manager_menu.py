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
8. сохранить содержимое рабочей директории в файл
9. просмотр информации об операционной системе
10. создатель программы
11. играть в викторину
12. мой банковский счет
13. смена рабочей директории
14 выход.''')

    point = input('>>: ')
    if point == '1':
        name_folder = input("Введите название папки: ")
        actions_folder_files.create_folder(name_folder)

    if point == '2':
        name_folder_files = input("Введите название папки или файла: ")
        actions_folder_files.delete_folder_files(name_folder_files)

    if point == '3':
        name = input("Введите название файла или папки которую нужно скопировать: ")
        new_name = input("Введите новое название файла или папки: ")
        actions_folder_files.copy_folder_files(name, new_name)

    if point == '4':
        item = input("Введите название папки или файла для переименования: ")
        actions_folder_files.rename_folder_files()

    if point == '5':
        print(actions_folder_files.content_directory())

    if point == '6':
        print(actions_folder_files.filter_folder_files('folder'))

    if point == '7':
        print(actions_folder_files.filter_folder_files('file'))

    if point == '8':
        name = input("Введите название файла: ")
        actions_folder_files.safe_content_directory(name)

    if point == '9':
        import sys
        print(sys.platform)

    if point == '10':
        print(f'''Создатель программы: Dziuba Nikolai Sergeevich
email: hebelt@mail.ru
''')
    if point == '11':
        victory_to_manager.victory()

    if point == '12':
        my_bank_account.bank_account()

    if point == '13':
        name = input("Введите название рабочей директории: ")
        actions_folder_files.directory_change(name)

    if point == '14':
        break
