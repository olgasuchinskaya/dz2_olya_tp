#2.1


import pytest
from recipe import Ingredient

class TestIngredient:

    
    def test1(self):
        ingredient = Ingredient('Мука', 500.0, 'г')
        assert ingredient.name == 'Мука'
        assert ingredient.quantity == 500.0
        assert ingredient.unit == 'г'

    
    def test2(self):
        ingredient = Ingredient('Мука', 500.0, 'г')
        assert str(ingredient) == 'Мука: 500.0 г'

    
    def test3(self):
        ingredient1 = Ingredient('Мука', 500.0, 'г')
        ingredient2 = Ingredient('Мука', 1000.0, 'г')
        assert ingredient1 == ingredient2

    
    def test4(self):
        ingredient1 = Ingredient('Мука', 500.0, 'г')
        ingredient2 = Ingredient('Рис', 500.0, 'г')
        assert ingredient1 != ingredient2

    
    def test5(self):
        ingredient1 = Ingredient('Мука', 500.0, 'г')
        ingredient2 = Ingredient('Мука', 500.0, 'кг')
        assert ingredient1 != ingredient2