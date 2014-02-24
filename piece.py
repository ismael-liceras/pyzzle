import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, image, initial_position, original_position_id, factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.factor = factor
        self.original_position_id = self.current_position_id = original_position_id
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (50, 50, 50), self.rect, 1)
        self.rect.topleft = initial_position
        self.move = 0
        self.stopping_at = (0, 0)

    def do_slide(self):
        self.move = 10
        self.stopping_at = (self.rect.left + self.image.get_width(), self.rect.top)
        old_position_id = self.current_position_id
        self.current_position_id += self.factor
        return old_position_id

    def update(self):
        if self.move is not 0:
            new_pos = self.rect.move((self.move, 0))
            if new_pos.left > self.stopping_at[0]:
                self.move = 0
                new_pos.left = self.stopping_at[0]
            self.rect = new_pos