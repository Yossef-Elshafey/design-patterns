from abc import ABC, abstractmethod


class Drink(ABC):

    def __init__(self, description: str, money: float) -> None:
        self.description = description
        self.money = money

    def getDescription(self) -> str:
        return self.description

    @abstractmethod
    def cost(self) -> float:
        pass


class Espresso(Drink):
    def __init__(self) -> None:
        super().__init__("Espresso", 2.99)

    def cost(self):
        return self.money


class Latte(Drink):
    def __init__(self) -> None:
        super().__init__("Latte", 3.99)

    def cost(self) -> float:
        return self.money


class DrinkDecorator(Drink):
    @abstractmethod
    def getDescription(self) -> str:
        pass


class WithMilk(DrinkDecorator):

    def __init__(self, drink: Drink) -> None:
        self.drink = drink

    def getDescription(self) -> str:
        return self.drink.getDescription() + "," + "Milk"

    def cost(self) -> float:
        return self.drink.cost() + 0.50


class WithSugar(DrinkDecorator):

    def __init__(self, drink: Drink) -> None:
        self.drink = drink

    def getDescription(self) -> str:
        return self.drink.getDescription() + "," + "Sugar"

    def cost(self) -> float:
        return self.drink.cost() + 0.25


espresso = Espresso()
espresso = WithMilk(espresso)
espresso = WithSugar(espresso)
espresso = WithSugar(espresso)

print(espresso.getDescription())
print(espresso.cost())

latte = Latte()
latte = WithSugar(latte)
latte = WithMilk(latte)
latte = WithMilk(latte)
print(latte.getDescription())
print(latte.cost())
