def find_pos(keyboard, char):
    for r, ROW in enumerate(keyboard):
        for c, k in enumerate(ROW):
            if k == char:
                return (r, c)
    return None

def compute_mov(start, target):
    sr, sc = start
    tr, tc = target
    ver_mov = tr - sr
    hori_mov = tc - sc

    move_ins = ''
    if ver_mov > 0:
        move_ins += 'd' * ver_mov
    elif ver_mov < 0:
        move_ins += 'u' * -ver_mov

    if hori_mov > 0:
        move_ins += 'r' * hori_mov
    elif hori_mov < 0:
        move_ins += 'l' * -hori_mov

    return move_ins

def cal_path(keyboard, input_string):
    start = (0, 0)  # Starting at the top-left corner
    path = ''

    for char in input_string:
        pos = find_pos(keyboard, char)
        if pos is None:
            return None

        path += compute_mov(start, pos) + 'p'
        start = pos

    return path

def main():
    keyboards = [
        ["abcdefghijklm", "nopqrstuvwxyz"],
        ["789", "456", "123", "0.-"],
        ["chunk", "vibex", "gymps", "fjord", "waltz"],
        ["bemix", "vozhd", "grypt", "clunk", "waqfs"]
    ]

    input_string = input("Enter a string to type: ")

    best_key = None
    min_moves = float('inf')
    best_path = None
    best_index = -1

    for i, keyboard in enumerate(keyboards):
        path = cal_path(keyboard, input_string)
        if path is not None:
            moves = len(path)  # The number of moves is the length of the path string
            if moves < min_moves:
                min_moves = moves
                best_key = keyboard
                best_path = path
                best_index = i

    if best_key is not None:
        print(f"Configuration used:\n{'-' * 7}")
        for row in best_key:
            print(f"| {row} |")
        print(f"{'-' * 7}")
        print(f"The robot must perform the following operations:\n{best_path}")
    else:
        print("The string cannot be typed out.")

if __name__ == "__main__":
    main()
