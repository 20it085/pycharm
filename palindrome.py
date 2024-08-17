def palindrome(x):
    z = str(x)
    w = "".join(reversed(z))
    if z == w:
        return True
    else:
        return False


a = palindrome(121)
print(a)
