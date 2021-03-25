# Let's import reptile class
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.limbs = False
        self.venom = True
        self.fork_tongue = True

    def scent_with_tongue(self):
        return "I use my tongue to smell"

    def shed_skin(self):
        return "growing out"

# snake_object = Snake()
#
# print(snake_object.eat())  # eat() is inherited from the Animal class
# print(snake_object.move())  # move() is inherited from Animal class
# print(snake_object.hunt())  # hunt() is inherited from Reptile class
# print(snake_object.scent_with_tongue())  # scent_with_tongue is from current class
# Multiple inheritance
# Encapsulation?
# when hunt() definition in reptile is written as __hunt() it is not available here
