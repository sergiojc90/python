# ###################
# # Example: Strings#
# ###################

# hi = "Hello there"
# name = "ana"
# greet = hi + name
# print(greet)

# greeting = hi + " " + name
# print(greeting)

# silly = hi + (" " + name)*3
# print(silly)

# ###################

# x = 1
# print(x)

# x_str = str(x)
# print("my fav number is", x,".","x =",x)
# print("my fav number is", x_str + ".","x = "+x_str)

# ##################

# text = input("Type anything... ")
# print(5*text)

# num = int(input("Type a number... "))
# print(num*5)

# #############
# #Booleans

#print("a">"b")

# #############
# #Control Flow

# If condition

# x = float(input("Enter a number for x: "))
# y = float(input("Enter a number for y: "))

# if x == y:
#     print("x and y are equal")
#     if y != 0:
#         print("therefore, x/y is", x/y)
# elif x < y:
#     print("x is smaller")
# else:
#     print("y is smaller")

# print("thanks!")

# While loop

# n = 0

# while n <= 5:
#     print(n)

# for n in range(5):
#     print(n)

# Range (start,stop,step)

# mysum = 0

# for i in range(7, 10):
#     mysum += i

# print(mysum)

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    break
print(mysum)