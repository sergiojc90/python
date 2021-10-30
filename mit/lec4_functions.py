#######################
## Create Structure with Decomposition
## Divide Code into modules
## - Sefl-contained
## - Break up the code
## - Reusable
## - Organized
## - Keep code coherent
##
## In this lecture, achive decomposition with FUNCTIONS
## Decomposition can also be achived with CLASES
#######################
## Supress details with abstraction
## Inputs, type of inputs, what it does, output
#######################
## Functions (Hat1 - Create the function, Hat2 - User of the function)
## Reusable pieces/chunks of code
## Functions are not fun in a program until they are "called" of "invoked" in a program
## function characteristics:
## has a name
## has parameteres (0 or more)
## has a docstring (optional but recomended)
## has a body
## RETURNS something
##
## FUNCTION DEFINITION
##
## def is_even( i ):
## """
## Input: i, a positive int
## Returns True if i is even, otherwhise False
## """
## print("inside is_even")
## return i%2 == 0
##
## FUNCTION CALL/INVOKE
## is_even(3)
##
## VARIABLES SCOPE
## Scope is another word for environtment
## - Former parameter gets bound to the value of actual parameter when function is called
## - New scope/frame/environtment created when enter a function
## - Scope is mapping of names to objects
##
## def f(x):
##      x = x + 1
##      print('in f(x): x = ',x)
##      return x
##
## x = 3
## z = f(x)

# def is_even_with_return(i):
#     """
#     Input: i, a positive int
#     Return True if i is even, otherwise False
#     """
#     print("with return")
#     remainder = i % 2
#     return remainder == 0

# is_even_with_return(3)
# print(is_even_with_return(3))

# def is_even_without_return(i):
#     """
#     Input: i, a positive int
#     Does not return anything
#     """
#     print("without return")
#     remainder = i % 2
#     # return none

# is_even_without_return(3)
# print(is_even_without_return(3))

# Simple is_even function definition
def is_even(i):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """

    remainder = i % 2
    return remainder == 0

# Use the even function later on in the code
print("All numbers between 0 and 20: even or not")

for i in range(20):
    if is_even(i):
        print(i, "even")
    else:
        print(i, "odd")