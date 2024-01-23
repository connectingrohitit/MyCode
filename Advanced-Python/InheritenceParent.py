class Car:
    def __init__(self, windows, doors, engine_type):
        self.windows = windows
        self.doors = doors
        self.engineType = engine_type

    def drive(self):
        print("This is a manual driven car.")
