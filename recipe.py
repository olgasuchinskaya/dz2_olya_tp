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


