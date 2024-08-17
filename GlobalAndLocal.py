a = 10
print(a)


def something():
    # global a

    a = 15
    print(a)

    x = globals()["a"]
    print(x)


something()

print(a)

# ll = ["dev", "vaibhav", "riken", "badal", "jeenal"]

# i = 0
#
# for item in ll:
#     if i % 2 == 0:
#         print(item)
#     i += 1

# for index, item in enumerate(ll):
#     if index % 2 == 0:
#         print(item)

# def func(data):
#     for i, f in data.items():
#         print(i, f)
#
#
# lst = ["dev", "vaibhav", "riken", "badal", "jeenal"]
# dic = {"Dev": 1, "vaibhav": 2, "Riken": 3}
# func(dic)

# def person(name, **data):
#     print(name)
#
#     for i, j in data.items():
#         print(i, j)
#
#
# person(name="Dev", age=28, city="surat", number=9825446367)

