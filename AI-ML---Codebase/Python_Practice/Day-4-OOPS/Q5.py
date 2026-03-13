class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats
        print(f"total seats in car {self.seats}")

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        super().__init__(brand,model)
        self.engine_cc = engine_cc
        print(f"Bike have {self.engine_cc} cc engine")

c1 = Car("Toyota","Fortuner",7)
b1 = Bike("Honda","Deluxe",100)