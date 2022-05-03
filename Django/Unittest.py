"""Пример"""
import unittest
from file import series_sum  # Импорт тестируемой функции


class TestSeriesSum(unittest.TestCase):
    """Тестируем series_sum."""
    def test_mixed_numbers(self):  # Это - test case
        # Вызов тестируемой функции
        call = series_sum([1, 2.5, 3, 4])
        # Ожидаемый результат
        result = '12.534'
        # Проверка: идентичен ли результат вызова ожидаемому результату
        self.assertEqual(call, result,
                         'Функция series_sum() не работает '
                         'со списком чисел')

    def test_mixed_numbers_strings(self):  # И это - test case
        call = series_sum([1, 'fff', 3, 4])
        result = '1fff34'
        self.assertEqual(call, result,
                         'Функция series_sum не работает со смешанным списком')

    def test_empty(self):  # И это - тоже test case
        call = series_sum([])
        result = ''
        self.assertEqual(call, result,
                         'Функция series_sum не работает с пустым списком')

if __name__ == '__main__':
    unittest.main()


"""Методы"""
assertEqual(a, b)	a == b
assertNotEqual(a, b)	a != b
assertTrue(x)	bool(x) is True
assertFalse(x)	bool(x) is False
assertIs(a, b)	a is b
assertIsNot(a, b)	a is not b
assertIsNone(x)	x is None
assertIsNotNone(x)	x is not None
assertIn(a, b)	a in b
assertNotIn(a, b)	a not in b
assertIsInstance(a, b)	isinstance(a, b)
assertNotIsInstance(a, b)	not isinstance(a, b)


"""В Python есть несколько популярных библиотек для тестирования."""
nose2
pytest
unittest  # стандартная библиотека Python


"""Создание фикстур."""
import unittest


def setUpModule():
    """Вызывается один раз перед всеми классами, которые есть в файле."""
    print('> setUpModule')


def tearDownModule():
    """Вызывается один раз после всех классов, которые есть в файле."""
    print('> tearDownModule')


class TestExample(unittest.TestCase):
    """Демонстрирует принцип работы тестов."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        print('>> setUpClass')

    @classmethod
    def tearDownClass(cls):
        """Вызывается один раз после запуска всех тестов класса."""
        print('>> tearDownClass')

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        print('>>> setUp')

    def tearDown(self):
        """Вызывается после каждого теста."""
        print('>>> tearDown')

    def test_one(self): # это -- test case 
        print('>>>> test_simple')

    def test_one_more(self): # это -- еще один test case
        print('>>>> test_simple')


if __name__ == '__main__':
    unittest.main()

#########################################
# если проверить ожидамое значение невозможно, потому что
# действие невозможнос само себе. Как с делением на ноль: 

# функция
def square(self, num):
    """Возвращает квадратный корень аргумента."""       
    if num < 0:
        raise ValueError('Не могу извлечь корень из отрицательного числа')
    return num ** 0.5 

########
# обработка ошибки в тесте

def test_square_negative_value(self):
    with self.assertRaises(ValueError):
        TestCalc.calc.square(-1) 