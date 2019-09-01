#!/usr/bin/python
# Making an object from a class is called instantiation 
# and you work with instances for a class

class Dog():
    #A simple attempt to model a dog
    def __init__(self, name, age):  # the __init__() method in Python creates a new instance
        self.name = name
        self.age = age

    def sit(self):
    #Simulate a dog sitting in respone to a command
        print(self.name.title() + "is now sitting.") # Any variable with the prefix self 
                                                     # is available to every method in the class
    
    def roll_over(self):
    # Simulate rolling over in response to a command.
        print(self.name.title() + "rolled over")

# Invoking the class
my_dog = Dog('Ava',6) # Create a dog whose name is age is 6, and save the instance in my_dog
print("My dog's name is " + my_dog.name.title() +".")
print("My dog is " + str(my_dog.age) + " years old." )

