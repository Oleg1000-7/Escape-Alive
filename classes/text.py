import pygame

from classes.sprite_base import SpriteObject
from constants import BLACK


class Text(SpriteObject):
    def __init__(self, text: str, pos_x: int, pos_y: int, color: pygame.Color | tuple[int, int, int] = BLACK):
        super().__init__()
        font = pygame.font.Font(None, 50)
        self.image = font.render(text, True, color)
        self.rect = self.image.get_rect().move(pos_x, pos_y)