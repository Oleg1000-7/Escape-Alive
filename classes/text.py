import pygame

from classes.sprite_base import SpriteObject
from constants import BLACK


class Text(SpriteObject):
    def __init__(self, text: str, pos_x: int, pos_y: int, color: pygame.Color | tuple[int, int, int] = BLACK):
        super().__init__()
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.color = color

    def set_text(self, text: str) -> None:
        self.image = self.font.render(text, True, self.color)
