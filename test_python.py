'''

2. В модуле написать тесты для встроенных функций filter, map, sorted,
 а также для функций из библиотеки math: pi, sqrt, pow, hypot.
 Чем больше тестов на каждую функцию - тем лучше
'''
import functools
import random
from math import pi, sqrt, pow, hypot

people = ['исаак ньютон', 'альберт эйнштейн', 'никола тесла', 'томас эдисон', 'константин циолковский',
          'александр пушкин', 'вольфганг моцарт', 'людвиг бетховен', 'сергей королёв', 'юрий гагарин']

numbers_random = random.sample(list(i for i in range(100)), 100)

def test_1filter_function():
    numbers = list(i for i in range(100))
    even_num = list(filter(lambda x: True if x % 2 == 0 else False, numbers))
    for i in even_num:
        assert i % 2 == 0


def test_2filter_function():
    result = filter(lambda x: True if x.startswith('А') else False, people)
    for i in result:
        assert i[0] == 'А'


def test_3filter_function():
    result = filter(lambda x: True if x.endswith('н') else False, people)
    for i in result:
        assert i[-1] == 'н'


def test_1map_function():
    num_str = ['1', '2', '3', '4', '5', '6', '7']
    num_int = list(map(int, num_str))
    for i in num_int:
        assert isinstance(i, int)


def test_2map_function():
    title_people = map(lambda x: x.title(), people)
    for i in title_people:
        assert i.istitle()


def test_3map_function():
    upper_people = map(lambda x: x.upper(), people)
    for i in upper_people:
        assert i.isupper()





def test_sorted_function():
    numbers_sorted = sorted(numbers_random)
    for i in range(100 - 1):
        for j in range(100 - i - 1):
            assert numbers_sorted[j] < numbers_sorted[j + 1]


def test_reducer_function():
    sum_numbers = functools.reduce(lambda x, y: x + y, numbers_random)
    assert sum_numbers == sum(numbers_random)


def test_math_pi():
    num_pi = pi
    assert pi == 3.141592653589793


def test_math_sqrt():
    num = 49
    square_root = sqrt(num)
    assert square_root == 7


def test_math_pow():
    square_num = pow(14, 7)
    assert square_num == 14 ** 7


def test_math_hypot():
    hypotenuse = hypot(7, 7)
    assert hypotenuse ** 2 == 7 ** 2 + 7 ** 2
