"""create a module, define about 5 functions or classes, create 
variables that hold lists, dictionaries, use arithmetic
functions and operators in your modules. 
Now create another file where you import your module and 
use some of the methods in it."""

#Module definition
#functions
def add(m,n):
    return m + n

def subtract(m, n):
    return m - n

def multiply(m, n):
    return m * n

def divide(m, n):
    if n == 0:
        return "Error: Division by zero"
    return m / n


#classes

class Animal:
    # a simple class representing animal
    def __init__(self, animal_type, animal_colour,):
        self.animal_type= animal_type
        self.animal_colour = animal_colour
        
    def pet(self):
        print(f'my pets type is a, {self.animal_type} and its has a  {self.animal_colour} colour.')
    

    #variables
    #list
animal_list = ["dog", "cat", "lion", "elephant"]
    
    
    #dictionary
my_dict ={
    "dog": "canine",
    "cat": "feline",
    "lion": "carnivore", 
    "elephant": "mammal"
}


