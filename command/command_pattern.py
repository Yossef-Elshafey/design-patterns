from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Light:
    def __init__(self, location) -> None:
        self.location = location

    def on(self):
        print(f"Turn lights on for {self.location}")

    def off(self):
        print(f"Turn lights off for {self.location}")


class LightOnCommand(Command):
    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class NoCommand(Command):
    def execute(self):
        pass

    def undo(self):
        pass


class RemoteControl:
    def __init__(self, slots) -> None:
        self.on_command = [NoCommand()] * slots
        self.off_command = [NoCommand()] * slots
        self.undo_command = NoCommand()

    def set_command(self, slot, on_command, off_command):
        self.on_command[slot] = on_command
        self.off_command[slot] = off_command

    def on_button_pushed(self, slot):
        self.on_command[slot].execute()
        self.undo_command = self.on_command[slot]

    def off_button_pushed(self, slot):
        self.off_command[slot].execute()
        self.undo_command = self.off_command[slot]

    def undo_button_pushed(self):
        self.undo_command.undo()


if __name__ == "__main__":
    remote_control = RemoteControl(slots=10)

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)

    remote_control.on_button_pushed(0)
    remote_control.off_button_pushed(0)
    remote_control.undo_button_pushed()

    remote_control.on_button_pushed(1)
    remote_control.off_button_pushed(1)
    remote_control.undo_button_pushed()
