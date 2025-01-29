from typing import Any

import pygame

from sprite_groups import all_sprites

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self, groups: Any = None):
        if groups is not None:
            super().__init__(all_sprites, groups)
        else:
            super().__init__(all_sprites)