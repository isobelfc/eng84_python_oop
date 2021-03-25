# Let's create our first class
# Syntax class is the keyword then name of the class

# # To bypass the code without putting data in
# class Animal():
#     pass  # pass is the keyword to bypass

# Creating an Animal class
class Animal():

    # name = "Dog"  # class variable

    def __init__(self):  # self refers to the current class
        self.alive = True  # Attributes / variables
        self.spine = True
        self.lungs = True

    def move(self):
        return "moving left right and centre"

    def eat(self):
        return "keep eating to stay alive"

    def breathe(self):
        return "keep breathing if you want to live"

# Creating an object of our Animal class
# cat = Animal()  # this will store all the data available in Animal class into cat
#
# print(cat.eat())  # ABSTRACTION of eat() method

# Let's move on to INHERITANCE
