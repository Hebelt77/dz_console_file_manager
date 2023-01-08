import os
import shutil


def create_folder():  # Создание папки
    name_folder = input("Введите название папки: ")
    if os.path.exists(name_folder):  # Проверка на наличие такого имени
        print("Папка с таким именем существует!")
    else:
        os.mkdir(name_folder)


def delete_folder_files():  # Удаляет файл или папку со всем её содержимым
    name_item = input("Введите название папки или файла: ")
    if not os.path.exists(name_item):  # Проверка на наличие такого имени
        print(f'''
Папки или файла с таким именем не существует!
''')
    elif os.path.isfile(name_item):
        os.remove(name_item)
    else:
        shutil.rmtree(name_item, ignore_errors=True)
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
        return print(file)
    elif selection == 'folder':
        return print(folder)


def copy_folder_files(item, new_item):  # Копирует файл или папку item присваивая новое имя new_item
    if os.path.isfile(item):  # Если это файл
        shutil.copy(item, new_item)  # Копирует файлы
    if os.path.isdir(item):  # Если это папка
        shutil.copytree(item, new_item)  # Копирует папки item со всем содержимым присваивая им новое имя new_item


def directory_change():  # Смена рабочей директории
    name = input("Введите название рабочей директории: ")
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
    print(os.listdir(path=os.getcwd()))


def rename_folder_files():  # Переименовывает папку или файл
    item = input("Введите название папки или файла для переименования: ")
    if os.path.exists(item):  # Проверка на наличие такого имени
        new_item = input("Введите новое название папки или файла: ")
        os.rename(item, new_item)  # Присвоение нового имени
    else:
        print("Папка или файл с таким именем не найдены!")


if __name__ == "__main__":
    # print(os.name)
    # print(os.listdir())
    # os.rmdir('new')
    # os.mkdir('new')
    # os.remove('file') #
    # create_folder()
    # delete_folder_files()
    # print(os.path.isfile('file'))
    # content = (os.listdir(path=os.getcwd()))  # Список файлов и папок в текущей рабочей директории

    # copy_folder_files('new_file', '1_file')
    # print(os.listdir(path='folder'))    # Список папок и файлов в конкретной директории
    # os.chdir('folder')  # Смена рабочей директории
    # print(os.getcwd())  # Текущая рабочая деректория
    # filter_folder_files('file')
    rename_folder_files()
    # print(os.path.join(os.path.abspath(os.path.dirname('first_folder')), 'first folder'))
    # path = os.path.join(os.path.abspath(os.path.dirname(item)), item) # Возвращает путь к директории по имени папки или файла
