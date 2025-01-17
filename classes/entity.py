import pygame
from classes.cell import Cell

class Entity(Cell):
    def __init__(self, group, image, pos_x, pos_y, size, hp, speed=0):
        super().__init__(group, image, pos_x, pos_y, size)
        self.hp = hp
        self.speed = speed

    def update(self):
        if self.hp <= 0:
            self.kill()