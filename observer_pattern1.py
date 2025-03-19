from abc import ABC, abstractmethod
import random
import time


class Observer(ABC):
    @abstractmethod
    def update(self, temp, humidity):
        pass


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer: Observer):
        pass

    @abstractmethod
    def remove_observer(self, observer: Observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class WeatherStation(Subject):
    observers: list[Observer]
    humidity: int
    temp: int

    def __init__(self) -> None:
        self.observers = []
        self.humidity = 0
        self.temp = 0

    def registerObserver(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
        else:
            print(f"{observer.__str__} is not an observer idiot")

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temp, self.humidity)

    def measurements_changed(self, temp, humidity):
        self.humidity = humidity
        self.temp = temp
        self.notify_observers()


class CurrentConditionsDisplay(Observer):
    temp: int
    humidity: int

    def __init__(self, weather_station: WeatherStation):
        weather_station.registerObserver(self)
        self.temp = 0
        self.humidity = 0

    def update(self, temp, humidity):
        self.temp = temp
        self.humidity = humidity

    def displayCurrent(self):
        print("Current Temp", self.temp)
        print("Current Humidity", self.humidity)


class Forecasting(Observer):

    temp_history: dict[str, int]
    humidity_history: dict[str, int]

    def __init__(self, weather_station: WeatherStation):
        weather_station.registerObserver(self)
        self.temp_history = {}
        self.humidity_history = {}

    def update(self, temp, humidity):

        result = time.gmtime()
        string_time = time.strftime("%M:%S", result)
        self.temp_history[string_time] = temp
        self.humidity_history[string_time] = humidity

    def display_forecasting_data(self):
        print(self.temp_history)
        print(self.humidity_history)


ws = WeatherStation()
ccd = CurrentConditionsDisplay(ws)
forecast = Forecasting(ws)
for i in range(20):
    temp = random.randint(0, 10)
    humidity = random.randint(100, 200)
    ws.measurements_changed(temp, humidity)
    ccd.displayCurrent()
    forecast.display_forecasting_data()
    time.sleep(1)
