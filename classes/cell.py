from typing import Iterator

import pygame

from classes.sprite_base import SpriteObject
from constants import FPS
from functions import load_image


class Cell(SpriteObject):
    def __init__(self, image: pygame.Surface | list[str] | Iterator, pos_x: int, pos_y: int,
                 groups: list[pygame.sprite.Group] | pygame.sprite.Group | None = None, animation_speed: int = FPS):
        super().__init__(groups)
        if isinstance(image, pygame.Surface):
            self.image = image
            self.animated = False
        else:
            self.images = image
            self.animated = True
            self.tick = 0
            self.frame = 0
            self.animation_speed = animation_speed
            self.image = self.animate()

        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.center = self.rect.center

    def update(self, *args, **kwargs):
        if self.animated:
            if self.tick <= self.animation_speed:
                self.tick += 1
            else:
                self.center = self.rect.center
                self.tick = 0
                self.image = self.animate()
                if self.image:
                    self.rect = self.image.get_rect(center=self.center)

    def animate(self) -> pygame.Surface:
        if isinstance(self.images, list):
            self.frame = self.frame + 1 if not self.frame + 1 >= len(self.images) else 0
            return load_image(self.images[self.frame], do_resize=False)
        else:
            try:
                return load_image(next(self.images), do_resize=False)
            except StopIteration:
                for group in self.groups():
                    group.remove(self)
                self.kill()
