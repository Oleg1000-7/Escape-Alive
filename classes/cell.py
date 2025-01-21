import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, group, image, pos_x, pos_y, size: tuple|int, hit_box=False):
        super().__init__(group)
        self.image = image
        x, y = size if type(size) == tuple else size, size
        self.rect = self.image.get_rect().move(x * pos_x, y * pos_y)
        self.has_hit_box = hit_box
