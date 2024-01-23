# child class
from InheritenceParent import Car


class Audi(Car):
    def __init__(self, windows, doors, engine_type, ai_enabled):
        super().__init__(windows, doors, engine_type)
        self.aiEnabled = ai_enabled

    def self_driven(self):
        if self.aiEnabled:
            print("This is a Self Driven Audi Car")
        else:
            super().drive()


audi1 = Audi(5, 6, 'Diesel', False)
print(audi1.self_driven())
