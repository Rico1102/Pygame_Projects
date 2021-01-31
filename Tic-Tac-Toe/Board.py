import pygame
from Tile import Tile


class Board():
    def __init__(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Tic Tac Toe')
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.Green = (0, 255, 0)
        self.Blue = (0, 0, 128)
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.tiles = [[], [], []]
        row = 0
        for i in self.board:
            for j in i:
                self.tiles[row].append(Tile(False))
            row += 1
        # self.play_game()

    def create_outline(self, x, y, s_x=70, s_y=70):
        pygame.draw.line(self.canvas, self.Black, [x, y], [x+s_x, y], 1)
        pygame.draw.line(self.canvas, self.Black, [x+s_x, y], [x+s_x, y+s_y], 1)
        pygame.draw.line(self.canvas, self.Black, [x+s_x, y+s_y], [x, y+s_y], 1)
        pygame.draw.line(self.canvas, self.Black, [x, y+s_y], [x, y], 1)

    def create_rect(self, x, y, s_x, s_y):
        pygame.draw.rect(self.canvas, self.White, [x, y, s_x, s_y])
        self.create_outline(x, y, s_x, s_y)

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                self.tiles[i][j].pos_y = i * 70 + 45
                self.tiles[i][j].pos_x = j * 70 + 45
                self.tiles[i][j].board_x = i
                self.tiles[i][j].board_y = j
                self.create_rect(i*70+45, j*70+45, 70, 70)

    def draw_tiles(self):
        for i in self.tiles:
            for j in i:
                if j.present:
                    j.draw_tile(self.canvas)

    def update_board(self):
        self.canvas.fill(self.White)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render("Tic Tac Toe", True, self.Green)
        textRect = text.get_rect()
        textRect.center = (150, 22)
        self.canvas.blit(text, textRect)
        self.draw_board()
        self.draw_tiles()
        pygame.display.update()

    def play_game(self, turn=0):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.destroy_board()
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    x = (pos[1] - 45)//70
                    y = (pos[0] - 45)//70
                    if((x < 3 and x >= 0) and (y < 3 and y >= 0) and not self.tiles[x][y].present):
                        if turn == 0:
                            self.board[x][y] = 'X'
                            self.tiles[x][y] = Tile(True, 'X')
                        else:
                            self.board[x][y] = 'O'
                            self.tiles[x][y] = Tile(True, 'O')
                        self.update_board()
                        return True

    def destroy_board(self):
        pygame.quit()

    def show_text(self, statment):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render(statment, True, self.Green)
        textRect = text.get_rect()
        textRect.center = (150, 150)
        self.canvas.blit(text, textRect)
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render("MENU", True, self.Blue)
        textRect = text.get_rect()
        textRect.center = (275, 17)
        self.canvas.blit(text, textRect)
        pygame.display.update()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.destroy_board()
                    exit(0)
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if(pos[0]>=245 and pos[1]<=33):
                        run = False
                        break
