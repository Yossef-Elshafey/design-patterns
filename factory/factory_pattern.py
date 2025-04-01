from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


class CheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = "CheesePizza"

    def prepare(self):
        print(f"Preparing {self.name}")

    def bake(self):
        print(f"Baking {self.name}")

    def cut(self):
        print(f"Cutting {self.name}")

    def box(self):
        print(f"Boxing {self.name}")


class ChickenPizza(Pizza):
    def __init__(self) -> None:
        self.name = "ChickenPizza"

    def prepare(self):
        print(f"Preparing {self.name}")

    def bake(self):
        print(f"Baking {self.name}")

    def cut(self):
        print(f"Cutting {self.name}")

    def box(self):
        print(f"Boxing {self.name}")


class PizzaStore(ABC):

    def orderPizza(self, name: str) -> Pizza:
        pizza = self.createPizza(name)
        if pizza is None:
            print(f"Sorry, {name} is not available in our menu.")
            return None

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        print("-" * 30)
        return pizza

    @abstractmethod
    def createPizza(self, name: str) -> Pizza:
        pass


class SimplePizzaStore(PizzaStore):

    def createPizza(self, name: str) -> Pizza:
        if name == "CheesePizza":
            return CheesePizza()
        elif name == "ChickenPizza":
            return ChickenPizza()
        return None


pizza_store = SimplePizzaStore()

cheese_pizza = pizza_store.orderPizza("CheesePizza")
chicken_Pizza = pizza_store.orderPizza("ChickenPizza")
chicken_Pizza = pizza_store.orderPizza("ChickenPizza")

invalid_pizza = pizza_store.orderPizza("PepperoniPizza")
