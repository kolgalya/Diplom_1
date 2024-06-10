from praktikum.burger import Burger
from unittest.mock import Mock, patch

class TestBurger:
    def test_bun_of_burger_true(self):
        burger = Burger()  # создание нового экземпляра класса
        assert burger.bun == None  # проверка корректности значения булок в созданном экземпляре

    def test_ingredients_of_burger_true(self):
        burger = Burger()  # создание нового экземпляра класса
        assert burger.ingredients == []  # проверка корректности значения ингридиентов в созданном экземпляре

    def test_set_buns_true(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_true(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient_true(self):
        burger = Burger()
        burger.ingredients = [{'SAUCE', 'Что-то', 150},{'FILLING', 'Ингридиент_2', 500},{'SAUCE', 'Что-то_2', 250}]
        burger.remove_ingredient(len(burger.ingredients)-1)
        assert burger.ingredients == [{'SAUCE', 'Что-то', 150},{'FILLING', 'Ингридиент_2', 500}]

    def test_move_first_ingredient_to_end_true(self):
        burger = Burger()
        burger.ingredients = [['SAUCE', 'Что-то', 150], ['FILLING', 'Ингридиент_2', 500], ['SAUCE', 'Что-то_2', 250]]
        burger.move_ingredient(0, len(burger.ingredients) - 1)  #1 элемент ставим в конец
        assert burger.ingredients == [['FILLING', 'Ингридиент_2', 500], ['SAUCE', 'Что-то_2', 250], ['SAUCE', 'Что-то', 150]]

    def test_get_price_true(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 200
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 150
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert burger.get_price() == 550

    @patch('praktikum.burger.Burger.get_price', return_value = 680) #мок на метод получения цены в бургерах
    def test_get_receipt_true(self, mock_price):
        mock_bun = Mock()
        mock_bun.get_name.return_value = 'bun_1'
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = 'SAUCE'
        mock_ingredient.get_name.return_value = 'Ингридиент_2'
        burger = Burger()
        burger.bun = mock_bun
        burger.ingredients = [mock_ingredient]
        assert 'Price: 680' in burger.get_receipt()
