import pygame

from classes.sprite_base import SpriteObject
from functions import load_image

class Cell(SpriteObject):
    def __init__(self, image: str, pos_x: int, pos_y: int, groups: list[pygame.sprite.Group] | pygame.sprite.Group | None = None,
                 hit_box: bool = False):
        super().__init__(groups)
        self.image = load_image(image, (50, 50))
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.has_hit_box = hit_box
