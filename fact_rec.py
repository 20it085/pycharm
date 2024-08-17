def fact_rec(x):

    if x <= 1:
        return 1
    else:
        return (x*fact_rec(x-1))

n = int(input("Enter a number:-"))

a = fact_rec(n)
print(a)

# def factorial(x):
#
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
#
# num = int(input("Enter a number: "))
#
# result = factorial(num)
# print("The factorial of", num, "is", result)
