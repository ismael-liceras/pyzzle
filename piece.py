import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, image, initial_position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = initial_position

    def update(self):
        pass