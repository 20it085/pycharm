# lst = []
#
# # number of elements as input
# n = int(input("Enter number of elements : "))
#
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#     lst.append(ele)  # adding the element
#
# sort = input("ENTER ORDER ASC OR DSC OR NONE:-\n")
#
# if sort == "ASC":
#     lst.sort()
#     print(lst)
# elif sort == "DSC":
#     lst.sort(reverse=True)
#     print(lst)
# elif sort == "NONE":
#     print(lst)

# def sort_list(x ,y):#linear sorting Alogirthm
# i=0;
# l=len(x)
#
# if y.upper()=="ASC":
# for i,v in enumerate(x):
# for j in range(i+1,l):
# if x[i]>=x[j]:
# t=x[j]
# x[j]=x[i]
# x[i]=t
# print(x)
# elif y.upper()=='DESC':
# for i,v in enumerate(x):
# for j in range(i+1,l):
# if x[i]<=x[j]:
# t=x[j]
# x[j]=x[i]
# x[i]=t
# print(x)
#
# l1=[3,4,1,5,2]
# print (l1)
# sort_list(l1,'ASC')
# print ( 'this is ')
# print(l1)
# sort_list(l1,'DESC')


# print("Input six integers:")
# nums = list(map(int, input().split()))
# nums.sort()
# nums.reverse()
# print("After sorting the said ntegers:")
# print(*nums)

def Sort(x,y):
    # number of elements as input
    # n = int(input("Enter number of elements : "))
    # iterating till the range
    # for i in range(0, n):
    #     ele = int(input())
        # x.append(ele)  # adding the element
    # y = input("ENTER ORDER ASC OR DSC OR NONE:-\n")
    if y == "ASC":
        x.sort()
        print(x)
    elif y == "DSC":
        x.sort(reverse=True)
        print(x)
    elif y == "NONE":
        print(x)
y = input("ENTER ORDER ASC OR DSC OR NONE:-\n")
Sort(x=[1,2,3],y=y)

print ("TIME ON EARTH")

sec =  input ("Input a time in seconds:"'\n')

total_sec = int(sec) # convert the input to an integer
#caclculate the hour, minutes and seconds
hours = total_sec // 3600
sec_remaining = total_sec % 3600
minutes =  sec_remaining // 60
sec_final = sec_remaining  % 60
#print the result in the given format
print('\n' "The time on Earth is" ,hours,"hours",minutes,"minutes", "and",sec_final,"seconds"'.')

print("\nTIME ON TRISOLARIS")

trisol_seconds_per_minutes = int(input("Input the number of seconds in a minute on Trisolaris:\n"))
trisol_minutes_per_hours = int(input("Input the number of minutes in an hour on Trisolaris:\n"))

trisol_hours = total_sec // (trisol_seconds_per_minutes * trisol_minutes_per_hours)
trisol_sec_remaining = total_sec % (trisol_seconds_per_minutes * trisol_minutes_per_hours)
trisol_min = trisol_sec_remaining // trisol_seconds_per_minutes
trisol_sec_final = trisol_sec_remaining % trisol_seconds_per_minutes

print(f"\nThe time on Trisolaris is {trisol_hours} hours {trisol_min} minutes and {trisol_sec_final} seconds.")