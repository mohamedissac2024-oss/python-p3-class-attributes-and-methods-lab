#!/usr/bin/env python3

class Dog:
    species = "Canis familiaris"  # class attribute

    def __init__(self, name, age):
        self.name = name          # instance attribute
        self.age = age            # instance attribute

dog1 = Dog("Buddy", 3)
dog2 = Dog("Milo", 2)

print(dog1.name)      # Buddy (instance attribute)
print(dog1.species)   # Canis familiaris (class attribute)
print(dog2.species)   # Canis familiaris (shared)
