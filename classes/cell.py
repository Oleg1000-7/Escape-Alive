import pygame

from classes.sprite_base import SpriteObject

class Cell(SpriteObject):
    def __init__(self, image: pygame.Surface, pos_x: int, pos_y: int, groups: list[pygame.sprite.Group] | pygame.sprite.Group | None = None,
                 hit_box: bool = False):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.has_hit_box = hit_box
