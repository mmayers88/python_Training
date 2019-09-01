#!/usr/bin/python
import sys

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles[1].title()) # This will capitalize it
print(bicycles[-1].title()) # This will capitalize it and show the last item

# Using individual values from a list
message = "My first bicycle was a" + bicycles[0].title() + "."
print(message)

# Modifying Elements in a List
motorcyles = ['honda','yamaha','suzuki']
print(motorcyles)

motorcyles[0] = 'ducati'
print(motorcyles)

# Append Elements
motorcyles.append('ducati')
print(motorcyles)

# Append dynamically
motorcyles = []
motorcyles.append('Honda')
motorcyles.append('Yamaha')
motorcyles.append('suzuki')
print(motorcyles)

# Insert Elements into A list
motorcyles.insert(0,'Ducati')
print(motorcyles)

# Removing Elements from a list
del motorcyles[0] # Removing the first element
print(motorcyles)

# The pop method / First IN First OUT 
popped_motorcyles = motorcyles.pop()
print(motorcyles)
print(popped_motorcyles)
print("The last  motorcyle I owened was a " + popped_motorcyles.title() + ".")

first_owned = motorcyles.pop(0)
print ('The first bike is '+ first_owned.title() + '.')

motorcyles = ['honda','yamaha','suzuki']
motorcyles.remove('honda')
print(motorcyles)

# Using the sort() Method
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)




