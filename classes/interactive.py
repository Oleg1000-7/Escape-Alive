import pygame

from classes.cell import Cell
from sprite_groups import interactive, all_sprites


class Interactive(Cell):
    def __init__(self, image: pygame.Surface, pos_x: int, pos_y: int, hit_box: bool = False):
        super().__init__(image, pos_x, pos_y, groups=interactive)

    def interaction(self):
        interactive.remove(self)
        all_sprites.remove(self)
        self.kill()

