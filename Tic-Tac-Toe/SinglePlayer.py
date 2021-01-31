from Board import Board
from Tile import Tile

class Game(Board):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.status = True
        self.update_board()
        self.show_text("Coming Soon")
        # self.play()

    def check_win(self, turn):
        if self.board[0][0] == turn and self.board[0][1] == turn and self.board[0][2] == turn:
            return True
        if self.board[1][0] == turn and self.board[1][1] == turn and self.board[1][2] == turn:
            return True
        if self.board[2][0] == turn and self.board[2][1] == turn and self.board[2][2] == turn:
            return True
        if self.board[0][0] == turn and self.board[1][0] == turn and self.board[2][0] == turn:
            return True
        if self.board[0][1] == turn and self.board[1][1] == turn and self.board[2][1] == turn:
            return True
        if self.board[0][2] == turn and self.board[1][2] == turn and self.board[2][2] == turn:
            return True
        if self.board[0][0] == turn and self.board[1][1] == turn and self.board[2][2] == turn:
            return True
        if self.board[2][0] == turn and self.board[1][1] == turn and self.board[0][2] == turn:
            return True
        return False

    def ai_move(self, depth):
        if depth == 8:
            return False
        if depth&1:
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.board[i][j] == '-'):
                        self.board[i][j] = 'X'
                        if self.check_win('X') or not self.ai_move(depth+1):
                            self.board[i][j] = '-'
                            print(i , j)
                            return True
                        self.board[i][j] = '-'
            return False
        else:
            for i in range(0, 3):
                for j in range(0, 3):
                    if(self.board[i][j] == '-'):
                        self.board[i][j] = 'O'
                        if self.check_win('O') or not self.ai_move(depth+1):
                            self.board[i][j] = '-'
                            print(i , j)
                            return True
                        self.board[i][j] = '-'
            return False

    def get_ai_move(self):
        x = 0
        y = 0
        for i in range(0 , 3):
            for j in range(0 , 3):
                if(self.board[i][j]=='-'):
                    x = i
                    y = j
                    self.board[i][j] = 'O'
                    if self.check_win('O') or not self.ai_move(1):
                        self.board[i][j] = '-'
                        print(i , j)
                        return (i, j)
                    self.board[i][j] = '-'
        return (x , y)

    def make_move(self, move):
        self.board[move[0]][move[1]] = 'O'
        self.tiles[move[0]][move[1]] = Tile(True, 'O')
        self.update_board()

    def play(self):
        while self.status:
            if self.turn == 0:
                self.status = self.play_game(self.turn)
                if self.check_win('X'):
                    print("You Won!!!")
                    self.show_text("You Won!!!")
                    break
            else:
                move = self.get_ai_move()
                self.make_move(move)
                if self.check_win('O'):
                    print("Computer Won!!!")
                    self.show_text("Computer Won!!!")
                    break
            self.turn += 1
            self.turn %= 2
            print(self.board)
