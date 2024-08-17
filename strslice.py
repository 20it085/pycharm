mystr = "Riken is a bad boy"
print(mystr)
print(mystr[3])
print(mystr[-4:])
print(mystr[1:6])
print(len(mystr))
print(mystr[0:7:3])
print(mystr[::-1]) #reverse string

print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("boy"))
print(mystr.startswith("Riken"))
print(mystr.count("a"))
print(mystr.capitalize())
print(mystr.find("a"))
print(mystr.upper())
print(mystr.lower())
print(mystr.replace("Riken","Dev"))

numbers = ["1","5","80"]

# for i in range(len(numbers)):
#     # print(items)
#     numbers[i] = int(numbers[i])

numbers = list(map(int,numbers))

numbers[1] = numbers[1] + 2
print(numbers[1])