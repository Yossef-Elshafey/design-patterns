from abc import ABC, abstractmethod


class QuackStrategy(ABC):
    @abstractmethod
    def quack(self):
        pass


class LongQuack(QuackStrategy):
    def quack(self):
        print("QUAAAAAAAAACK")


class SmallQuack(QuackStrategy):
    def quack(self):
        print("quack")


class MediumQuack(QuackStrategy):
    def quack(self):
        print("Quaaack")


class Duck:
    def __init__(self, quack_strategy: QuackStrategy) -> None:
        self.quack_strategy = quack_strategy

    def set_quack_strategy(self, quack_strategy):
        self.quack_strategy = quack_strategy

    def quack(self):
        self.quack_strategy.quack()

    def display(self):
        print("Im a Duck")

    def swim(self):
        print("Duck is swimming")

    def fly(self):
        print("Duck is flying")


d = Duck(LongQuack())
d.quack()
d.set_quack_strategy(SmallQuack())
d.quack()
