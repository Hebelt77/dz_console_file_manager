def history_bay(buy):  # Функция собирает строки для вывода истории покупок
    thing = list(buy.keys())
    cost = list(map(lambda x: str(x) + " рублей.", buy.values()))
    history = []
    for index in range(len(thing)):
        history.append(thing[index] + ' - ' + cost[index])

    return history


def bank_account():
    buy = dict()
    check = 0
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
            for i in (history_bay(buy)):
                print(i)

        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
