import math
import os
import pygame

from classes.cell import Cell
from constants import FPS, WIDTH
from functions import get_dist
from sprite_groups import entities, moving


class Punch(Cell):
    def __init__(self, parent, pos_x: int, pos_y: int, animation_speed: int = FPS):
        image = iter(map(lambda x: "other/punches/" + x, os.listdir("data/other/punches")))
        super().__init__(image, pos_x, pos_y, animation_speed=animation_speed)
        self.parent = parent

    def destroy(self):
        for group in self.groups():
            group.remove(self)
        self.kill()

    def update(self):
        super().update()
        target = pygame.sprite.spritecollideany(self, entities)
        if not target:
            target = pygame.sprite.spritecollide(self, moving, False)
            if self.parent in target:
                target.remove(self.parent)
            if target:
                target = target[0]

        if target:
            self.parent.deal_damage(target)
            self.destroy()


class Bullet(Cell):
    def __init__(self, parent, image: pygame.Surface, pos_x: int, pos_y: int, angle: float, speed: int = 5):
        super().__init__(image, pos_x, pos_y)
        self.speed = speed
        self.angle = angle
        self.image = pygame.transform.rotate(image, math.degrees(self.angle))
        self.parent = parent
        self.rect = self.image.get_rect(center=image.get_rect(center=self.parent.rect.center).center)

    def destroy(self):
        for group in self.groups():
            group.remove(self)
        self.kill()

    def update(self):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)

        if get_dist(self.parent.rect, self.rect) > WIDTH * 1.5:
            self.destroy()

        target = pygame.sprite.spritecollideany(self, entities)
        if not target:
            target = pygame.sprite.spritecollide(self, moving, False)
            if self.parent in target:
                target.remove(self.parent)
            if target:
                target = target[0]

        if target:
            self.parent.deal_damage(target)
            self.destroy()
