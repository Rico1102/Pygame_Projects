import pygame
from pygame.constants import MOUSEBUTTONDOWN
from Tile import Tile
import threading
import os

class Board():
    def __init__(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((432, 432))
        pygame.display.set_caption('Sudoku')
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.Green = (0, 255, 0)
        self.Red = (255, 0, 0)
        self.Blue = (0, 0, 128)
        self.active = False
        self.active_x = -1
        self.active_y = -1
        self.board = [['-', '-', '-', '2', '6', '-', '7', '-', '1'],
                      ['6', '8', '-', '-', '7', '-', '-', '9', '-'],
                      ['1', '9', '-', '-', '-', '4', '5', '-', '-'],
                      ['8', '2', '-', '1', '-', '-', '-', '4', '-'],
                      ['-', '-', '4', '6', '-', '2', '9', '-', '-'],
                      ['-', '5', '-', '-', '-', '3', '-', '2', '8'],
                      ['-', '-', '9', '3', '-', '-', '-', '7', '4'],
                      ['-', '4', '-', '-', '5', '-', '-', '3', '6'],
                      ['7', '-', '3', '-', '1', '8', '-', '-', '-']]
        self.tiles = [[], [], [], [], [], [], [], [], []]
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.solving = False
        self.solved = False
        row = 0
        for i in self.board:
            for j in i:
                if j == '-':
                    self.tiles[row].append(Tile(fix=False))
                else:
                    self.tiles[row].append(Tile(text=j, fix=True))
            row += 1 
        self.update_board()
        self.play_game()

    def create_outline(self, x, y, s_x=38, s_y=38, width=1, color=None):
        if color is None:
            curr_color = self.Black
        else:
            curr_color = color
        pygame.draw.line(self.canvas, curr_color, [x, y], [x+s_x, y], width)
        pygame.draw.line(self.canvas, curr_color, [
                         x+s_x, y], [x+s_x, y+s_y], width)
        pygame.draw.line(self.canvas, curr_color, [
                         x+s_x, y+s_y], [x, y+s_y], width)
        pygame.draw.line(self.canvas, curr_color, [x, y+s_y], [x, y], width)

    def create_rect(self, x, y, s_x, s_y, width=1):
        pygame.draw.rect(self.canvas, self.White, [x, y, s_x, s_y])
        self.create_outline(x, y, s_x, s_y, width)

    def draw_board(self):
        font = pygame.font.Font('freesansbold.ttf', 10)
        text = font.render("Solve", True, self.White)
        textRect = text.get_rect()
        textRect.center = (410, 23)
        pygame.draw.rect(self.canvas, self.Black, [390, 13, 40, 20])
        self.canvas.blit(text, textRect)
        # self.create_rect(9*38+48 , 3 , 40 , 40)
        for i in range(0, 9):
            for j in range(0, 9):
                self.tiles[i][j].pos_y = i * 38 + 45
                self.tiles[i][j].pos_x = j * 38 + 45
                self.create_rect(i*38+45, j*38+45, 38, 38)
        for i in range(0 , 3):
            for j in range(0 , 3):
                self.tiles[3*i][3*j].pos_y = 3*i * 38 + 45
                self.tiles[3*i][3*j].pos_x = 3*j * 38 + 45
                self.create_outline(3*i*38+45, 3*j*38+45, 3*38, 3*38, width=2)
        if(self.active):
            self.create_outline(self.active_y*38+45, self.active_x*38+45, 38, 38, width=2, color=self.Green)

    def draw_tiles(self):
        for i in self.tiles:
            for j in i:
                j.draw_tile(self.canvas, self.font)
    
    def update_board(self):
        self.canvas.fill(self.White)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Sudoku", True, self.Green)
        textRect = text.get_rect()
        textRect.center = (216, 22)
        self.canvas.blit(text, textRect)
        self.draw_board()
        self.draw_tiles()
        pygame.display.update()

    def check_board(self):
        for x in range(0 , 9):
            for y in range(0 , 9):
                if self.board[x][y] == '-' or self.tiles[x][y].present:
                    continue
                flag = True
                for i in range(0 , 9):
                    if (self.board[x][i] == self.board[x][y] and i!=y) or (self.board[i][y] == self.board[x][y] and i!=x):
                        self.tiles[x][y].color = self.Red
                        flag = False
                        break
                base_x = 3*(x//3)
                base_y = 3*(y//3)
                for i in range(0 , 3):
                    for j in range(0 , 3):
                        if(base_x+i==x and base_y+j==y):
                            continue
                        elif(self.board[base_x+i][base_y+j] == self.board[x][y]):
                            self.tiles[x][y].color = self.Red
                            flag = False
                            break
                if flag:
                    self.tiles[x][y].color = self.Green

    def check_point(self, x, y):
        if self.board[x][y] == '-' or self.tiles[x][y].present:
            return True
        for i in range(0 , 9):
            if (self.board[x][i] == self.board[x][y] and i!=y) or (self.board[i][y] == self.board[x][y] and i!=x):
                self.tiles[x][y].color = self.Red
                return False
        base_x = 3*(x//3)
        base_y = 3*(y//3)
        for i in range(0 , 3):
            for j in range(0 , 3):
                if(base_x+i==x and base_y+j==y):
                    continue
                elif(self.board[base_x+i][base_y+j] == self.board[x][y]):
                    self.tiles[x][y].color = self.Red
                    return False
        self.tiles[x][y].color = self.Green
        return True

    def game_over(self):
        for i in range(0 , 9):
            for j in range(0 , 9):
                if self.board[i][j] == '-' or self.tiles[i][j].color == self.Red:
                    return False
        return True

    def play_game(self, turn=0):
        run = True
        while run:
            if self.solved:
                self.show_text("Sudoku solved")
            for event in pygame.event.get():
                if self.solving:
                    continue
                if event.type == pygame.QUIT:
                    run = False
                    self.destroy_board()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (pos[0]>=390 and pos[0]<=430) and (pos[1]>=13 and pos[1]<=33) :
                        self.solve_sudoku()
                    x = (pos[1] - 45)//38
                    y = (pos[0] - 45)//38
                    if (x<9 and x>=0) and (y<9 and y>=0):
                        self.active = True
                        self.active_x = x
                        self.active_y = y

                    else:
                        self.active = False
                    self.update_board()
                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.tiles[self.active_x][self.active_y].present:
                        if event.key == pygame.K_BACKSPACE:
                            self.tiles[self.active_x][self.active_y].text = ""
                            self.tiles[self.active_x][self.active_y].color = self.Green
                            self.board[self.active_x][self.active_y] = '-'
                        elif event.key == pygame.K_RETURN:
                            self.active = False
                        else:
                            if event.unicode>'0' and event.unicode<='9':
                                self.tiles[self.active_x][self.active_y].text = event.unicode
                                self.board[self.active_x][self.active_y] = event.unicode
                                self.tiles[self.active_x][self.active_y].color = self.Green
                        self.check_board()
                        self.update_board()
                    if self.game_over():
                        run = False
                        self.show_text("Sudoku Solved")

    def destroy_board(self):
        pygame.quit()

    def show_text(self, statment):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(statment, True, self.Blue)
        textRect = text.get_rect()
        textRect.center = (216, 216)
        self.canvas.blit(text, textRect)
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.destroy_board()
                    exit(0)

    def solve_sudoku(self):
        self.solving = True
        t1 = threading.Thread(target=self.backtrack, args=(0, 0,))
        t1.start()
        
        

    def get_next(self, x, y):
        if(y==8):
            return x+1 , 0
        else:
            return x , y+1


    def backtrack(self, x, y):
        if(x==9 and y==0):
            self.solving = False
            self.solved = True
            return True
        if self.tiles[x][y].present:
            nx , ny = self.get_next(x , y)
            return self.backtrack(nx , ny)
        else:
            for i in range(1 , 10):
                self.board[x][y] = str(i)
                self.tiles[x][y].text = str(i)
                self.tiles[self.active_x][self.active_y].color = self.Green
                self.check_board()
                self.update_board()
                if self.tiles[x][y].color == self.Green :
                    nx , ny = self.get_next(x , y)
                    if self.backtrack(nx , ny):
                        return True
                    self.board[x][y] = '-'
                    self.tiles[x][y].text = ''
                    self.tiles[self.active_x][self.active_y].color = self.Green
                else:
                    self.board[x][y] = '-'
                    self.tiles[x][y].text = ''
                    self.tiles[self.active_x][self.active_y].color = self.Green
                if(i == 9):
                    return False
        return True

board = Board()
