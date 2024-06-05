import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('type', ['SAUCE', 'FILLING', 'какой-то тип', 1589, None, False])
    def test_type_of_ingredient_true(self, type):
        ingredient = Ingredient(type, 'Просто мазик', 100)  # создание нового экземпляра класса
        assert ingredient.type == type  # проверка корректности типа в созданном экземпляре

    @pytest.mark.parametrize('name', ['Кетченез', '', 'GYHNMGbhhgvn','какое-то длинное имя ИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИИ', 1589, None, False])
    def test_name_of_ingredient_true(self, name):
        ingredient = Ingredient('SAUCE', name, 150)  # создание нового экземпляра класса
        assert ingredient.name == name  # проверка корректности имени в созданном экземпляре

    @pytest.mark.parametrize('price', [1589, 0, -58621, 8655/5, 9865.854, 'строка', None, False])
    def test_price_of_ingredient_true(self, price):
        ingredient = Ingredient('FILLING', 'Чурчхелла', price)  # создание нового экземпляра класса
        assert ingredient.price == price  # проверка корректности цены в созданном экземпляре

    def test_get_price_of_ingredient_true(self):
        ingredient = Ingredient('SAUCE', 'Золотая пыль', 1050)  # создание нового экземпляра класса
        price = ingredient.get_price() # получили цену
        assert price == 1050  # проверка корректности цены

    def test_get_name_of_ingredient_true(self):
        ingredient = Ingredient('FILLING', 'Летающие хвостики', 2000)  # создание нового экземпляра класса
        print(ingredient)
        name = ingredient.get_name() # получили имя
        assert name == 'Летающие хвостики'  # проверка корректности имени

    def test_get_type_of_ingredient_true(self):
        ingredient = Ingredient('FILLING', 'Неизвестность', 30000)  # создание нового экземпляра класса
        type = ingredient.get_type() # получили имя
        assert type == 'FILLING'  # проверка корректности имени