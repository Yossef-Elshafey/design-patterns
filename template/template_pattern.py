from abc import abstractmethod


class CaffineBeverage:

    def boil_water(self):
        print("Boiling water")

    def prepare_ingredients(self):
        print("Preparing ingredients")

    @abstractmethod
    def drink_caffine(self):
        pass

    @abstractmethod
    def brew(self):
        pass

    def prepare(self):
        self.boil_water()
        self.prepare_ingredients()
        self.brew()
        self.drink_caffine()


class Tea(CaffineBeverage):
    def drink_caffine(self):
        print("Preparing Tea")

    def brew(self):
        print("Brew Tea")


class Coffe(CaffineBeverage):

    def drink_caffine(self):
        print("Preparing Coffe")

    def brew(self):
        print("Brew Coffe")


c = Coffe()
c.prepare()
t = Tea()
t.prepare()
