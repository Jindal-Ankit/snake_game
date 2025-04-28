class Animal:
    eyees_1 = 2
    def __init__(self):
        self.eyes = 2
        self.legs = 4

    def breath(self):
        print("Inhale, Exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        print("You are creating a fish.")



animal = Animal()
animal.eyees_1 = 5
print(f"Eyes : {animal.eyes} {animal.eyees_1}")
animal.breath()


fish = Fish()
print(f"Eyes : {fish.eyees_1}")
fish.breath()
