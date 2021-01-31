import pygame
from Multiplayer import Game

class Mode():
    def __init__(self):
        self.canvas = None
        self.White = (255, 255, 255)
        self.Black = (0, 0, 0)
        self.Green = (0, 255, 0)
        self.show_menu()
        self.show()

    def show_menu(self):
        pygame.init()
        self.canvas = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Tic Tac Toe')
        self.canvas.fill(self.White)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Single Player", True, self.White)
        textRect = text.get_rect()
        textRect.center = (150, 100)
        pygame.draw.rect(self.canvas, self.Black, [45, 75, 210, 50])
        self.canvas.blit(text, textRect)
        font = pygame.font.Font('freesansbold.ttf', 30)
        text = font.render("Multi Player", True, self.White)
        textRect = text.get_rect()
        textRect.center = (150, 200)
        pygame.draw.rect(self.canvas, self.Black, [45, 175, 210, 50])
        self.canvas.blit(text, textRect)
        pygame.display.update()

    def show(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if(pos[0]>=45 and pos[0]<=255 and pos[1]>=75 and pos[1]<=125):
                        self.destroy_board()
                        self.show_menu()
                    if(pos[0] >= 45 and pos[0] <= 255 and pos[1] >= 175 and pos[1] <= 225):
                        self.destroy_board()
                        game = Game()
                        self.show_menu()

    def destroy_board(self):
        pygame.quit()

mode = Mode()
