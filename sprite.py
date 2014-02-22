import pygame


class SpriteManager():

    @staticmethod
    def load(sprites, sprite_x, sprite_y, width, height):
        rect = pygame.Rect((sprite_x, sprite_y, width, height))
        image = pygame.Surface(rect.size, pygame.SRCALPHA)
        image.blit(sprites, (0, 0), rect)
        return image

    @staticmethod
    def load_all(sprites, sprite_x, sprite_y, width, height):
        image = SpriteManager.load(sprites, sprite_x, sprite_y, width, height)
        rect = image.get_rect()
        return image, rect