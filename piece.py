import pygame


class Piece(pygame.sprite.Sprite):
    def __init__(self, image, initial_position, original_position, factor):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.factor = factor
        self.original_position = self.current_position = original_position
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (50, 50, 50), self.rect, 1)
        self.rect.topleft = initial_position
        self.move = (0, 0)
        self.stopping_at = (0, 0)

    def do_slide(self, move):
        self.move = (10 * move[0], 10 * move[1])
        self.stopping_at = (self.rect.left + (self.image.get_width() * move[0]),
                            self.rect.top + (self.image.get_height() * move[1]))
        old_position = self.current_position
        self.current_position = (self.current_position[0] + move[0], self.current_position[1] + move[1])
        return old_position

    def get_position(self):
        return self.current_position

    def update(self):
        if self.move != (0, 0):
            new_pos = self.rect.move((self.move[0], self.move[1]))
            if new_pos.left > self.stopping_at[0] or new_pos.top > self.stopping_at[1]:
                self.move = (0, 0)
                new_pos.left = self.stopping_at[0]
                new_pos.top = self.stopping_at[1]
            self.rect = new_pos