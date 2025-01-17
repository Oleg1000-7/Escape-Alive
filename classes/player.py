import pygame

from constants import *

class Player(pygame.sprite.Sprite):
    def __init__(self, all_sprites, player_image, pos_x, pos_y, speed=10):
        super().__init__(all_sprites)
        self.image = player_image
        self.pos_x, self.pos_y = pos_x, pos_y
        self.rect = self.image.get_rect().move(self.pos_x, self.pos_y)
        self.speed = speed

    def move(self, key, entities, delta_time):
        delta_x, delta_y = 0.0, 0.0
        speed = self.speed * delta_time

        if key == pygame.K_UP:
            delta_x, delta_y = 0, -speed
        if key == pygame.K_DOWN:
            delta_x, delta_y = 0, speed
        if key == pygame.K_LEFT:
            delta_x, delta_y = -speed, 0
        if key == pygame.K_RIGHT:
            delta_x, delta_y = speed, 0

        self.rect.x += delta_x
        self.rect.y += delta_y

        if pygame.sprite.spritecollideany(self, entities):
            self.rect.x -= delta_x
            self.rect.y -= delta_y