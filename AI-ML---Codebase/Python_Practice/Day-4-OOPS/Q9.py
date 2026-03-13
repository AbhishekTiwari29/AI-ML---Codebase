class Herbivore:
    def eat_plants(self):
        print("eat plants")

class Carnivore:
    def eat_meat(self):
        print("eat meat")

class Omnivore:
    def eat_both(self):
        print("eat both plants and meat")

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Animal : {self.name}")

b1 = Bear("Brown Bear")

b1.show()
b1.eat_plants()
b1.eat_meat()
b1.eat_both()