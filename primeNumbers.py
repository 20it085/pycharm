def primeNumnbers(n):

    for i in range(2, n):
        if n % i == 0:
            return "Enter number ia not prime number"
        else:
            return "Enter number is prime number"

n = int(input("Enter Number to check:-"))
print(primeNumnbers(n))


