# list = [2,5,6,8,9,2,5,25,36,22,20,14]

def CountEvenOdd(list):
    even = 0
    odd = 0

    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


list = [2, 5, 6, 8, 9, 2, 5, 25, 36, 22, 20, 14]
even, odd = CountEvenOdd(list)

print("Even : {} and odd : {}".format(even, odd))
