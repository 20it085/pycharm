from array import *
#
# Array = array("i",[1,2,3,4,5])
# print(Array)
# print(Array.buffer_info())
#
# newArry = array(Array.typecode, (a%3 for a in Array))
# print(newArry)

arr = array("i", [])

n = int(input("Enter The size of array:-"))

for i in range(n):
    x = int(input("Enter numbers for input:-"))
    arr.append(x)
print(arr)

val = int(input("Enter to verif your value:-"))

# k = 0
for e in arr:
    if e == val:
        print(arr.index(e))
        # print(k)
        # break
     # k += 1