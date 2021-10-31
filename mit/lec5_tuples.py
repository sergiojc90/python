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
# def quotient_and_remainder(x,y):
#     q = x // y
#     r = x % y
#     return(q,r)

# (quot,rem) = quotient_and_remainder(4,5)
# print(quot)
# print(rem)
#
## We can iterate within a tuple

# def get_data(aTuple):
#     nums = ()
#     words = ()

#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)

#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)

#     return(min_n, max_n, unique_words, words)

# myTuple = ((1,"Pizza"), (2, "Burger"),(3,"Tacos"),(4,"Hotdog"),(1,"Burger"))

# (a,b,c,d) = get_data(myTuple)

# print("Min number:",a,"Max number:",b,"There are",c,"unique words"," The list of unique words is",d)

## LISTS
## Like tuples, they can contain any kind of data type, but they are MUTABLE

# a_list = []
# L = [2,"a",4,[1,2]]

# print(len(L), L[0],L[2]+1,L[3])

# i = 2
# print(L[i-1])

## Lists are mutable
L = [1,2,3]

# L[1] = 5 #This changes the L[1] value, it does not creates a new variable.

# print(L)

## Iterating  over a List
## Compute the sum of elements of a list
## common pattern, iterate over list elements

total = 0

for i in L:
    total += i

print(total)