## Strings

# s = "abc"
# print(len(s))

# print(s[-1]) # Negative indexing in order to go from right to left

## Slice
## [start:stop:step]

# s = "abababab"

# print(s[::-1])

## Strings are immutable

# s = "hello"
# s[0] = "y"

## for Loops Recap
## These two code snippets do the same thing

s = "abcdefgh"

for index in range(len(s)):
    if s[index] == "i" or s[index] == "u":
        print("There is an i or u")

## This snippet is more "pythonic"
for char in s:
    if char == "i" or char == "u":
        print("There is an i or u")