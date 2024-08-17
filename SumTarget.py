from array import *

arr = array("i", [])
p = int(input("Enter size of array:-"))

for i in range(p):
    q = int(input("Enter value:-"))
    arr.append(q)
print(arr)

target = int(input("Enter Final value:-"))

length = len(arr)
for a in range(length):
    for e in range(a + 1, length):
        if arr[a] + arr[e] == target:
            lst = [a, e]
            print(lst)
