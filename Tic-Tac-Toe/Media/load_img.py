import pygame
import os

class Media:
    current_path = os.path.dirname(__file__)
    pygame.init()
    temp = pygame.display.set_mode((0, 0))
    X = pygame.image.load(os.path.join(
        current_path, "X.png")).convert_alpha()
    O = pygame.image.load(os.path.join(
        current_path, "O.png")).convert_alpha()
    pygame.quit()
