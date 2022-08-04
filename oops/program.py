class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Method overriding means replacing or extending defined in base class.


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walf(self):
        print("walk")


m = Mammal()
m.eat()
m.walf()
