import itertools

STR = input("Enter String:=")
combs = []
lst = []
lst1 = []
for l in range(1, len(STR) + 1):
    combs.append(list(itertools.combinations(STR, l)))

for c in combs:
    # print(c)
    for t in c:
        a = int(''.join(t))
        print(a, end=' ')
        lst.append(a)


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
        else:
            # print("Prime number")
            return True


for x in range(len(lst)):
    is_prime(lst[x])

count = 0
for e in range(len(lst)):
    if (is_prime(lst[e]) == True) and (lst[e - 1] < lst[e]):
        count += 1
print(end='\n')
print(count)

