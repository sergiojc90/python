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

# ## Lists are mutable
# L = [1,2,3]

# # L[1] = 5 #This changes the L[1] value, it does not creates a new variable.

# # print(L)

# ## Iterating  over a List
# ## Compute the sum of elements of a list
# ## common pattern, iterate over list elements

# # total = 0

# # for i in L:
# #     total += i

# # print(total)

# ## Operations on lists - ADD
# ## add elements to end of list with L.append(element)
# ## MUTATES THE LIST!

# L.append(1) #this mutates the list

# print(L)

# ## to combine lists together use concatenation, + operator, to give you a NEW list
# ## mutate list with L.extend(some_list)

# L1 = [2,1,3]
# L2 = [4,5,6]
# L3 = L1 + L2

# print(L3)
# print(L1)
# print(L2)
# L1.extend([0,6])
# print(L1)

## Operations on lists - REMOVE
## Delete element at a specific index with del(L[index])
## Remove element at end of list with L.pop(), returns the removed element
## Remove a specific element with L.remove(element)
## - looks for the element and removes it
## - if element occurs multiple times, removes first occurence
## - if element not in list, gives an error

L = [2,1,3,6,3,7,0] # do below in order

L.remove(2) # Mutates L
print(L)

L.remove(3)
print(L)

del(L[1])
print(L)

L.pop()
print(L)

