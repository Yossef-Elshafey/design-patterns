from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, new_data):
        pass


class Subject(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class User(Subject):
    num_of_users: int
    observers: list[Observer]
    users: dict[int, str]

    def __init__(self) -> None:
        self.num_of_users = 0
        self.observers = []
        self.users = {}

    def notify_observers(self):
        id = list(self.users.keys())[-1]
        user = self.users[id]
        for observer in self.observers:
            observer.update(user)

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print("Liar you are not an observer")

    def add_user(self, id, username):
        self.users[id] = username
        self.num_of_users += 1
        self.notify_observers()


class Greet(Observer):
    def __init__(self, subject: Subject) -> None:
        subject.register_observer(self)

    def update(self, new_data):
        print(f"Sending email to {new_data}")


class RedirectToHome(Observer):
    def __init__(self, subject: Subject) -> None:
        subject.register_observer(self)

    def update(self, new_data):
        print(f"Sending that idiot {new_data} to Home")


user = User()
greet = Greet(user)
redir = RedirectToHome(user)

user.add_user(0, "Yossef")
user.add_user(1, "Mohamed")
