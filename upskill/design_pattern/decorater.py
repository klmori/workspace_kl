# 	Add features/behavior dynamically
# Add milk/sugar to coffee


class Coffee:
    def cost(self):
        return 50

class CoffeeDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def cost(self):
        return self.coffee.cost()

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 10

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 5

# Usage
basic_coffee = Coffee()
c = MilkDecorator(basic_coffee)
c = SugarDecorator(c)

print("Total cost:", c.cost())  # Output: 65
