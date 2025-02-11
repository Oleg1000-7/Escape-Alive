import pygame

from classes.cell import Cell

class Entity(Cell):
    def __init__(self, image: pygame.Surface, pos_x: int, pos_y: int, hp: int, groups=None):
        super().__init__(image, pos_x, pos_y, groups=groups)
        self.hp = hp

    def update(self):
        super().update()
        if self.hp <= 0:
            self.kill()

    def get_damage(self, damage: int) -> None:
        self.hp -= damage
