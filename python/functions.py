#!/usr/bin/python
# Writing functions in python

# Simple function to print a greeting
def greet_user(): # define a function
    """Display a simple greeting."""
    print('Hello') # Body of the function

greet_user()

# Passing information to a function
def greet_users(username): # username is a parameter
    """Display a greeting for a user"""
    print('Hello, '+username.title())

greet_users('Nik') # Nik in this case is an argument

# Passing arguments

    # Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print('\nI have a '+ animal_type + ".")
    print('My '         + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster','harry')

    # Multiple Function Calls
describe_pet('Dog','Ava') # Order matters, 1st animal type then name

# Keyword arguments
# Name-value pair that you pass to a function
describe_pet(animal_type='Cat', pet_name='Jim')

pet_name = 'Nik'
# Equivalent Function Calls
def describe_pet(pet_name, animal_type = 'dog')





