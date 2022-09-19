# Author     :  Omar Hamed Marie
# Description:  builder-design-pattern
# Date       :  19 SEP 2022
# Version    :  V 1.0

class Director():
    """Director -> What Actually Builds a product (Car)"""
    def __init__(self, builder):
        """@param _builder: is where the concrete builder object is store"""
        self._builder = builder 
        
    def construct_car(self):
        self._builder.create_new_car()
        self._builder.add_model()
        self._builder.add_tires()
        self._builder.add_engine()
        
    def get_car(self):
        return self._builder.car
        
        
class Builder():
    """Abstract Builder"""
    def __init__(self):
        self.car = None 
        
    def create_new_car(self):
        self.car = Car()
        

class SkyLarkBuilder(Builder):
    """Concrete Builder --> provides parts and tools to work on the parts """
    
    def add_model(self):
        self.car.model = "Skylark"

    def add_tires(self):
        self.car.tires = "Regular tires"

    def add_engine(self):
        self.car.engine = "Car Turbo Engine"


class Car():
    """Product"""
    def __init__(self):
        self.model = None
        self.tires = None
        self.engine = None
        
    def __str__(self):
        return '{} | {} | {}'.format(self.model, self.tires, self.engine)



# 1. Create a concrete builder
builder = SkyLarkBuilder() 

# 2. Dicrector takes the concrete builder and puts it to work
director = Director(builder)

# 3. Construct our car
director.construct_car()

# 4. The director gets a refrence to the car instance
car = director.get_car()

# Print the car
print (car)