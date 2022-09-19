# Author     :  Omar Hamed Marie
# Description:  Observer lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.
# Date       :  19 SEP 2022
# Version    :  V 1.0

class Subject(object):
    """Represents what is being 'observed'"""
    def __init__(self):
        self._observers = [] # This where references to all the observers are being kept
							 # Note that this is a one-to-many relationship: there will be one subject to be observed by multiple _observers

    def attach(self, observer):
        #If the observer is not already in the observers list
        # append the observer to the list
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers: 
            # Don't notify the observer who is actually updating the temperature 
            if observer != modifier:
               observer.update(self)

class Core(Subject): #Inherits from the Subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Initialize the temperature of the core

    @property #Getter that gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets the core temperature
    def temp(self, temp):
        self._temp = temp
        #Notify the observers whenever somebody changes the core temperature
        self.notify()

class TempViewer:
	def update(self, subject): #Alert method that is invoked when the notify() method in a concrete subject is invoked
		print("Temperature Viewer: {} has Temperature {}".format(subject._name, subject._temp))

#Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#Let's attach our observers to the first core
c1.attach(v1)
c1.attach(v2)

#Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90
