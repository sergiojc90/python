### OBJECT ORIENTED PROGRAMMING
### 
### Python objects supports many different kinds of data
###
### each is an object, and every object has:
### - a type
### - an internal data representation
### - a set of procedures for interaction with the object
### 
### - an object is an instance of a type
### 1234 is an intance of an int
### "hello" is an instance of a string
###
### EVERYTHING IN PYTHON IS AN OBJECT
###
### You can create, manipulate and destroy objects (using del or just forgetting about them)
###
### Objects are a DATA ABSTRACTION
### 1) An internal representation through data attributes
### 2) An interface for interactiong with object
### - through methods
### - defines behaviors but hides implementation
###
### CREATING AND USING YOUR OWN TYPES WITH CLASSES
### 
### Make distinction between CREATING A CLASS and USING INSTANCE OF THE CLASS
###
### Creating the class involves
### - Defining the class name
### - Defining class atributes
### - for example, someone wrote code to implement a list class
###
### Using the class involves
### - Creating new instances of objects
### - Doing operations on the instances
### - for example, L=[1,2] and len(L)
###
### DEFINE YOUR OWN TYPES
### - Use the class keyword to define a new type
###
### class Coordinate(object):
###     #define attributes here
###
### - similar to def, indent code to indicate which statements are part of the class definition
### - the word object means that Coordinate is a python object and inherits all its attributes (inheritance next lecture)
### - Coordinate is a subclass of OBJECT
### - OBJECT is a superclasss of Coordinate
###
### WHAT ARE ATTRIBUTES?
###
### Data and procedures that "belong" to the class
### 
### Data attributes
### - think of data as other object that make up the class
### - for example, a coordinate is made up of two numbers
###
### Methods (procedural attributes)
### - Think of methods as functions that only work with this class
### - How to interact with the object