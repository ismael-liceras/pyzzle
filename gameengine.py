import pygame
from pygame.locals import *


class GameEngine():

    def __init__(self, image_file):
        pygame.init()
        try:
            image = pygame.image.load(image_file)
        except:
            #TODO To improve exception management here
            print 'Error loading image'
            exit()
        self.screen = pygame.display.set_mode((image.get_width(), image.get_height()))
        rect = pygame.Rect((0, 0, image.get_width(), image.get_height()))
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