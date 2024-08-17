a = input("Enter the string: ")
a = a.lower()

letter1 = 'o'
letter2 = 'x'
count1 = dict.fromkeys(letter1, 0)
count2 = dict.fromkeys(letter2, 0)

print(count1)
print(count2)

for keys in a:
    # print(keys)
    if keys in count1:
        count1[keys] +=1
        # print(count1[keys])
for keys in a:
    if keys in count2:
        count2[keys] +=1

if count1['o'] == count2['x']:
    print(True)
else:
    print(False)

