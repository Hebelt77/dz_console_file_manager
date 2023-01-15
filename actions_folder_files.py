import json
import os
import shutil


def create_folder(name):  # Создание папки
    if os.path.exists(name):  # Проверка на наличие такого имени
        print("Папка с таким именем существует!")
    else:
        os.mkdir(name)


def delete_folder_files(name):  # Удаляет файл или папку со всем её содержимым
    if not os.path.exists(name):  # Проверка на наличие такого имени
        print(f'''
Папки или файла с таким именем не существует!
''')
    elif os.path.isfile(name):
        os.remove(name)
    else:
        shutil.rmtree(name, ignore_errors=True)
        # os.rmdir(name_folder)


def filter_folder_files(selection):  # Выводит список файлов или папок в зависимости от параметра 'folder/files'
    file = []
    folder = []
    content = os.listdir()

    for i in content:
        if os.path.isfile(i):  # Добавить в список если является файлом
            file.append(i)
        if os.path.isdir(i):  # Добавить в список если является папкой
            folder.append(i)
    if selection == 'file':  # Возвращает список в зависимости от параметра
        return file
    elif selection == 'folder':
        return folder


def copy_folder_files(item, new_item):  # Копирует файл или папку item присваивая новое имя new_item
    if os.path.isfile(item):  # Если это файл
        shutil.copy(item, new_item)  # Копирует файлы
    if os.path.isdir(item):  # Если это папка
        shutil.copytree(item, new_item)  # Копирует папки item со всем содержимым присваивая им новое имя new_item


def directory_change(name):  # Смена рабочей директории
    if not os.path.exists(name):
        print("Папки с таким именем не существует!")
    else:
        os.chdir(name)
    print("Вы находитесь в этой директории ↓↓↓")
    print(os.getcwd())


def content_directory():  # Выводит содержимое рабочей директории
    print("Вы находитесь в этой директории ↓↓↓")
    print(os.getcwd())
    print("Содержимое этой директории ↓↓↓")
    return os.listdir(path=os.getcwd())


def rename_folder_files():  # Переименовывает папку или файл
    item = input("Введите название папки или файла для переименования: ")
    if os.path.exists(item):  # Проверка на наличие такого имени
        new_item = input("Введите новое название папки или файла: ")
        os.rename(item, new_item)  # Присвоение нового имени
    else:
        print("Папка или файл с таким именем не найдены!")


def safe_content_directory(name):       # Сохраняет содержимое рабочей директории в указанный файл
    files = filter_folder_files('file')  # Функция возвращает список файлов
    folders = filter_folder_files('folder')  # Функция возвращает список папок
    str_files = 'files: ' + ', '.join(files)  # Собираем строки, сохраняем в переменные
    str_folders = 'dirs: ' + ', '.join(folders)
    with open(name, 'w') as f:  # Записываем строки в файл
        f.write(f'{str_files} \n')
        f.write(str_folders)

#   json.dump((f'{str_files} \n{str_folders}'), f)   # Вариант с переводом строк в формат json
#   with open('listdir.txt', 'r') as f:              # Позволяет восстанавливать данные в первоначальный вид
#        print(json.load(f))                         # но вид содержимого файла менее читабелен!


if __name__ == "__main__":
    safe_content_directory('listdir.txt')
    # print(os.name)
    # print(os.listdir())
    # os.rmdir('new')       # Удаляет пустую папку
    # os.mkdir('new')       # Создаёт пустую папку
    # os.remove('file')     # Удаляет файл
    # create_folder()
    # delete_folder_files()
    # print(os.path.isfile('file'))
    # content = (os.listdir(path=os.getcwd()))  # Список файлов и папок в текущей рабочей директории

    # copy_folder_files('new_file', '1_file')
    # print(os.listdir(path='folder'))    # Список папок и файлов в конкретной директории
    # os.chdir('folder')  # Смена рабочей директории
    # print(os.getcwd())  # Текущая рабочая деректория
    filter_folder_files('file')
    # rename_folder_files()
    # print(os.path.join(os.path.abspath(os.path.dirname('first_folder')), 'first folder'))
    # path = os.path.join(os.path.abspath(os.path.dirname(item)), item) # Возвращает путь к директории по имени папки или файла
