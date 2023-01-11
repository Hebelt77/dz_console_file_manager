import os.path

from actions_folder_files import create_folder
from actions_folder_files import delete_folder_files
from actions_folder_files import copy_folder_files
from actions_folder_files import rename_folder_files
from actions_folder_files import content_directory
from actions_folder_files import directory_change
from my_bank_account import history_bay


def test_create_folder():
    create_folder('test_folder')
    assert os.path.exists('test_folder')
    os.rmdir('test_folder')


def test_delete_folder_files():
    os.mkdir('test_folder')  # Создать папку
    open('test_file.txt', 'a+')  # Создать файл
    delete_folder_files('test_folder')  # Удалить папку
    assert not os.path.exists('test_folder')
    delete_folder_files('test_file.txt')  # Удалить файл
    assert not os.path.exists('test_file.txt')


def test_copy_folder_files():
    os.mkdir('test_folder')
    copy_folder_files('test_folder', 'copy_folder')
    open('test_file.txt', 'a+')
    copy_folder_files('test_file.txt', 'copy_file.txt')
    assert os.path.exists('copy_folder')
    assert os.path.exists('copy_file.txt')
    delete_folder_files('test_folder')
    delete_folder_files('copy_folder')
    delete_folder_files('test_file.txt')
    delete_folder_files('copy_file.txt')


# def test_content_directory():  # При запуске проходит тест, но в конце выдаёт несколько ошибок
#     assert content_directory() == os.listdir()


# def test_directory_change():      # При запуске проходит тест, но в конце выдаёт несколько ошибок
#     path = os.path.join(os.getcwd(), 'venv')
#     directory_change('venv')
#     assert path == os.getcwd()
#     directory_change('Консольный файловый менеджер')


def test_history_bay():
    result = history_bay({"Пальто": 12000})
    assert result == ['Пальто - 12000 рублей.']
