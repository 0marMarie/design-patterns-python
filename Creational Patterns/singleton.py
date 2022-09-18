# Author     :  Omar Hamed Marie
# Description:  singleton-design-pattern
# Date       :  17 SEP 2022
# Version    :  V 1.0

class Borg:
    """The Borg design pattern"""
    # Attribute dictionary
    _shared_data = {} 
    
    def __init__(self):
        # Make it Attribute Dictionary
        self.__dict__ = self._shared_data


class Singleton(Borg): 
    """The singleton class"""
    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attricute dictionary
        self._shared_data.update(kwargs)

    def __str__(self):
        # Return attr dict for printing
        return str(self._shared_data)
   

h = Singleton(HTTP = "Hyper Text Transfer Protocol")
print(h)

s = Singleton(SNMP = "Simple Network Management Protocol")
print(s)