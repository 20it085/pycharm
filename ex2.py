N1 = int(input('Enter first Number :- '))
opr = input("Enter operator :-")
N2 = int(input("Enter second Number :-"))

if opr=="*" and (N1==45 or N1==3) and (N2==45 or N2==3):
    print("Your result is 555")
elif opr=="*":
    print("Your result is ", N1*N2)
elif opr == "+" and (N1 == 56 or N1 == 9) and (N2 == 9 or N2 == 56):
    print("Your result is 77")
elif opr=="+":
    print("Your result is ", N1+N2)
elif opr=="/" and (N1==56 and N2==6):
    print("Your result is 4")
elif opr=="/":
    print("Your result is ", N1/N2)
elif opr=="-":
    print(N1-N2)