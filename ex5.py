import datetime


def getdate():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("1 for food and 2 for exe:-"))
        if c == 1:
            d = input("Type:-")
            with open("Dev_food_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")
        elif c == 2:
            d = input("Type:-")
            with open("Dev_Exe_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")

    elif k == 2:
        c = int(input("1 for food and 2 for exe:-"))
        if c == 1:
            d = input("Type:-")
            with open("Vaibhav_food_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")
        elif c == 2:
            d = input("Type:-")
            with open("Vaibhav_exe_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")

    elif k == 3:
        c = int(input("1 for food and 2 for exe:-"))
        if c == 1:
            d = input("Type:-")
            with open("Riken_food_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")
        elif c == 2:
            d = input("Type:-")
            with open("Riken_exe_add", "a") as dd:
                dd.write(str([str(getdate())]) + ":" + d + "\n")
            print("successfully written")


def retrieve(k):
    if k == 1:
        c = int(input("1 for food 2 for exe:-"))
        if c == 1:
            with open("Dev_food_add") as dd:
                for i in dd:
                    print(i)
        elif c == 2:
            with open("Dev_Exe_add") as dd:
                for i in dd:
                    print(i)

    if k == 2:
        c = int(input("1 for food 2 for exe:-"))
        if c == 1:
            with open("Vaibhav_food_add") as dd:
                for i in dd:
                    print(i)
        elif c == 2:
            with open("Vaibhav_exe_add") as dd:
                for i in dd:
                    print(i)

    if k == 3:
        c = int(input("1 for food 2 for exe:-"))
        if c == 1:
            with open("Riken_food_add") as dd:
                for i in dd:
                    print(i)
        elif c == 2:
            with open("Riken_exe_add") as dd:
                for i in dd:
                    print(i)


a = int(input("1 For add and 2 for retrieve:-"))

if a == 1:
    b = int(input("Enter 1 for Dev 2 for Vaibhav 3 for Riken"))
    take(b)
else:
    b = int(input("Enter 1 for Dev 2 for Vaibhav 3 for Riken"))
    retrieve(b)
