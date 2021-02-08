import random


def get_next(x, y):
    if(y == 8):
        return x+1, 0
    else:
        return x, y+1

def check_point(board, x, y):
    if board[x][y] == '-':
        return True
    for i in range(0, 9):
        if (board[x][i] == board[x][y] and i !=y) or (board[i][y] == board[x][y] and i!=x):
            return False
    base_x = 3*(x//3)
    base_y = 3*(y//3)
    for i in range(0, 3):
        for j in range(0, 3):
            if(base_x+i ==x and base_y+j==y):
                continue
            elif(board[base_x+i][base_y+j] == board[x][y]):
                return False
    return True

def backtrack(board, x, y):
    if(x == 9 and y == 0):
        return True
    mid = random.randrange(1, 10)
    order = random.randrange(0, 2)
    if order == 0:
        for i in range(1, mid):
            board[x][y] = str(i)
            if check_point(board, x, y):
                nx, ny = get_next(x, y)
                if backtrack(board, nx, ny):
                    return True
                board[x][y] = '-'
            else:
                board[x][y] = '-'
            if(i == 9):
                return False
        for i in range(mid, 10):
            board[x][y] = str(i)
            if check_point(board , x, y):
                nx, ny = get_next(x, y)
                if backtrack(board, nx, ny):
                    return True
                board[x][y] = '-'
            else:
                board[x][y] = '-'
            if(i == 9):
                return False
    elif order == 1:
        for i in range(mid, 10):
            board[x][y] = str(i)
            if check_point(board, x, y):
                nx, ny = get_next(x, y)
                if backtrack(board, nx, ny):
                    return True
                board[x][y] = '-'
            else:
                board[x][y] = '-'
            if(i == 9):
                return False
        for i in range(1, mid):
            board[x][y] = str(i)
            if check_point(board, x, y):
                nx, ny = get_next(x, y)
                if backtrack(board, nx, ny):
                    return True
                board[x][y] = '-'
            else:
                board[x][y] = '-'
            if(i == 9):
                return False
    return True

def generate_sudoku():
    board = [[], [], [], [], [], [], [], [], []]
    n_board = [[], [], [], [], [], [], [], [], []]
    indexes = []
    for i in range(0 , 81):
        indexes.append(i)
    for i in range(0 , 9):
        for j in range(0 , 9):
            board[i].append('-')
            n_board[i].append('-')
    start = random.randrange(1 , 10)
    board[0][0] = str(start)
    backtrack(board , 0 , 1)
    for i in range(0, 9):
        for j in range(0, 9):
            n_board[i][j] = board[i][j]
    for i in range(45):
        index = random.randrange(0 , len(indexes))
        x = indexes[index]//9
        y = indexes[index]% 9
        board[x][y] = '-'
        indexes.remove(indexes[index])
    return board , n_board

# generate_sudoku()
