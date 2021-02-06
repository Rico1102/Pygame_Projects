import pygame

class Tile():
    def __init__(self, text="", fix=False):
        self.present  = fix
        self.text = text
        self.pos_x = 0
        self.pos_y = 0
        self.board_x = 0
        self.board_y = 0
        self.color = None
        if(fix):
            self.color = (0, 0, 0)
        else:
            self.color = (0 , 255, 0)

    def draw_tile(self, canvas, font):
        text = font.render(self.text , True, self.color)
        text_rect = text.get_rect()
        text_rect.center = (self.pos_x+19, self.pos_y+19)
        canvas.blit(text , text_rect)

