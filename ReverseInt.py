def reverseInt(x):
    def signcheck(n):
        if n >= 0:
            return 1
        else:
            return -1

    sign = signcheck(x)
    x = str(abs(x))
    reverse = x[::-1]
    num = sign * int(reverse)

    if abs(num) > (2 ** 31 - 1):
        return 0
    else:
        return num


a = reverseInt(-123)
print(a)
