import pygame
from pygame.locals import *


class GameEngine():

    def __init__(self, image_file):
        pygame.init()

        image = pygame.image.load(image_file)
        self.screen = pygame.display.set_mode((800, 600))
        rect = pygame.Rect((0, 0, 800, 600))
        self.background = pygame.Surface(rect.size)
        self.background.blit(image, (0, 0), rect)
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return -1
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return -1