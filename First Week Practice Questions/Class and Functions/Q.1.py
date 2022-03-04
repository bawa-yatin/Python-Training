# Create a child class Bus that will inherit all the variables and methods
# of the Vehicle class

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "Public Transport", "180", "15")

    def msgDisplay(self):
        print("This is the bus class!")


b = Bus()
print("Vehicle Name:", b.name)
print("Vehicle Speed:", b.max_speed)
print("Vehicle Mileage:", b.mileage)
b.msgDisplay()
