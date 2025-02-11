import math
import os
from typing import Iterator

import pygame

from classes.cell import Cell
from constants import FPS, WIDTH
from functions import get_dist
from sprite_groups import entities, moving


class Particle(Cell):
    def __init__(self, image: pygame.Surface | list[str] | Iterator, parent, pos_x: int, pos_y: int,
                 animation_speed: int = FPS, kill_on_collide: bool = False):
        super().__init__(image, pos_x, pos_y, animation_speed=animation_speed)
        self.parent = parent
        self.active = True
        self.kill_on_collide = kill_on_collide

    def update(self, *args, **kwargs):
        super().update()
        if self.active:
            self.collision()

    def collision(self):
        target = pygame.sprite.spritecollideany(self, entities)
        if not target:
            target = pygame.sprite.spritecollide(self, moving, False)
            if self.parent in target:
                target.remove(self.parent)
            if target:
                target = target[0]
        if target:
            self.parent.deal_damage(target)
            if self.kill_on_collide:
                self.destroy()
            else:
                self.active = False


class Punch(Particle):
    def __init__(self, parent, pos_x: int, pos_y: int, animation_speed: int = FPS):
        image = iter(map(lambda x: "other/punches/" + x, os.listdir("data/other/punches")))
        super().__init__(image, parent, pos_x, pos_y, animation_speed=animation_speed)


class Bullet(Particle):
    def __init__(self, parent, image: pygame.Surface, pos_x: int, pos_y: int, angle: float, speed: int = 5):
        self.speed = speed
        self.angle = angle
        self.parent = parent

        super().__init__(image, parent, pos_x, pos_y, kill_on_collide=True)
        self.image = pygame.transform.rotate(image, math.degrees(self.angle))
        self.rect = self.image.get_rect(center=image.get_rect(center=self.parent.rect.center).center)

    def update(self, *args, **kwargs):
        self.rect.x += self.speed * math.cos(self.angle)
        self.rect.y -= self.speed * math.sin(self.angle)

        if get_dist(self.parent.rect, self.rect) > WIDTH * 1.5:
            self.destroy()

        super().update()
