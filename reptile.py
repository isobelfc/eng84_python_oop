# Let's import Animal class
# Best practices are to use a new file for each class to make debugging easier

# "from animal" works because they're in the same project
# if animal file was elsewhere we would need to give the path
from animal import Animal

class Reptile(Animal):  # we need to pass the Animal class as an arg in our Reptile class

    def __init__(self):
        super().__init__()  # super is to make everything available from parent class
        self.cold_blooded = True
        self.tetrapod = True
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "working hard to catch the next meal"

    def use_venom(self):
        return "I use venom"

    def seek_heat(self):
        return "looking for sunshine"

# # Let's see some benefits of inheritance
# reptile_object = Reptile()
# print(reptile_object.hunt())
# print(reptile_object.breathe())
# # we have access to the methods in both the Reptile and Animal classes
