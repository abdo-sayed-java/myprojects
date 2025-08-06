# 1
class vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def start_engine (self):
        return "Engine Started"
    
    def describe (self):
        return f"{self.name} moves at {self.speed} km/h"

vehicle1 = vehicle("Car called BMW" ,120)
print(vehicle1.start_engine())
print(vehicle1.describe())

# 2
class car (vehicle):
    def __init__(self, name, speed, brand):
        super().__init__(name, speed)
        self.brand = brand

    def describe(self):
        return f"\n{super().describe()} its brand is {self.brand}\n"
    

x = car("Matrix", 120, "Hyundai")
print(x.describe())
print(x.describe())

# 3 
class electric_car (car):
    def __init__(self, name, speed, brand, battery_range):
        super().__init__(name, speed, brand)
        self.battery_range = battery_range
    
    def start_engine(self):
        return "Electric motor activated!"
    
electric_car1 = electric_car("Tesla 1", 220, "Tesla", "350 KM to 450 KM")
print(electric_car1.start_engine())

# 4 
class bicycle (vehicle):
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def start_engine(self):
        return "Start walking"
    
    def describe(self):
        return f"{super().describe()}"

bicycle1 = bicycle("Strong", 30)
print(bicycle1.start_engine())
print(bicycle1.describe())