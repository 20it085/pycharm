# defines lists of username and passwords
un = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
up = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]

#initializing all
ro_att = 0
tries = 0
max_att = 3

#while loop for user and pass input
while True:
    New_un = input("Enter username: ")
    New_pass = input("Enter password: ")
    #conditions for user and pass
    if New_un in un and New_pass == up[un.index(New_un)]:
        print(f"Login successful. Welcome {New_un} !")
        break
    else:
        max_att = max_att - 1
        if max_att > -1:
            print(f"Login incorrect. Tries left: {max_att}")
    if max_att == 0:
        #while loop for robot check
        while True:
            robo = input("Are you a robot (Y/n)? ")
            if robo == 'Y' or robo == '':
                ro_att = 1
                break
            elif robo == 'n':
                max_att = 3
                break
            else:
                continue
    if ro_att == 1:
        break
