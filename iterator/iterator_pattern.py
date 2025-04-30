from abc import ABC, abstractmethod
from typing import Any


class Iterator(ABC):
    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    # here could be a parser function that transform the data structure
    # to a data structure which user expect
    def next(self) -> Any:
        pass


class MenuA(Iterator):
    def __init__(self) -> None:
        self.menu_items = {}
        self.position = 0

    def get_menu_items(self):
        return self.menu_items

    def add_to_menu(self, name, description, price):
        self.menu_items[name] = {"description": description, "price": price}

    def has_next(self):
        return len(list(self.menu_items)) - 1 >= self.position

    def next(self):
        items = list(self.menu_items.items())
        item_name, info = items[self.position]
        self.position += 1
        return item_name, info


menua = MenuA()
menua.add_to_menu("pizza", "circled", 12)
menua.add_to_menu("rice", "small", 2)
menua.add_to_menu("pasta", "medium", 2.5)


while menua.has_next():
    print(menua.next())


class MenuB(Iterator):

    def __init__(self) -> None:
        self.menu_items = []
        self.position = 0

    def get_menu_items(self):
        return self.menu_items

    def add_to_menu(self, name, description, price):
        self.menu_items.append([name, description, price])

    def has_next(self) -> bool:
        return len(self.menu_items) - 1 >= self.position

    def next(self) -> Any:
        name, desc, price = self.menu_items[self.position]
        self.position += 1
        return name, desc, price


menub = MenuB()
menub.add_to_menu("tea", "hot", 3)
menub.add_to_menu("coffe", "almost hot", 5)
menub.add_to_menu("orange", "cold", 10)

while menub.has_next():
    print(menub.next())
