import pygame
from pygame.locals import *
from piece import Piece
from sprite import SpriteManager


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

        # Background management
        self.screen = pygame.display.set_mode((image.get_width(), image.get_height()))
        rect = pygame.Rect((0, 0, image.get_width(), image.get_height()))
        self.background = pygame.Surface(rect.size)
        self.render_background_tiles()

        # Displaying image as tiles (sprites)
        self.sprites = pygame.sprite.RenderPlain()
        self.generate_picture_sprites(image, int(factor))

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

    def generate_picture_sprites(self, image, factor):
        piece_width = image.get_width() // factor
        piece_height = image.get_height() // factor
        w = h = 0
        while w < self.screen.get_width():
            while h < self.screen.get_height():
                sprite_img = SpriteManager.load(image, w, h, piece_width, piece_height)
                piece = Piece(sprite_img, (w, h))
                piece.add(self.sprites)
                h += piece_height
            w += piece_width
            h = 0

    def do_play(self):
        self.update_sprites()
        self.draw_everything()

    def draw_everything(self):
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def update_sprites(self):
        self.sprites.update()