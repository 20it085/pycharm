# print("How Many Row You Want To Print")
# one = int(input())
# print("Type 1 Or 0")
# two = int(input())
# new = bool(two)
# # print(new)
# if new == True:
#     for i in range(1,one+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new == False:
#     for i in range(one,0,-1):
#         for j in range(1,i+1):
#             print("*",end="")
#         print()

print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new = bool(two)
# print(new)
if new == True:
    for i in range(one):
        for j in range(i+1):
            print("*",end=" ")
        print()
elif new == False:
    for i in range(one):
        for j in range(i,one):
            print("*",end="")
        print()

# print("How Many Row You Want To Print")
# one = int(input())
# print("Type 1 Or 0")
# two = int(input())
# new =bool(two)
# if new == True:
#     for i in range(1,one+1):
#         print("* "*i)
# elif new == False:
#     for i in range(1,one+1):
#         print(" "*(one-i)+"*"*i)
