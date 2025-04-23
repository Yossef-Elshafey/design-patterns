from abc import abstractmethod


class Duck:
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Turkey:
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Im a duck QUACKING")

    def fly(self):
        print("Im a duck FLYING")


class WildTurkey(Turkey):
    def gobble(self):
        print("Turkey Gobble")

    def fly(self):
        print("Im flying a short distance")


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


def test_duck(duck: Duck):
    # two different instances same methods diffrenet behaviors
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)

    print("The duck says...")
    test_duck(duck)

    print("The TurkeyAdapter says...")
    test_duck(turkey_adapter)
