from abc import ABC, abstractmethod


class SubSystem(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass


class DVDPlayer(SubSystem):
    def on(self):
        print("Dvd Player... Fire!")

    def off(self):
        print("Dvd Player ... off")


class Monitor(SubSystem):
    def on(self):
        print("Monitor... Fire!")

    def off(self):
        print("Monitor ... off")


class Projector(SubSystem):
    def on(self):
        print("Projector... Fire!")

    def off(self):
        print("Projector ... off")


class HomeTheaterFacade:
    def __init__(self, dvd: DVDPlayer, monitor: Monitor, projector: Projector) -> None:
        self.dvd = dvd
        self.monitor = monitor
        self.projector = projector

    def watchMovie(self):
        self.dvd.on()
        self.monitor.on()
        self.projector.on()

    def endMovie(self):
        self.dvd.off()
        self.monitor.off()
        self.projector.off()


dvd = DVDPlayer()
monitor = Monitor()
projector = Projector()

theater = HomeTheaterFacade(dvd, monitor, projector)
theater.watchMovie()
theater.endMovie()
