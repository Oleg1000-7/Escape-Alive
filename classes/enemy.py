import pygame
from classes.entity import Entity


class Enemy(Entity):
    def __init__(self, group, image, pos_x, pos_y, size, hp, speed=0):
        super().__init__(group, image, pos_x, pos_y, size, hp)

    def update(self, **kwargs):
        if "dt" in kwargs:
            self.move(kwargs["dt"])

    def move(self, delta_time):
        pass

    def attack(self):
        pass