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



#2.2


class TestRecipe:

    
    def test1(self):
        ingredients = [Ingredient('Мука', 500.0, 'г'), Ingredient('Сахар', 200.0, 'г')]
        recipe = Recipe('Блины', ingredients)
        assert recipe.title == 'Блины'
        assert recipe.ingredients == ingredients


    def test2(self):
        recipe = Recipe('Салат', [])
        ingredient = Ingredient('Томат', 2, 'шт')
        recipe.add_ingredient(ingredient)
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0] == ingredient


    def test3(self):
        ingredient1 = Ingredient('Мука', 200.0, 'г')
        ingredient2 = Ingredient('Мука', 400.0, 'г')
        recipe = Recipe('Пирог', [ingredient1])
        recipe.add_ingredient(ingredient2)
        assert len(recipe.ingredients) == 1
        assert recipe.ingredients[0].quantity == 600.0


    def test4(self):
        ingredients = [Ingredient('Мука', 500.0, 'г')]
        original = Recipe('Блины', ingredients)
        scaled = original.scale(3)
        assert scaled is not original
        assert original.ingredients[0].quantity == 500.0
        assert scaled.ingredients[0].quantity == 1500.0


    def test5(self):
        ingredients = [
            Ingredient('Мука', 500.0, 'г'),
            Ingredient('Сахар', 200.0, 'г'),
            Ingredient('Молоко', 100.0, 'мл')
        ]
        recipe = Recipe('Блины', ingredients)
        scaled = recipe.scale(2)
        assert scaled.ingredients[0].quantity == 1000.0
        assert scaled.ingredients[1].quantity == 400.0
        assert scaled.ingredients[2].quantity == 200.0

    
    def test6(self):
        recipe = Recipe('Блины', [])
        with pytest.raises(ValueError):
            recipe.scale(0)
        with pytest.raises(ValueError):
            recipe.scale(-100)

    
    def test7(self):
        ingredients = [
            Ingredient('Мука', 600.0, 'г'),
            Ingredient('Мука', 700.0, 'г'),
            Ingredient('Сахар', 800.0, 'г')
        ]
        recipe = Recipe('Блины', ingredients)
        assert len(recipe) == 2