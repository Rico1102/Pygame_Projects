from Board import Board

class Game(Board):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.status = True
        self.update_board()
        self.play()

    def check_win(self , turn):
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

    def play(self):
        while self.status :
            self.status = self.play_game(self.turn)
            if self.turn == 0 and self.check_win('X'):
                print("Player1 Won!!!")
                self.show_text("Player1 Won!!!")
                break
            if self.turn == 1 and self.check_win('O'):
                print("Player2 Won!!!")
                self.show_text("Player2 Won!!!")
                break
            self.turn += 1
            self.turn %= 2
