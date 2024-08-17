# with open("dev.txt") as x:
#     a = x.read(10)
#     print(a)
x = open("dev.txt")
# content = x.read()
# print(x.tell())
# x.seek(10)
# print(x.readline())
# print(x.readlines())
for line in x:
    print(line)
# print(content)
# x.close()
