import pygame
from pygame.locals import *
from piece import Piece
from sprite import SpriteManager


class GameEngine():

    def __init__(self, image_file, factor):
        pygame.init()
        pygame.mouse.set_visible(1)
        pygame.display.set_caption('PyZZLE: ' + image_file + " - " + factor + "*" + factor + " pieces")

        #Initializing parameters
        try:
            self.image = pygame.image.load(image_file)
        except:
            #TODO To improve exception management here
            print 'Error loading image'
            exit()
        self.factor = factor
        self.clock = pygame.time.Clock()

        # Background management
        self.screen = pygame.display.set_mode((self.image.get_width(), self.image.get_height()))
        rect = pygame.Rect((0, 0, self.image.get_width(), self.image.get_height()))
        self.background = pygame.Surface(rect.size)
        self.render_background_tiles()

        # Displaying image as tiles (sprites)
        self.last_piece = None
        self.sprites = pygame.sprite.RenderPlain()
        self.generate_picture_sprites(self.image, int(self.factor), True)

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
        #self.screen.blit(self.background, (0, 0))

    def generate_picture_sprites(self, image, factor, gap):
        piece_width = image.get_width() // factor
        piece_height = image.get_height() // factor
        w = h = original_position_id = 0
        while w < self.screen.get_width():
            while h < self.screen.get_height():
                original_position_id += 1
                if (gap is False) or (original_position_id != (factor*factor)):
                    sprite_img = SpriteManager.load(image, w, h, piece_width, piece_height)
                    piece = Piece(sprite_img, (w, h), original_position_id)
                    piece.add(self.sprites)
                    h += piece_height
                else:
                    break
            w += piece_width
            h = 0
        self.last_piece = piece

    def do_play(self):
        self.clock.tick(60)
        self.update_sprites()
        self.draw_everything()

    def draw_everything(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def update_sprites(self):
        self.sprites.update()