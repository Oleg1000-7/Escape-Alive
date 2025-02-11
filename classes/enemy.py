from typing import Iterator

import pygame.time
from pygame.sprite import spritecollide

from classes.entity import Entity
from constants import ENEMIES_ATTACK_COOLDOWN, ENEMIES_AGRO_DISTANCE
from functions import get_dist
from sprite_groups import entities, moving
from classes.player import player


class Enemy(Entity):
    def __init__(self, image: pygame.Surface | list[str] | Iterator, pos_x: int, pos_y: int, hp: int,
                 speed: int = 0, damage: int = 5, cost: int = 5):
        super().__init__(image, pos_x, pos_y, hp, groups=moving)
        self.speed = speed
        self.agro_distance = ENEMIES_AGRO_DISTANCE
        self.stop_distance = max(self.rect.h, self.rect.w) // 4
        self.damage = damage
        self.previous_attack = 0
        self.do_attack = False
        self.cost = cost

    def update(self):
        if self.hp <= 0:
            player.add_money(self.cost)
        super().update()
        if player.moved:
            d = get_dist(self.rect.center, player.rect.center)
            if self.agro_distance > d:
                self.do_attack = self.move(d)
            if self.do_attack:
                self.attack()
                self.do_attack = False

    def move(self, d):
        collides = list()
        xp, yp = player.rect.center
        dx, dy = abs(self.rect.centerx - xp), abs(self.rect.centery - yp)

        if not self.speed == 1:
            sin = dx / d
            cos = dy / d

        else:
            sin = cos = 1

        if dx > self.stop_distance:
            delta_x = int(self.speed * sin if xp > self.rect.centerx else -self.speed * sin)
            self.rect.x += delta_x

            collides = spritecollide(self, moving, False)
            if spritecollide(self, entities, False) or len(collides) > 1:
                self.rect.x -= delta_x

        if dy > self.stop_distance:
            delta_y = int(self.speed * cos if yp > self.rect.centery else -self.speed * cos)
            self.rect.y += delta_y

            collides = spritecollide(self, moving, False)
            if spritecollide(self, entities, False) or len(collides) > 1:
                self.rect.y -= delta_y

        return player in collides

    def attack(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.previous_attack > ENEMIES_ATTACK_COOLDOWN:
            player.get_damage(self.damage)
            self.previous_attack = current_tick
