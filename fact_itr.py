def fact_itr(n):

    result = 1
    if n > 1:
        for i in range(1, n+1):
            result *= i
        return result
    else:
        return 'n has to be positive'

inp = int(input("Enter a number: "))

print(f"The result is:", fact_itr(inp))
