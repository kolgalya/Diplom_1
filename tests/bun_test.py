import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', ['Странная булка', '', 'B', '@#', 13, 58.695, None, True, 'Очень длинное имя булки тттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттттт'])
    def test_name_of_bun_true(self, name):
        bun = Bun(name, 50)  # создание нового экземпляра класса
        assert bun.name == name  # проверка корректности имени в созданном экземпляре

    @pytest.mark.parametrize('price', [500, 0, -85695, 99999999999999999999999999999999999999999999999999999999999, 9856.8, 986/5, '859', None, False])
    def test_price_of_bun_true(self, price):
        bun = Bun('Чудная булка', price)  # создание нового экземпляра класса
        assert bun.price == price  # проверка корректности цены в созданном экземпляре

    def test_get_name_of_bun_true(self):
        bun = Bun('Крутая булка', 500)  # создание нового экземпляра класса
        name = bun.get_name() # получили имя
        assert name == 'Крутая булка'  # проверка корректности имени

    def test_get_price_of_bun_true(self):
        bun = Bun('Улетная булка', 5000)  # создание нового экземпляра класса
        price = bun.get_price() # получили цену
        assert price == 5000  # проверка корректности цены