def decimalToBinary(n):
    if (n > 1):
        decimalToBinary(n // 2)
    print(n % 2, end=' ')

decimalToBinary(8)
print("\n")
decimalToBinary(18)
print("\n")
decimalToBinary(7)
print("\n")

def binaryToDecimal(n):
    return int(n, 2)

print(binaryToDecimal("1111"))
print(binaryToDecimal('100'))
print(binaryToDecimal('101'))
print(binaryToDecimal('1001'))
