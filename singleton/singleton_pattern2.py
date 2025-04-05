from typing import Self


class Singleton:
    _instances = {}

    def __new__(cls) -> Self:
        if cls not in cls._instances:
            print("Creating new instance ....")
            instance = super().__new__(cls)
            cls._instances[cls] = instance

        else:
            print("Returning an existing instace")

        return cls._instances[cls]


a = Singleton()
b = Singleton()
print(a is b)
