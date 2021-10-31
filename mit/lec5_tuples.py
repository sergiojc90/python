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
# te = () # Empty tuple
# t = (2,"mit",3)
# print(t+(5,6))
# print(te)
# print(len(t))
# t[1] = 4
## Tuples can be used to return more than one value from a function
def quotient_and_remainder(x,y):
    q = x // y
    r = x % y
    return(q,r)

(quot,rem) = quotient_and_remainder(4,5)
print(quot)
print(rem)