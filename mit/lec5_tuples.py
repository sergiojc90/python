################################
## Lecture 5
## Tuples, Listing, Aliasing, Mutability, Cloning
##
## Compound Data Types
## - Tuples
## - Lists
## Idea of aliasing
## Idea of mutability
## Idea of cloning
##
## TUPLES
## An ordered sequence of elements, can mix element types cannot change element values, immutable represented with parenthesis
te = () # Empty tuple
t = (2,"mit",3)
print(t+(5,6))
print(te)
print(len(t))
t[1] = 4