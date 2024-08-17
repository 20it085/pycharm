def smart_div(func):
    def inner(a, b):
        # print("pqr")
        if a < b:
            a, b = b, a
        func(a, b)
        # print("xyz")

    return inner


def div(a, b):
    # if a < b:
    #     a,b = b,a
    print(a / b)


div1 = smart_div(div)
div1(2, 4)
