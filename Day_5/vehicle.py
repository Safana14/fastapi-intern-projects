class Vehicle:
    def __init__(self, make, model, speed=0):
        self.make = make
        self.model = model
        self.speed = speed

    def accelerate(self, amount):
        self.speed += amount

    def get_info(self):
        return f"{self.make} {self.model} - Speed: {self.speed} km/h"


v1 = Vehicle("Toyota", "Corolla")

v1.accelerate(30)

print(v1.get_info())

class Car(Vehicle):
    def __init__(self, make, model, num_doors, speed=0):
        super().__init__(make, model, speed)
        self.num_doors = num_doors

    def get_info(self):
        return (
            f"Car: {self.make} {self.model} | "
            f"Doors: {self.num_doors} | "
            f"Speed: {self.speed} km/h"
        )
    
class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity, speed=0):
        super().__init__(make, model, speed)
        self.payload_capacity = payload_capacity

    def get_info(self):
        return (
            f"Truck: {self.make} {self.model} | "
            f"Payload: {self.payload_capacity} tons | "
            f"Speed: {self.speed} km/h"
        )
    
car = Car("Honda", "City", 4)

truck = Truck("Tata", "Signa", 20)

print(car.get_info())
print(truck.get_info())