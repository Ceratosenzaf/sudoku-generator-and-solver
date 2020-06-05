import random


def get_empty_board():
    line = []
    bo = []

    for i in range(9):
        for j in range(9):
            line.append(0)
        bo.append(line)
        line = []

    return bo


def generator(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    valid_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(valid_num) > 0:
        n = random.choice(valid_num);
        valid_num.remove(n);
        if valid(bo, n, (row,col)):
            bo[row][col] = n

            if generator(bo):
                return True

            bo[row][col] = 0

    return False  


def remove_numbers(bo, dif):
    if dif == 'easy':
        n = 3
    if dif == 'medium':
        n = 5
    if dif == 'hard':
        n = 7

    for i in range(9):
        for j in range(n):
            col = random.randint(0,8);
            bo[i][col] = 0;


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)  # row, col   Y, X

    return None


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(bo)):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(bo[i][j])
            else:
                print(bo[i][j], end=" ")
    print("")


if __name__ == "__main__":
    # you can change this in easy,medium,hard
    difficulty = 'hard'

    print ('\n*************************\nEMPTY BOARD\n')
    board = get_empty_board()
    print_board(board)

    print ('\n*************************\nRANDOM BOARD\n')
    generator(board)
    print_board(board)

    print ('\n*************************\nBOARD TO BE SOLVED\n')
    remove_numbers(board, difficulty)
    print_board(board)