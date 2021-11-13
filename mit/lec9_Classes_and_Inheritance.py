### IMPLEMENTING THE CLASS VS USING THE CLASS
###
### Write code from two different perspectives
###
### Implementing a new object type with a class
### - Define the class
### - Define data attributes (what is the object)
### - define methods (how to use the object)
###
### Using the new object type in code
### - create instances of the type
### - do operations with them

### CLASS DEFINITION OF AN OBJECT TYPE
### Class name is the type
### Class coordinate(object)

### Class is defined generically
### use self to refer to some instance while defining the class
### (self.x - self.y)**2
###
### self is a parameter to methods in class definition
###
### class defines data and methods common across all instances
###
### INSTANCE OF A CLASS
### instance is one specific object
### coord = Coordinate(1,2)

### data attribute values vary between instances
### c1 = Coordinate(1,2)
### c2 = Coordinate(3,4)

### c1 and c2 have different data attribute values c1.x and c2.x because they are different objects

### GETTER AND SETTER METHODS
### Getters return the values of any of the data attributes
### Setters set the data attributes to whatever is set in

class Animal(object):
    def __init__(self,age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name
    
    def set_age(self,newage):
        self.age = newage
    
    def set_name(self, newname = ""):
        self.name = newname
    
    def __str__(self):
        return "Animal:" + str(self.name) + ":" + str(self.age)