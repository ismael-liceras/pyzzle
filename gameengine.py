import pygame
from pygame.locals import *
from piece import Piece
from gap import Gap
from sprite import SpriteManager


class GameEngine():

    def __init__(self, image_file, factor):
        pygame.init()
        pygame.mouse.set_visible(1)
        pygame.display.set_caption('PyZZLE: ' + image_file + " - " + str((int(factor)*int(factor))-1) + " pieces")

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

        # Dealing with gap
        self.gap = Gap(int(self.factor))

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
            elif event.type == MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_piece = [s for s in self.sprites if s.rect.collidepoint(pos)]
                if len(clicked_piece) > 0:
                    distance = self.gap.get_distance_to_position(clicked_piece[0].get_position())
                    if abs(distance[0]) <= 1 and abs(distance[1]) <= 1 and abs(distance[0]) != abs(distance[1]):
                        self.gap.set_current_position(clicked_piece[0].do_slide(distance))
                else:
                    print self.gap.get_current_position()

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

    def generate_picture_sprites(self, image, factor, gap):
        piece_width = image.get_width() // factor
        piece_height = image.get_height() // factor
        w = h = 0
        for x in range(1, factor+1):
            for y in range(1, factor+1):
                if (gap is False) or x is not factor or y is not factor:
                    sprite_img = SpriteManager.load(image, w, h, piece_width, piece_height)
                    piece = Piece(sprite_img, (w, h), (x, y), factor)
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