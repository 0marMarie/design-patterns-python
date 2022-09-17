# Author     :  Omar Hamed Marie
# Description:  abstract-factory-design-pattern
# Date       :  17 SEP 2022
# Version    :  V 1.0

class Dog:

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """ Concrete Product 1
            @returns: Dog object
        """
        return Dog()


    def get_food(self):
        """ Concrete Product 2
            @returns: Dog Food object
        """
        return "Dog Food Object!"


class PetStore:
    """PetStore houses our Abstract Factory"""

    def __init__(self, pet_factory=None):
        """Pet factory is our abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """Utility method to display details of objects reterned by concrete factory"""
        pet      = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Our pet is {pet}")
        print(f"Our pet says {pet.speak()}")
        print(f"Our pet food is {pet_food}")


# Create a conrete Factory
concrete_factory = DogFactory()

# Create a Pet store housing our abstract factory
pet_store = PetStore(concrete_factory)

# Show Details
pet_store.show_pet()