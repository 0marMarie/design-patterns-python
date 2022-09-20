# Author     :  Omar Hamed Marie
# Description:  Iterator lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).
# Date       :  19 SEP 2022
# Version    :  V 1.0

def count_to(count):
    """Our iterator implementation"""
	
	#Our list
    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

	#Our built-in iterator
	#Creates a tuple such as (1, "eins")
    iterator = zip(range(count), numbers_in_german)
	
	# 1. Iterate through our iterable list
	# 2. Extract the German numbers
	# 3. Put them in a generator called number
    for position, number in iterator:
        yield number #Returns a 'generator' containing numbers in German


#Let's test the generator returned by our iterator
for num in count_to(3):
    print(num)
