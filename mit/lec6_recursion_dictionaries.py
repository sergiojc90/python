##########################
## Recurtion
## Is the process of repeting items in a self-similar way
## Take a problem and reduce it to a  simpler version of a similar problem
## WHAT IS RECURTION?
## 
## Algorithmically: a way to design solutions to problems by divide-and-conquer or decrease-and-conquer
## "Reduce the problem to a simpler version of the same problem"
##
## Semantically: a programming technique where a function calls itself
## In programming, goal is to not have infinite recurtion
## - Must have 1 or more base cases that are easy to solve
## - Must solve the same problem on some other input with the goal of simplifying the larger problem input
##
## ITERATIVE ALGORITHMS SO FAR
## Looping constructs (while and for loops) lead to iterative algorithms
## can capture computation in a set of state varibles that update on each iteration through loop
## 
## MULTIPLICATION - ITERATIVE SOLUTION
## "multiply a*b" is equivalent to "add a to itself b times"

# def mult_iter(a,b):
#     result = 0

#     while b>0:
#         result += a
#         b -= 1
#     return result

# ## MULTIPLICATION - RECURSIVE SOLUTION

# def mult(a,b):
#     if b == 1:
#         return a # This is the base case, to avoid infinite recurtion.
#     else:
#         return a + mult(a,b-1)

# ## FACTORIAL

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)

## TOWERS OF HANOI

# def printMove(fr,to):
#     print("move from" + str(str) + "to" + str(to))

# def Towers(n, fr, to, spare):
#     if n == 1:
#         printMove(fr,to)
#     else:
#         Towers(n-1, fr, spare, to)
#         Towers(1, fr, to, spare)
#         Towers(n-1, spare, to, fr)

## RECURTION WITH MULTIPLE BASE CASES
## Fibonacci

# def fib(x):
#     """
#         assumes x an int >= 0
#         returns Fibonacci of x
#     """
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)

## PALINDROME

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
    return isPal(toChars(s))