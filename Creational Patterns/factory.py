# Author     :  Omar Hamed Marie
# Description:  factory-design-pattern
# Date       :  17 SEP 2022
# Version    :  V 1.0

class Dog:

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Woof!"

class Cat:

    def __init__(self, name):
        self._name = name
    
    def speak(self):
        return "Meow!"

def get_pet(pet="dog"):
    """Factory Method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Lucy"))
    return pets[pet]

d = get_pet("dog")
print(d.speak())

c = get_pet("cat")
print(c.speak())