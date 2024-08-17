#list of keyboard
keybo = ["abcdefghijklm", "nopqrstuvwxyz"]
#defining fuction for find
def find(character):
    for index, ROW in enumerate(keybo):
        if character in ROW:
            return (index, ROW.index(character))
    return (None, None)
#defining function for answer
def ans(a):
    cur_row, cur_col = 0, 0
    work = ''
    #for loop for character
    for ch in a:
        final_row, final_col = find(ch)

        if final_row is None:
            return "The string cannot be typed out."

        # Move to correct col
        while cur_col < final_col:
            work += 'r'
            cur_col += 1
        while cur_col > final_col:
            work += 'l'
            cur_col -= 1
        # Move to the correct row
        while cur_row < final_row:
            work += 'd'
            cur_row += 1
        while cur_row > final_row:
            work += 'u'
            cur_row -= 1

        # Type the char
        work += 'p'

    return work


a = input("Enter a string to type: ").strip()
work = ans(a)
if work != "The string cannot be typed out.":
    print("The robot must perform the following operations:")
    print(work)
else:
    print(work)




