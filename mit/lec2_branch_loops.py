###################
# Example: Strings#
###################

hi = "Hello there"
name = "ana"
greet = hi + name
print(greet)

greeting = hi + " " + name
print(greeting)

silly = hi + (" " + name)*3
print(silly)

###################

x = 1
print(x)

x_str = str(x)
print("my fav number is", x,".","x =",x)
print("my fav number is", x_str + ".","x = "+x_str)

##################

text = input("Type anything... ")
print(5*text)