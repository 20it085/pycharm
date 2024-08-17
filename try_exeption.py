print("Enter value 1")
num1 = input()
print("Enter value 2")
num2 = input()

try:
    print("Sum of value is",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This is important")
