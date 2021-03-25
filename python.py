# Create python class inheriting from snake
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False  # polymorphism - overridden from Snake

    def climb(self):
        return "up we go"

    def swallow(self):
        return "can't be bothered to chew"

python_object = Python()

print(python_object.breathe())  # breathe() from Animal class
print(python_object.hunt())  # hunt() from Reptile class
print(python_object.scent_with_tongue())  # scent_with_tongue() from Snake class
print(python_object.climb())  # climb() from Python class
