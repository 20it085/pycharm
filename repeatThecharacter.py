def repeat(word):

    result = ""
    for i in word:
        result = result + i
        result = result + i
    # print(result)
    return result

a = repeat("geeks")
print(a)
