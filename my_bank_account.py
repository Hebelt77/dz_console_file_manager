import json
import os.path


def history_buy(buy):  # Функция собирает строки для вывода истории покупок
    thing = list(buy.keys())
    cost = list(map(lambda x: str(x) + " рублей.", buy.values()))
    history = []

    for index, item in enumerate(thing):
        history.append(str(index + 1) + '.) ' + item + ' - ' + cost[index])

    return history


def load_unload_file(file, data, mode):  # Загружает/выгружает файл и кодирует/восстанавливает его из формата json
    if os.path.exists(file):  # Если он существует
        if mode == 'r':
            with open(file, 'r') as f:
                return json.load(f)

    if mode == 'w':
        with open(file, 'w') as f:
            return json.dump(data, f)

    else:  # Если файла не существует
        return data  # То возвращает значение переменной обратно


def bank_account():
    buy = dict()
    history = 'history buy.txt'

    check = 0
    balance = 'account balance.txt'

    buy = load_unload_file(history, buy, 'r')  # Записываем результаты загрузки файлов в переменные
    check = load_unload_file(balance, check, 'r')   # Если файлов не существует, возвращает значения переменных

    while True:
        print(f"На вашем счету {check} рублей")
        print(f'''Выберите пункт меню:
    1. Пополнение счёта
    2. Покупка
    3. История покупок
    4. Выход''')

        choice = input('>>: ')
        if choice == '1':
            try:
                check += int(input("На какую сумму хотите пополнить счёт?: "))
            except:
                print("Введите числовое значение!")
                continue
            # print(f"На вашем счету {check} рублей.")

        elif choice == '2':
            try:
                price = int(input("Введите стоимость покупки: "))
            except:
                print("Введите числовое значение!")
                continue
            if price > check:
                print("На счёте не хватает средств, пополните баланс.")
            elif price <= check:
                name_buy = input("Введите название покупки: ")
                check -= price
                buy[name_buy] = price

        elif choice == '3':
            print("<<Список ваших покупок>>")
            for i in (history_buy(buy)):
                print(i)

        elif choice == '4':
            load_unload_file(history, buy, 'w')  # Записываем из buy в файл history  историю покупок
            load_unload_file(balance, check, 'w')  # Записываем из check в файл balance состояние счёта

            # with open('account balance.txt', 'w') as f:
            #     json.dump(check, f)  # Записываем  состояние балланса в строковом типе
            #
            # with open('history buy.txt', 'w') as f:  # Открываем файл в режиме записи
            #     json.dump(buy, f)  # Записываем в файл данные из словаря

            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    buy = {'a': 1000, 'b': 4000}
    bay = {'a': 1000, 'b': 4000}
    with open('history bay.txt', 'w') as f:  # Открываем файл в режиме записи
        json.dump(buy, f)  # Кодируем данные в формат json и записываем в файл

    # with open('history bay.txt', 'a') as f:  # Открываем файл в режиме дозаписи
    #     json.dump(bay, f)  # Кодируем новые данные в формат json и дозаписываем в файл

    with open('history bay.txt', 'r') as f:
        result = json.load(f)
        print(type(result), result)

    # with open('person.json', 'r') as f:
    #     result = json.load(f)
    #     print(result)
