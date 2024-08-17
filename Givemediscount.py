x = int(input("Enter total numebr of amount:-"))
y = int(input("Total percentage discount:-"))

def gimeMediscount(x,y):

    price = x-(x*y)/100
    return price

a = gimeMediscount(x,y)
print(a)



