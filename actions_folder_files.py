import os
import shutil


def create_folder():  # Создание папки
    name_folder = input("Введите название папки: ")
    if os.path.exists(name_folder):  # Проверка на наличие такого имени
        print("Папка с таким именем существует!")
    else:
        os.mkdir(name_folder)


# ***Добавить удаление файла***
def delete_folder():
    name_folder = input("Введите название папки: ")
    if not os.path.exists(name_folder):  # Проверка на наличие такого имени
        print(f'''
Папки с таким именем не существует!
''')
    else:
        shutil.rmtree(name_folder, ignore_errors=True)
        # os.rmdir(name_folder)


def filter_folder_files(selection):  # Выводит список файлов или папок в зависимости от параметра ('folder/files')
    file = []
    folder = []
    content = (os.listdir(path=os.getcwd()))  # Список файлов и папок в текущей рабочей директории

    for i in content:
        if os.path.isfile(i):  # Добавить в список если является файлом
            file.append(i)
        if os.path.isdir(i):  # Добавить в список если является папкой
            folder.append(i)
    if selection == 'files':  # Возвращает список в зависимости от параметра
        return print(file)
    elif selection == 'folder':
        return print(folder)


def copy_folder_files(item, new_item):
    if os.path.isfile(item):  # Если это файл
        shutil.copy(item, new_item)  # Копирует файлы
    if os.path.isdir(item):  # Если это папка
        shutil.copytree(item, new_item)  # Копирует папки со всем содержимым присваивая им новое имя


# print(os.name)
# print(os.getcwd())
# print(os.listdir())
# os.rmdir('new')
# os.mkdir('new')

if __name__ == "__main__":
    # create_folder()
    # delete_folder()
    # print(os.path.isfile('file'))
    filter_folder_files('files')
    copy_folder_files('new_file', '1_file')
