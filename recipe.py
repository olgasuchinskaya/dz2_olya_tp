#1.1

class Ingredient:
    
    def __init__(self, name, quantity, unit):
        self.name = name
        self.unit = unit
        self.quantity = quantity

    
    @property
    def quantity(self):
        return self._quantity

    
    @quantity.setter
    def quantity(self, x):
        if x <=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(x)
        
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"

    
    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"

    
    def __eq__(self, x):
        return self.name == x.name and self.unit == x.unit


#1.2

class Recipe:
    
    def __init__(self, title, ingredients):
        self.title = title
        self.ingredients = ingredients

    
    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)


    @staticmethod
    def is_valid_ratio(ratio):
        return ratio >0


    def scale(self, ratio):
        if self.is_valid_ratio(ratio):
            a = []
            for i in self.ingredients:
                new_quantity = i.quantity * ratio
                new = Ingredient(i.name, new_quantity, i.unit)
                a.append(new)
            return Recipe(self.title, a)
        else:
            raise ValueError("Коэффициент должен быть положительным")
    
    def __len__(self):
        return len(set(self.ingredients))

    
    def __str__(self):
        return f"{self.title}: {', '.join(str(i) for i in self.ingredients)}"


#1.3

class ShoppingList:

    def __init__(self):
        self._items = []

    
    def add_recipe(self, recipe, portions):
        if portions <=0:
            raise ValueError("Количество порций должно быть положительным")
        
        new = recipe.scale(portions)
        
        for ingredient in new.ingredients:
            self._items.append((ingredient, recipe.title))

    
    def remove_recipe(self, title):
        new = []
        for i in self._items:
            if i[1] != title:
                new.append(i)
        self._items = new


    def get_list(self):
        
        d = {}
        for ingredient, title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in d:
                d[key] += ingredient.quantity
            else:
                d[key] = ingredient.quantity
        
        result = []
        for key, quantity in d.items():
            name = key[0]
            unit = key[1]
            result.append(Ingredient(name, quantity, unit))
        
        result.sort(key=lambda x: x.name)
        return result


    def __add__(self, other):
        new = ShoppingList()
        new._items = self._items + other._items
        return new



#1.4

class DietaryRecipe(Recipe):
    
    def __init__(self, title, diet_type, ingredients=None):
        if ingredients is None:
            ingredients =[]
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    
    def scale(self, ratio):
        new = super().scale(ratio)
        return DietaryRecipe(new.title, self.diet_type, new.ingredients)

    
    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"

