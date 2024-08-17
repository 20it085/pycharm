# a = int(input("Enter value a :-"))
# b = int(input("Enter value b :-"))
# c = sum((a,b))
# print(c)

# def function1(a,b):
#     average = (a+b)/2
#     # print(average)
#     return average
# v = function1(10,10)
# print(v)

# def add(y):
#     x=10
#     z = x+y
#     return z
#     # print(z)
# a = add(10)
# print(a)

# Anonymous function or lamda function

# from functools import reduce

# ll = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# f = list(map(lambda a: (a * a), range(10)))
# g = list(filter(lambda b: (b * b), range(5)))

def sqr(a):
    return a * a


def cub(a):
    return a * a * a


ll = [sqr, cub]

for i in range(5):
    h = list(map(lambda x: x(i), ll))
# h = reduce(lambda c : c*c*c, range(4))
print("result:-", h)
