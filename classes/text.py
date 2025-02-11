import pygame

from constants import BLACK
from sprite_groups import hud_elements


class Text(pygame.sprite.Sprite):
    def __init__(self, text: str, pos_x: int, pos_y: int, color: pygame.Color | tuple[int, int, int] = BLACK):
        super().__init__(hud_elements)
        self.font = pygame.font.Font(None, 50)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        self.color = color

    def set_text(self, text: str) -> None:
        self.image = self.font.render(text, True, self.color)

    def update(self, screen):
        screen.blit(self.image, self.rect)
