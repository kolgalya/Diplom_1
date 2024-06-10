from praktikum.database import Database
from unittest.mock import Mock

class TestDatabase:
    def test_buns_of_database_true(self):
        database = Database()
        assert len(database.buns) == 3

    def test_ingredients_of_database_true(self):
        database = Database()
        assert len(database.ingredients) == 6

    def test_available_buns_true(self):
        mock_buns = Mock()
        database = Database()
        database.buns = mock_buns
        assert database.available_buns() == mock_buns

    def test_available_ingredients_true(self):
        mock_ingredients = Mock()
        database = Database()
        database.ingredients = mock_ingredients
        assert database.available_ingredients() == mock_ingredients