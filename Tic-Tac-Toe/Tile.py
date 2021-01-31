import pygame
from Media.load_img import Media

class Tile():
    def __init__(self, present, type=None):
        self.present = present
        self.character = ''
        self.pos_x = 0
        self.pos_y = 0
        self.board_x = 0
        self.board_y = 0
        self.image = None
        if type == 'X':
            self.image = Media.X
            self.image = pygame.transform.scale(self.image, (68, 68))
        else:
            self.image = Media.O
            self.image = pygame.transform.scale(self.image, (68, 68))

    def draw_tile(self, canvas):
        canvas.blit(self.image, (self.pos_x+1, self.pos_y+1))
