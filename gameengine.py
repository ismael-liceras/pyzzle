import pygame
from pygame.locals import *


class GameEngine():

    def __init__(self, image_file, factor):
        pygame.init()

        #Initializing parameters
        try:
            image = pygame.image.load(image_file)
        except:
            #TODO To improve exception management here
            print 'Error loading image'
            exit()
        self.factor = factor

        # Background management
        self.screen = pygame.display.set_mode((image.get_width(), image.get_height()))
        rect = pygame.Rect((0, 0, image.get_width(), image.get_height()))
        self.background = pygame.Surface(rect.size)
        self.render_background_tiles()
        pygame.display.flip()

        #TODO NEXT Create a piece object...
        ## ... divide image in pieces depending on factor
        ## ... display the correct image on each piece
        ## ... display borders on this image, to make pieces effect
        ## ... display a generic image to fill the background

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                return -1
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return -1

    def render_background_tiles(self):
        background_tile = pygame.image.load('background.jpg')
        tile_rect = pygame.Rect((0, 0, background_tile.get_width(), background_tile.get_height()))
        w = h = 0
        while w < self.screen.get_width():
            while h < self.screen.get_height():
                self.background.blit(background_tile, (w, h), tile_rect)
                h += background_tile.get_height()
            w += background_tile.get_width()
            h = 0
        self.screen.blit(self.background, (0, 0))