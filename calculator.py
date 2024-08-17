n1 = int(input("Enter value one:-"))
n2 = int(input("Enter value two:-"))

operator = input("Enter Any operator \n"
                 "Addition = +\n"
                 "Substarction = -\n"
                 "Multiplication = *\n"
                 "Division = /\n")

if operator == "+":
    print("Answer=:",n1+n2)
elif operator == "-":
    print("Answer:-",n1-n2)
elif operator == "*":
    print("Answer:-",n1*n2)
elif operator == "/":
    print("Answer:-",n1/n2)