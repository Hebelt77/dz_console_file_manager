import os.path

from actions_folder_files import create_folder, delete_folder_files, copy_folder_files, safe_content_directory
from actions_folder_files import rename_folder_files
from actions_folder_files import content_directory
from actions_folder_files import directory_change
from my_bank_account import history_buy, load_unload_file
from victory_to_manager import random_people


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


def test_random_people():
    assert len(random_people()) == 5
    assert len(random_people()) == len(set(random_people()))


# def test_content_directory():  # При запуске проходит тест, но в конце выдаёт несколько ошибок
#     assert content_directory() == os.listdir()


# def test_directory_change():      # При запуске проходит тест, но в конце выдаёт несколько ошибок
#     path = os.path.join(os.getcwd(), 'venv')
#     directory_change('venv')
#     assert path == os.getcwd()
#     directory_change('Консольный файловый менеджер')


def test_history_buy():
    result = history_buy({"Пальто": 12000})
    assert result == ['1.) Пальто - 12000 рублей.']


def test_load_unload_file():
    file = 'test file.txt'
    test_buy = {"Пальто": 12000}
    load_unload_file(file, test_buy, 'w')
    assert os.path.exists(file)
    assert load_unload_file(file, test_buy, 'r') == test_buy
    delete_folder_files(file)


def test_safe_content_directory():
    safe_content_directory('testdir.txt')
    assert os.path.exists('testdir.txt')
    delete_folder_files('testdir.txt')

