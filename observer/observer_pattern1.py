from abc import ABC, abstractmethod
import random
import time


# Observer pattern book example


class Observer(ABC):
    """
    Creating interface for each observer.

    Update method is the function get called,
    when there is a notifying action has to be taken
    """

    @abstractmethod
    def update(self, temp, humidity):
        pass


# This class sometime called (Subject, Publisher, Topic)
class Subject(ABC):
    """
    Creating interface for Subject.

    @registerObserver(observer) -> store all passed observers that want to be notified
    @remove_observer(observer) -> find the observer who want to be removed
    @notify_observers -> tells all the observers that something changed
    """

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
    """
    Each time WeatherStation gets a new measurements,
    all the observers want to know that information.

    So it implements the Subject interface (ABC class).

    measurements_changed -> function gets called to update the values,
                            fire a notify_observers action
    """

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
    """
    Implements Observer interface.
    Display the current conditions for each change(update) immeditaly.

    displayCurrent -> handling the data as it should be handled depends on the logic
    """

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
    """
    Implements Observer interface.
    Display the current conditions for each change(update) immeditaly.

    displayCurrent -> handling the data as it should be handled depends on the logic
    """

    temp_history: dict[str, int]
    humidity_history: dict[str, int]

    def __init__(self, weather_station: WeatherStation):
        weather_station.registerObserver(self)
        self.temp_history = {}
        self.humidity_history = {}

    def update(self, temp, humidity):
        result = time.gmtime()
        string_time = time.strftime("%Y:%m:%d:%H:%M:%S", result)
        self.temp_history[string_time] = temp
        self.humidity_history[string_time] = humidity

    def display_previous_weather_data(self):
        print("Temp History")
        print(self.temp_history)
        print("-" * 20)
        print("Humidity History")
        print(self.humidity_history)


# Subject
ws = WeatherStation()

# Each observer needs the Subject in the object construction
ccd = CurrentConditionsDisplay(ws)
forecast = Forecasting(ws)

# Sending random numbers every second to the Subject
# Watching other observers gets notified
for i in range(5):
    temp = random.randint(0, 10)
    humidity = random.randint(100, 200)
    ws.measurements_changed(temp, humidity)
    ccd.displayCurrent()
    time.sleep(1)


# see all the previous measurement data
forecast.display_previous_weather_data()
