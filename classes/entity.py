import pygame
from classes.cell import Cell

class Entity(Cell):
    def __init__(self, image: str, pos_x: int, pos_y: int, size: tuple | int, hp: int, speed: int):
        super().__init__(image, pos_x, pos_y, size)
        self.hp = hp
        self.speed = speed

    def update(self):
        if self.hp <= 0:
            self.kill()