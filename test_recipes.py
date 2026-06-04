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





#2.3

class TestShoppingList:


    def test1(self):
        ingredients = [Ingredient('Мука', 800.0, 'г'), Ingredient('Сахар', 200.0, 'г')]
        recipe = Recipe('Блины', ingredients)
        shopping = ShoppingList()
        shopping.add_recipe(recipe, 2)
        assert len(shopping._items) == 2
        assert shopping._items[0][1] == 'Блины'
        assert shopping._items[1][1] == 'Блины'


    def test2(self):
        ingredients = [Ingredient('Мука', 500.0, 'г')]
        recipe = Recipe('Блины', ingredients)
        shopping = ShoppingList()
        with pytest.raises(ValueError):
            shopping.add_recipe(recipe, 0)
        with pytest.raises(ValueError):
            shopping.add_recipe(recipe, -100)


    def test3(self):
        ingredients1 = [Ingredient('Мука', 300.0, 'г')]
        ingredients2 = [Ingredient('Сахар', 700.0, 'г')]
        recipe1 = Recipe('Блины', ingredients1)
        recipe2 = Recipe('Ватрушка', ingredients2)
        shopping = ShoppingList()
        shopping.add_recipe(recipe1, 1)
        shopping.add_recipe(recipe2, 1)
        assert len(shopping._items) == 2
        shopping.remove_recipe('Блины')
        assert len(shopping._items) == 1
        assert shopping._items[0][1] == 'Ватрушка'


    def test4(self):
        ingredients = [Ingredient('Мука', 500.0, 'г')]
        recipe = Recipe('Блины', ingredients)
        shopping = ShoppingList()
        shopping.add_recipe(recipe, 1)
        shopping.remove_recipe('Какойторецепт')
        assert len(shopping._items) == 1


    def test5(self):
        ingredients1 = [Ingredient('Мука', 500.0, 'г')]
        ingredients2 = [Ingredient('Мука', 400.0, 'г')]
        recipe1 = Recipe('Блины', ingredients1)
        recipe2 = Recipe('Пирог', ingredients2)
        shopping = ShoppingList()
        shopping.add_recipe(recipe1, 1)
        shopping.add_recipe(recipe2, 1)
        result = shopping.get_list()
        assert len(result) == 1
        assert result[0].name == 'Мука'
        assert result[0].quantity == 900.0


    def test6(self):
        ingredients1 = [Ingredient('Сахар', 200.0, 'г')]
        ingredients2 = [Ingredient('Мука', 500.0, 'г')]
        ingredients3 = [Ingredient('Яйца', 3.0, 'шт')]
        recipe1 = Recipe('Блины', ingredients1)
        recipe2 = Recipe('Ватрушка', ingredients2)
        recipe3 = Recipe('Омлет', ingredients3)
        shopping = ShoppingList()
        shopping.add_recipe(recipe1, 1)
        shopping.add_recipe(recipe2, 1)
        shopping.add_recipe(recipe3, 1)
        result = shopping.get_list()
        assert result[0].name == 'Мука'
        assert result[1].name == 'Сахар'
        assert result[2].name == 'Яйца'


    def test7(self):
        ingredients1 = [Ingredient('Мука', 500.0, 'г')]
        ingredients2 = [Ingredient('Сахар', 200.0, 'г')]
        recipe1 = Recipe('Блины', ingredients1)
        recipe2 = Recipe('Ватрушка', ingredients2)
        shopping1 = ShoppingList()
        shopping2 = ShoppingList()
        shopping1.add_recipe(recipe1, 1)
        shopping2.add_recipe(recipe2, 1)
        combined = shopping1 + shopping2
        assert len(combined._items) == 2
        assert combined._items[0][1] == 'Блины'
        assert combined._items[1][1] == 'Ватрушка'


    def test8(self):
        ingredients = [Ingredient('Мука', 500.0, 'г')]
        recipe = Recipe('Блины', ingredients)
        shopping1 = ShoppingList()
        shopping2 = ShoppingList()
        shopping1.add_recipe(recipe, 1)
        shopping2.add_recipe(recipe, 1)
        original1_len = len(shopping1._items)
        original2_len = len(shopping2._items)
        combined = shopping1 + shopping2
        assert len(shopping1._items) == original1_len
        assert len(shopping2._items) == original2_len
        