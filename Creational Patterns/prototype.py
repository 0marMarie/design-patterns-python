# Author     :  Omar Hamed Marie
# Description:  Prototype lets you copy existing objects without making your code dependent on their classes.
# Date       :  19 SEP 2022
# Version    :  V 1.0

import copy

class Prototype:
    
    def __init__(self):
        """Creates dictionary object to obtain the objects to be cloned"""
        self._objects = {}

    def register_object(self, name, obj):
        """
            Register an object

            @param name: name as a key to be stored in dictionary object
            @param obj : object to be cloned 
        """
        self._objects[name] = obj
        
        
    def unregister_object(self, name):
        """
            Unregister an object -> Delete objects from dictionary object
            
            @param name: key used to delete a registered obj
        """
        del self._objects[name]
        
    def clone(self, name, **attr):
        """
            Clone a registered object and update its attributes

            @param name: a key used to get the object
            @param attr: optional parameter to update the object
            @return: the updated obj
        """
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj
        
class Car:
    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"
        
    def __str__(self):
        return '{} | {} | {}'.format(self.name, self.color, self.options)
        

# Institiate the car class - prototypical obj to be cloned
c = Car()

# Create an instance of prototype class
prototype = Prototype()

# Register our prototypical obj
prototype.register_object("skylark", c)

# Clone the prototypical obj
c1 = prototype.clone("skylark")

# Print
print(c1)


