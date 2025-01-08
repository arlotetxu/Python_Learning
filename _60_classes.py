'''
IMPORTED METHODS
'''
from icecream import ic # To substituted print function giving more information

'''
All we create in python are objects, so they have attributes and methods.
A class in python is an object type that represents whatever you want.
Variables can be passed to a class. These variables are called "attributes".
Within the classes, it is possible to define functions (called "methods").
A class is a blueprint for python to create an object.
'''

'''
==========================CREATING A SIMPLE CLASS============================
We will create a class that represents a different sport players.
'''

class Players:
    def __init__(self) -> None:
        pass

'''
An "instance" is a call to a class to create the class object:
'''
player_1 = Players()
print("-----------Checking the instance------------")
ic(player_1) # output: ic| player_1: <__main__.Players object at 0x10413bc10>


'''
===================CREATING A SIMPLE CLASS WITH ATTRIBUTES======================
'''

class Player_info:
    def __init__(self, name:str, age:int, sport:str) -> None:
        self.name = name
        self.age = age
        self.sport = sport

    def Player_desc(self):
        print(f"{self.name} is a {self.sport} player")

    def __repr__(self) -> str:
        return f"Player_info: {self.name} - {self.sport}"


'''
The "__init__" method is mandatory as it initializes the class object when the
instance is created, but implicitly, it is also called the "__new__" method
to create the object.

The "self" in the attributes works to keep the track of the object. That means,
if you creates more than one instance, the self is who identifies all of them.
The self is basically replaced by the name of the instance.

In the same way, the "self.attribute" makes this attribute accesible by all
the methods defined in the class.
'''

if __name__ == '__main__':
    '''
    When you run a module (or class) directly, the name of the module is set to __main__.
    So, if the module is run directly, this condition is fulfilled and the code
    will be executed. On the contrary, if this module is imported by other file,
    the code below will be ignored. It is a good practice for debbuging
    purposes.
    '''
    print("----------Checking class creation with attributes----------")
    player_2 = Player_info("Rafael Nadal", 36, "Tennis") # An instance.
    player_3 = Player_info("Fernando Alonso", 42, "F1 Driver")
    player_2.Player_desc() # Calling a Class method.
    player_3.Player_desc()
    player_4 = Player_info("Arlo", 45, "Basketball").Player_desc()
    ic(id(player_2)) #As the IDs are differents, the objects are differents (self)
    ic(id(player_3))


'''
=================================INHERITANCE===================================
It is also possible create a subclass that inherits the methods and attributes
from the main class.
In this subclass you can override the attributes and
methods of the parent class just defining a new method or attribute with the
same name than the parent one.
'''

class Player_desc(Player_info): # Inherits the methods and att from Player_info Class

    def player_Physic(self, genre: str, weight: int, height: int):
        self.genre = genre
        self.weight = weight
        self.height = height

        print(f"{self.name} ({self.genre}) and is {self.weight} kg. and {self.age} years old.")
        # name attribute is comming from Player_info class

if __name__ == '__main__':
    print("--------------------Subclasses------------------")
    player_4 = Player_desc("Arlo", 44, "Basket")
    # As the attributes from parent class, the parent attributes must be passed.
    player_4.player_Physic("Male", 65, 165)
    player_4.Player_desc()


'''
===============================MAGIC METHODS==================================
The magic methods are special methods that help to control the class in a better
way. Check https://www.geeksforgeeks.org/dunder-magic-methods-python/
'''
if __name__ == '__main__':
    player_5 = Player_info("Arlo", 44, "F1")
    print("----------------MAGIC METHODS---------------")
    print(player_5) # Check the definition of def __repr__(self) in the class
