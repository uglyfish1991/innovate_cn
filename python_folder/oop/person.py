                ################################################
                #                                              #
                #                     OOP                      #
                #                                              #
                ################################################

# What is OOP? Are we not doing it already?
# The model we've followed so far is procedural programming - reading top to bottom and starting and initialising in order. OOP allows us to create a different model.

# What is an object?

# "everything" - everything is an object. A variable, a function, a list can all be classed as an object. We can make our own using classes

# The data stored in objects are referred to as attributes. 

#       Object
#    |          |
# Attribute   Methods
# What is     What it
#   has        does

#        A Car
#    |          |
# Attribute   Methods
# Colour       Start
# Weight       Stop

# A frequently used analogy to describe oop is the cookie cutter
# Classes are templates for our objects, just as cookie cutters are for cookies
# A class is the blueprint for creating a new object

# Important!!
# variables use snake_case, classes use PascalCase, JS uses camelCase

# class Person():             #keyword - Class then declare the name. 
#     def __init__(self):     # this is a "constructor" or "initialiser"
#         self.name = None    # for every object inside the person class, there will be an attribute called name

class Person():
    def __init__(self, person_name, person_age, person_height):
        self.name = person_name
        self.age = person_age
        self.height = person_height
    
    def set_hair(self, person_hair):
        self.hair = person_hair

    def get_hair(self):
        print(self.hair)
    

