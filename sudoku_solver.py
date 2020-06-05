board = [
    [7, 0, 6, 5, 0, 0, 9, 2, 0], 
    [0, 3, 0, 0, 0, 9, 0, 0, 1], 
    [0, 1, 0, 6, 0, 4, 0, 0, 3], 
    [6, 0, 7, 1, 8, 0, 0, 0, 0], 
    [0, 0, 0, 0, 9, 0, 7, 8, 6], 
    [0, 0, 0, 0, 6, 0, 1, 5, 0], 
    [0, 0, 0, 0, 5, 0, 4, 0, 8], 
    [0, 0, 0, 2, 4, 8, 0, 0, 0], 
    [0, 0, 5, 9, 0, 6, 0, 3, 0]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo)):
            if bo[i][j] == 0:
                return (i, j)

    return None


def valid(bo, num, pos):
    # check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check box
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
    print('\n*************************\nSTARTING BOARD\n')
    print_board(board)
    print('\n*************************\nBOARD SOLVED\n')
    solve(board)
    print_board(board)
