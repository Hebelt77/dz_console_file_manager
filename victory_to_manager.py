import locale
import datetime as DT

locale.setlocale(locale.LC_ALL, 'ru')


def random_people():
    people = ["Исаак Ньютон", "Альберт Эйнштейн", "Никола Тесла", "Томас Эдисон", "Константин Циолковский",
              "Александр Пушкин", "Вольфганг Моцарт", "Людвиг Бетховен", "Сергей Королёв", "Юрий Гагарин"]

    year_of_birth = ["04.01.1643", "14.03.1879", "10.07.1856", "11.02.1847", "17.09.1857",
                     "06.06.1799", "27.01.1756", "17.12.1770", "12.01.1907", "09.03.1934"]

    people_birth = [(k, year_of_birth[i]) for i, k in enumerate(people)]
    import random
    result = random.sample(people_birth, 5)
    return result




def victory():

    while True:

        result = random_people()
        total_true = 0
        total_false = 0

        for name, date in result:
            answer = input(f"Введите дату рождения {name} в формате 'dd.mm.yyyy': ")
            if answer == date:
                total_true += 1
            else:
                total_false += 1
                date = DT.datetime.strptime(date, '%d.%m.%Y').date()
                print(f"Неверно!, Правильный ответ: {date.strftime('%d %B %Y года')}")

        print(f"""    Количество правильных ответов: {total_true}
    Количество неправильных ответов: {total_false}""")
        end = (input("Хотите начать заново?: 'Да/Нет': ")).lower()
        if end == 'нет':
            break


if __name__ == '__main__':
    import random
    victory()
